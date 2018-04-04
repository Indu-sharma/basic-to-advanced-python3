#!/usr/bin/python
# __author__: "indusharma5@gmail.com"

from csv2es import elasticsearch as elastic
import time
import argparse
import re
import httplib
import json
from collections import defaultdict

def parse_config():
    parser = argparse.ArgumentParser (description='Utility to push CSV data to Elasticsearch')
    parser.add_argument ('--ineterpolation_duration', type=int, default=5,
                         help='Number of consecutive points to '                                                                         'interpolate, default=5')
    parser.add_argument ('--url', required=True, type=str, help='Elasticsearch URL, example : localhost:9200')
    parser.add_argument ('--csvfiles', required=True, type=str,
                         help='Comma seperated list of the csv files to Import, make sure first and second columns '
                              'are Date & Time fields')
    parser.add_argument ('--maxrows', type=int, default=1000000, help='Maximum rows to Import, default=1000000')
    parser.add_argument ('--stacked', action='store_true', default = True, required=False, help='Fields are stacked or Not ')
    parser.add_argument ('--project', required=True, type=str, help='prjectName_buildnumber')
    parser.add_argument ('--sampling', required=False, default=1, type=int, help='sampling interval')
    parser.add_argument ('--buildno', required=True, type=str, help='buildnumber')
    return parser


def get_result(operation, url, mycommand, myjson):
    connection = httplib.HTTPConnection (url)
    connection.request (operation,mycommand,myjson)
    response = connection.getresponse ()
    data = response.read ()
    return data

def get_previous_run(url,project,buildno):
    #curl -XGET http://192.168.50.113:9200/_cat/indices/analyticsengine_5.1.3*?h=i\&s=creation.date
    operation  = 'GET'
    mycommand = '_cat/indices/'+project+'*?h=i&s=creation.date'
    myjson = ''
    data = get_result(operation, url, mycommand, myjson)
    if data.strip():
        latest_index = [ i for i in data.split('\n') if i]
	latest_index = latest_index[-1]
    else:
        latest_index = None 
    return latest_index	                

def get_first_timestamp(url,myindex,mytype):
    #curl -XPOST http://192.168.50.113:9200/analyticsengine_5.1.3_1/job_aggregator/_search -d  '{ "aggs" : { "min_timestamp" : { "min" : { "field" : "DateTime" } } }}'
    operation = 'POST'
    mycommand = '/'+myindex+'/'+mytype+'/_search'
    myjson = { "aggs" : { "min_timestamp" : { "min" : { "field" : "DateTime" } } }}
    myjson = json.dumps(myjson)
    data = get_result(operation,url,mycommand,myjson)
    mydict = json.loads(data)
    try:
        oldts = mydict['aggregations']['min_timestamp']['value_as_string'].split('.')[0]
    except:
        oldts = 0
    return oldts

def main():
    args = parse_config ().parse_args ()
    url = args.url
    csvfiles = args.csvfiles
    project = args.project
    buildno = args.buildno
    stacked = args.stacked
    ineterpolationduration = args.ineterpolation_duration
    sampling = args.sampling
    maxrows = args.maxrows
    myoldindex = get_previous_run(url,project,buildno)
    print "myoldindex", myoldindex
    if myoldindex != None and project+'_'+buildno in myoldindex:
        Iteration = int(myoldindex.split('_')[-1]) + 1
    else:
        Iteration = 1 
    index = project+'_'+buildno+'_' + str (Iteration)
    print Iteration 
    for csvfile in csvfiles.split(','):
	print "Inserting data from  file::",csvfile
        mytype = csvfile.split('/')[-1].split('.')[0]
        if myoldindex != None:
            oldts = get_first_timestamp(url,myoldindex,mytype)
        else:
            oldts = 0 
        es = elastic (url, csvfile, index, maxrows, stacked, ineterpolationduration, sampling, oldts)
	es.insert_data ()
if __name__=="__main__":
    main ()
