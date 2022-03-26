words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for s in stuff:
    print(s)
    
print("----------------------------\n")    
items = [1,2,3,4,5]
print("Square root of each item in {}".format(items))
mapSquared = list(map(lambda x: x**2, items))
print(mapSquared)
