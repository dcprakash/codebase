# reverse Words
words = "i.like.this.program.very.much".split('.')
n = len(words)
print n
while (n != 0):
    print words[n - 1]
    n = n - 1

print "\n \n"
string = "i.like.this.program.very.much"
list = string.split('.')
i= len(list) - 1
word = ""
while (i>=0):
    word += str(list[i])+'.'
    i -= 1
print word