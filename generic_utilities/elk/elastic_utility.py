import csv
import re
import time
from functools import wraps

import elasticsearch
from elasticsearch import exceptions
from elasticsearch_dsl import Search

max_retries = 5
max_delay = 2
timeout = 60


def retry(ExceptionToCheck, tries=max_retries, delay=max_delay):
    """The decorator for re-trying on exceptions while estabilishing the connections to elasticserach Server"""

    def deco_retry(f):
        @wraps (f)
        def f_retry(*args, **kwargs):
            mtries = tries
            while mtries > 0:
                try:
                    return f (*args, **kwargs)
                except ExceptionToCheck as e:
                    print(e)
                    print('Retrying in %d seconds ' % delay)
                    time.sleep (delay)
                    mtries -= 1
            try:
                return f (*args, **kwargs)
            except ExceptionToCheck as e:
                print('Fatal Error: %s' % e)
                exit (1)

        return f_retry

    return deco_retry


def SingleTon(Object):
    """ Decorator to enforce the Single Instance of the ElasticsearchUtils"""
    instance = {}

    def checkInstance(*args, **kwargs):
        if Object not in instance:
            instance[Object] = Object (*args, **kwargs)
        return instance[Object]

    return checkInstance


@SingleTon
class ElasticsearchUtils (object):
    """ This class provides methods and properties for pulling the documents and their various stats stored in 
    ElasticSearch """

    def __init__(self, es_node="192.168.133.216", es_port="6775"):
        self.es_port = es_port
        self.es_node = es_node
        self.es_client = self._get_es_client
        self.es_conn = self._es_connection (timeout)

    @property
    def _get_es_client(self):
        return str (self.es_node) + ':' + str (self.es_port)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def _es_connection(self, time_out):
        return elasticsearch.Elasticsearch (self.es_client, timeout=time_out)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_exists(self, index):
        """ Return True if an Index exists in the ElasticSearch"""
        return self.es_conn.indices.exists (index=index)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_count(self, index):
        """Returns the count of records of an Elasticsearch Index"""
        return self.es_conn.count (index=index)['count']

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_list(self):
        """Returns the list of all Indices present in the Elasticsearch"""
        cat_response = self.es_conn.cat.indices ().strip ().split ('\n')
        if any (cat_response):
            list_index = map (lambda x: x.split ()[2], cat_response)
            return list_index
        else:
            return []

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_pattern_list(self, index):
        """Returns the List of indices present in Elasticsearch matching to the provided Index. """
        indexpatternlist = []
        if any (self.es_index_list ()):
            for myindex in self.es_index_list ():
                result = re.match (index, myindex)
                if result:
                    indexpatternlist.append (myindex)
        return indexpatternlist

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_pattern_exists(self, index):
        """Returns True if the index pattern exists in the Elasticsearch."""
        if any (self.es_index_pattern_list (index)):
            return True
        return False

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_pattern_count(self, index):
        """Returns the Total counts of indices in elasticsearch matching to the provided pattern or string
        :param index:
        :return:
        """
        s = Search (index=index).using (self.es_conn)
        try:
            return s.execute ().hits.total
        except:
            return 0
    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_pattern_count_hash(self, index):
        """Returns the Total counts of records in each indices in elasticsearch matching to the provided pattern or
        string """
        matching_indices = self.es_index_pattern_list (index)
        myindex = {}
        if any (matching_indices):
            for index in matching_indices:
                myindex[index] = int (self.es_conn.count (index=index)['count'])
        return myindex

    @retry (exceptions.ConnectionError, tries=max_retries)
    def _es_index_mapping_name(self, index):
        """Returns the Mappings of an elasticsearch Index"""
        try:
            return self.es_conn.indices.get (index).get (index, None).get ('mappings', None).keys ()[0]
        except AttributeError as e:
            print('Invalid Index', e)
            exit (1)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_fields(self, index):
        """Returns the actual record schema of an elasticsearch Index
        :rtype: List
        """
        mappings = self._es_index_mapping_name (index)
        index_mapping = self.es_conn.indices.get (index)[index]
        return index_mapping.get ('mappings').get (mappings).get ('properties').keys ()

    @retry (exceptions.ConnectionError, tries=max_retries)
    def es_index_fields_count(self, index):
        """Returns the actual record fields count of an elasticsearch Index"""
        return len (self.es_index_fields (index))

    @retry (exceptions.ConnectionError, tries=max_retries)
    def get_mints_index_pattern(self, indexpattern, timefield="@timestamp"):
        """Returns the timestamp of the record in ealsticsearch index pattern which is the oldest"""
        body = dict (aggs={"min_timestamp": {"min": {"field": timefield}}})
        s = Search.from_dict (body)
        s = s.index (indexpattern).using (self.es_conn)
        t = s.execute ()
        return int (t.aggregations.min_timestamp.value)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def get_maxts_index_pattern(self, indexpattern, timefield="@timestamp"):
        """Returns the timestamp of the record in ealsticsearch index pattern which is the newest"""
        body = {"aggs": {"max_timestamp": {"max": {"field": timefield}}}}
        s = Search.from_dict (body)
        s = s.index (indexpattern).using (self.es_conn)
        t = s.execute ()
        return int (t.aggregations.max_timestamp.value)

    @retry (exceptions.ConnectionError, tries=max_retries)
    def get_dataset_dump_timerange(self, dataset, ts1, ts2, fields=None, timefield="gsi_ts"):
        """Returns the counts of the records in ealsticsearch index between the provided two Timestamp"""
        searchobj = Search (index=dataset).using (self.es_conn).source (exclude=fields).query ().filter ('range', **{
            timefield: {'gte': ts1, 'lt': ts2}})
        scanobj = searchobj.scan ()
        response = []
        for hit in scanobj:
            all_fields = hit.to_dict ()
            response.append (all_fields)
        return response

    @retry (exceptions.ConnectionError, tries=max_retries)
    def get_peak_of_index(self, index, timefield="@timestamp"):
        """Returns the peak of the index in elasticsearch by the no of records preserved in a second"""
        body = dict (
            aggs={"record": {"date_histogram": {"field": timefield, "interval": "1s", "order": {"_count": "desc"}}}})
        s = Search.from_dict (body)
        s = s.index (index).using (self.es_conn)
        t = s.execute ()
        return t.aggregations.record.buckets[0]['doc_count']

    @staticmethod
    def _write_index_to_file(path, index, searchobj):

        with open (path + '/' + index, 'w') as FH:
            scanobj = searchobj.scan ()
            all_fields = scanobj.next ().to_dict ()
            writer = csv.DictWriter (FH, all_fields.keys ())
            writer.writeheader ()
            writer.writerow (all_fields)
            for hit in scanobj:
                all_fields = hit.to_dict ()
                writer.writerow (all_fields)
            FH.close ()

    @retry (exceptions.ConnectionError, tries=max_retries)
    def dump_index(self, index, fields=None, ignore_fields=False):
        """Dumps all the records of an Elasticsearch Index to the CSV file namded as provided index"""
        if fields is None:
            dataset_fields = self.es_index_fields (index)
            searchobj = Search (index=index).using (self.es_conn).source (include=dataset_fields)
        elif any (fields) and ignore_fields:
            searchobj = Search (index=index).using (self.es_conn).source (exclude=fields)
        else:
            searchobj = Search (index=index).using (self.es_conn).source (include=fields)
        scanobj = searchobj.scan ()
        response = []
        for hit in scanobj:
            all_fields = hit.to_dict ()
            response.append (all_fields)
        return response
    @staticmethod
    def es_update(key, value):
        es_conn = elasticsearch.Elasticsearch ("192.168.112.52:9200")
        mydict = { "script": { "inline": "ctx.ip=\""+key+"\"","lang": "painless"},
                "query": { "term": { "abc": value} }
            }
        body=json.dumps(mydict)
        print(body)
        try:
            es_conn.update_by_query('xyz',body=body)
        except elasticsearch.exceptions.RequestError as e:
            print (e)
