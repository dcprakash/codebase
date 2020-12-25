n = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
d = {}
for i in n:
    d[i] = d[i]+1 if i in d else 1

for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
    print "{0} : {1}".format(key, value)

for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
    tempValue = value
    while tempValue!=0:
        print key
        tempValue-=1

#sort dict by keys
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}
print " sort dict by keys \n"
for key in sorted(mydict.iterkeys()):
    print " %s: %s" % (key, mydict[key])

print "\n sort dict by values \n"
for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)