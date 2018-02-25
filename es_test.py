from __future__ import print_function
import datetime
from Modules.elastic_utility import ElasticsearchUtils

ignore_fields = ["sads", "type", "tags", "beat", "input_type", "@timestamp", "source", "host", "offset", "message",
                 "@version"]

dump = ElasticsearchUtils().get_dataset_dump_timerange("rdpsuccess-*",ts1=0, ts2=1956528000, fields=ignore_fields)
print(dump)



'''
sys.path.insert (0, '/'.join (os.getcwd ().split ('/')[0:-1]) + '/' + "Modules")


#filter('range', ts={'gte': 1505803143.635668 , 'lt': 1505803163.635668})

#searchobj = Search (index = "blacklist1").using (es_conn)

#searchobj = elasticsearch_dsl.FacetedSearch('_all').search().using (es_conn)

#"aggs" : { "min_timestamp" : { "min" : { "field" : "DateTime" } } }}

FH = open (path + '/' + index, 'w')

if fields is None:
    searchobj = Search (index=index).using (self.es_conn)
else:
    if any(fields) and ignore_fields:
        searchobj = Search (index=index).using (self.es_conn).source(include=fields)
    else:
        searchobj = Search (index=index).using (self.es_conn).source (exclude=fields)


FH.write (','.join (fields) + '\n')
for hit in searchobj.scan ():
    line = ""
    all_fields = hit.to_dict ()
    for field in fields:
        line = line + str (all_fields[field]) + ','
    line = line + '\n'
    FH.write (line)
FH.close ()



# for hit in searchobj.scan():
#     print hit.to_dict()




#Testing


testindex = 'blacklist1'

testobj = ElasticsearchUtils ()

print(testobj.es_node)

testobj1 = ElasticsearchUtils ()

specific_fields = ['URL/IP']


testobj.dump_index ('blacklist1', testindex, ignore_fields, True)
t1 = datetime.datetime.now ()
'''
'''
print "Total_records", testobject.es_index_count(testindex)
print "All Records:\n", testobject.es_dump_all_index(esdumpath, testindex)
print "Specific Records:\n", testobject.es_dump_all_index(esdumpath,testindex,specific_fields, False)
print "All but ignore system specific fields:\n", testobject.es_dump_all_index(esdumpath,testindex,ignore_fields,True)


print "Stats\n"
print "Total_records:", testobject.es_index_count(testindex)
print "My Schema:\n", testobject.es_index_fields(testindex)
print "Total Fields counts", testobject.es_index_fields_count(testindex)
t2 = datetime.datetime.now()
print "Time_taken: ", t2 - t1


testindex = 'rdpsuccess-2017.09.19'

t1 = datetime.datetime.now()
#print "Dump all Records:\n", testobject.es_dump_all_index(testindex)
print "Dum Specific Records :\n", testobject.es_dump_all_index(testindex,['source','host','resp_p','orig_p','resp_h','orig_h'])

print "Specific Records:\n", testobject.es_dump_all_index(testindex,['source','host','resp_p','orig_p','resp_h','orig_h'])


print "Stats\n"
print "Total_records:", testobject.es_index_count(testindex)
print "My Schema:\n", testobject.es_index_fields(testindex)
print "Total Fields counts", testobject.es_index_fields_count(testindex)
t2 = datetime.datetime.now()
print "Time_taken: ", t2 - t1


'''
