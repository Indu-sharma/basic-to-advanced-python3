#!/usr/bin/python
# __author__: "indu.sharma@guavus.com"

import csv
import datetime
import httplib
import json
import re


class elasticsearch:
    def __init__(self, url, csvfile, index, maxrows=1000000, stacked=True, ineterpolationduration=5,sampling=1, oldts=0):
        self.sampling = sampling
        self.url = url
        self.csvfile = csvfile
        self.maxrows = int(maxrows)
        self.stacked = stacked
        self.interpolationduration = ineterpolationduration
        self.loopback = self.sampling * self.interpolationduration
        self.myindex = index
        self.mytype = self.csvfile.split('/')[-1].split ('.')[0]
        self.connection = httplib.HTTPConnection (self.url)
        FH = open (self.csvfile, 'rb')
        self.reader = FH.readlines()
        self.oldts = oldts
    def request_es_connection(self, operation, path, myjson):
        self.connection.request (operation, path, myjson)
        response = self.connection.getresponse ()
        data = response.read ()
        print operation, path, myjson, data,response.status
        return data

    def get_headers(self):
        headers = self.reader[0].strip('\n').strip('\r').split(',')
        return headers

    def split_fields (self):
        headers = self.get_headers()
        if self.stacked and 'system' not in self.mytype:
            heads = ','.join(headers)
            Process = list (set (re.findall ('.*?\s+\((.*?)\)\s+.*?', heads)))
            Fields = list (set (re.findall ('.*?\s+\(.*?\)\s+(.*?),', heads)))
        else:
            headers = map (lambda x: x.replace (')', '').replace (' ', '').replace ('(', ''), headers)
            Fields = headers[2:]
            headers = headers[:2] + [' (system) ' + i for i in headers[2:]]
            Process = ['system']
        return Fields, Process, headers

    def create_mappings(self):
        mymap = {}
        Fields = self.split_fields()[0]
        for field in Fields:
            mymap[field] = {"type": "double"}
        mymap["DateTime"] = {"type": "date"}
        mymap["processname"] = {"type": "text","fielddata":"true"}
        mydict = {self.mytype: {"properties": mymap}}
        final_mappings = json.dumps (mydict)
        return final_mappings

    def insert_mappings(self):
        final_mappings = self.create_mappings()
        try:
        	self.request_es_connection('PUT',self.myindex,'')
	except:
        	print "Index already exists, not creating!!"
	self.request_es_connection('PUT',self.myindex+'/'+self.mytype+'/_mapping',final_mappings)

    def gettimediff(self, datestring1, datestring2):
        d1 = datetime.datetime.strptime (datestring1, '%Y-%m-%dT%H:%M:%S')
        d2 = datetime.datetime.strptime (datestring2, '%Y-%m-%dT%H:%M:%S')
        diff = (d2 - d1).total_seconds ()
        return diff

    def normalise_date(self, datestring, offset):
        normalized_date = datetime.datetime.strptime (datestring, '%Y-%m-%dT%H:%M:%S') + datetime.timedelta(seconds=offset)
        normalized_date = normalized_date.strftime('%Y-%m-%dT%H:%M:%S')
        return normalized_date

    def insert_data(self):
        self.insert_mappings()
        lines = self.reader[1:]
        mycache = {}
        Fields, Process, headers = self.split_fields ()
        count = 0
        for row in lines:
            mydata = {}
            row = row.strip('\n').strip()
            if not row:
                continue	
            row = row.split(',')
            if len(row) < 3:
                continue
            if count == 0:
                mycurrentdt_first = row[0] + 'T' + row[1]
                if self.oldts: 
                    diff = self.gettimediff(mycurrentdt_first,self.oldts)
                else:
                    diff = 0     
            mycurrentdt = row[0] + 'T' + row[1]
            for pid in Process:
		mydatatemp = {}
                for field in Fields:			
                    if field.strip ():
                        pos = [i for i, word in enumerate (headers) if re.match ('.*? \(' + pid + '\) ' + field, word)]
                        if pos:
                            mydatatemp[field] = row[pos[0]]
                if all (mydatatemp.values ()):
                    mycache[pid] = [mycurrentdt, mydatatemp]
                else:  # If there is entry in cache && dateTime in the range of N seconds modify mydatatemp
                    if pid in mycache:
                        old_datetime = mycache[pid][0]
                        if self.gettimediff (old_datetime, mycurrentdt) <= self.loopback:
                            mydatatemp = mycache[pid][1]
                        else:
                            continue 
                mydatatemp["DateTime"] = self.normalise_date(mycurrentdt,diff) 
                for key, value in mydatatemp.iteritems ():
                    mydata[key] = value
                mydata["processname"] = pid
                _mydata = json.dumps (mydata)
                self.request_es_connection('PUT', '/' + self.myindex + '/' + self.mytype + '/' + pid + str (count), _mydata)
                count += 1
            print diff
            if count >= self.maxrows:
                exit ('Max no of rows processed!')
