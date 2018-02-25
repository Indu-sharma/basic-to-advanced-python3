from __future__ import print_function
from ip_utils import IpUtils


class Annotation (object):
    def __init__(self):
        pass

    @staticmethod
    def applyenrichment(data_list, data_columns, ib_dict, ib_columns, default_ib_columns=None, sep=','):
        """
        :param data_list: List of dictionary of the data records
        :param data_columns: List of column names to enrich by
        :param ib_dict: Dictionary of Lists
        :param ib_columns:  List of IB column names to enrich
        :param sep: sepeartor for column names in data_columns or ib_columns incase of string
        :return: List of dictionary of the enriched data records
        """
        if not isinstance (default_ib_columns, list):
            default_ib_columns = default_ib_columns.split (sep)
        else:
            default_ib_columns = default_ib_columns

        if not isinstance (ib_columns, list):
            ib_columns = ib_columns.split (sep)
        else:
            ib_columns = ib_columns

        if not isinstance (data_columns, list):
            data_columns = data_columns.split (sep)
        else:
            data_columns = data_columns

        ib_columns = map (lambda x: x.title (), ib_columns)
        result_list = []
        # Avoid Multiple Look ups by maintaining cache for the matched IP if a record src/dst IP already encountered.
        local_cache = {}
        for record in data_list:
            for d_col in data_columns:
                for k, ib_col in enumerate (ib_columns):
                    enriched_fields = default_ib_columns[k]
                    try:
                        try:
                            enriched_fields = ib_dict.get (record[d_col])[k]
                        except TypeError:
                            pass
                        try:
                            if record[d_col] not in local_cache and ':' in record[d_col]:
                                matched_ip = IpUtils ().match_in_set (record[d_col], ib_dict.keys ())
                                local_cache[record[d_col]] = matched_ip
                            elif record[d_col] in local_cache:
                                matched_ip = local_cache.get (record[d_col])
                                enriched_fields = ib_dict.get (matched_ip)[k]
                            else:
                                pass
                        except:
                            pass
                    except:
                        pass
                    record[ib_col + '_' + d_col] = unicode (enriched_fields)
            result_list.append (record)
        return result_list


'''
# Testing
data = [{"srcIp": "10:10:10:0:0:0:0:2", "dstIp": "10.10.10.10"}, {"srcIp": "10.10.10.2", "dstIp": "10.10.10.20"}]
data_columns = "srcIp"
ib_dict = {"10:10:10::2": ['10', '20', 'Nepal', 'NE'], "10.10.10.10": ['100', '200', 'India', 'IN']}
ib_columns = ['lat', 'lang', 'country', 'code']

t1 = datetime.datetime.now ()

testobj = Annotation ()
result = testobj.ApplyEnrichment (data, data_columns, ib_dict, ib_columns)
for line in result:
    print (line)

t2 = datetime.datetime.now ()

print (t2 - t1)

'''
