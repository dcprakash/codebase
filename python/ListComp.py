import sys
words = "Hello There How Are You".split()
stuff = [[w.lower(), w.upper(), len(w)] for w in words]
for i in stuff:
    print i