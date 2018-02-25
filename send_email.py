#!/usr/bin/python
import commands
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import sys
import subprocess
file=sys.argv[1]
cmd="cat "+file
(output,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
def sendmail(output):

    try:
        to_address=["indu.sharma@guavus.com"]
	print "Sending e-mail to :" + str(to_address)
        msg = MIMEMultipart()
        msg['From'] = 'NRMCSTSetup'
        msg['To'] =  "; ".join(to_address)
        msg['Subject'] = 'Check Collector Drop and memory-cpu usage'
        #message = str(output)
	message="abc"
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP("204.232.241.167")
        # identify ourselves to smtp gmail client
        #mailserver.ehlo()
        # secure our email with tls encryption
        #mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.sendmail(“indu.sharma@guavus.com",to_address[1],msg.as_string())
        mailserver.quit()
    except Exception,e:
        print e
sendmail(output)
