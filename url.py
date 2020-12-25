import getopt
import sys
import urllib2
import timeit
import socket
import subprocess
from subprocess import Popen, PIPE
import os
import subprocess
import sys
import time






# response = urllib2.urlopen('http://python.org/')
# html = response.read()
# #print html
#
#
req = urllib2.Request('https://locus-a.wbx2.com/locus/api/v1/build_info')


def CheckURL(req):
    response = ''
    try:
        timeout = 10
        socket.setdefaulttimeout(timeout)
        start = timeit.default_timer()
        print "requesting url {}".format(req)
        response = urllib2.urlopen(req)
        stop = timeit.default_timer()
        print "HTTP status is 200, everything went will; below is your requested page"
        print response.read()
        runtime = stop - start
        print runtime
        return 200
    except urllib2.HTTPError as e:
        

        #dest = socket.gethostbyname(req)
        #proc = subprocess.Popen("tracert -d %s" % dest, shell=True,
        #                        stdout=subprocess.PIPE)
                                
        #p = Popen(['tracert', req], stdout=PIPE)
        # while True:
        #     line = p.stdout.readline()
        #     if not line:
        #         break
        print "Request Failed with HTTP Code {}".format(e.code)
        return e.code
        #print e.read()

if __name__=='__main__':
    #time.sleep(3)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:e:",
                                   ["env="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-e':
            req = arg

    f = open('./CheckURL_Log.txt', 'w+')
    f.write("hello")
    Response = CheckURL(req)
    print "Printing Response     ...".format(Response)
    while (Response!=200):
        time.sleep(3)
        print "Looping againg to see results"
        CheckURL(req)
        f.write("  Run time is %s \r\n" % str(Response))
    f.close()
