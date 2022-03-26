words = 'The quick brown fox jumps over the lazy dog'.split()
print words
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print i