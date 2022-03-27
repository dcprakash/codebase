

#sort dict by keys or values

count = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

print(sorted(count.items(), key=lambda k: k[0]))

print(sorted(count.items(), key=lambda v: v[1], reverse=True))
print(sorted(count.items(), key=lambda v: v[1]))

