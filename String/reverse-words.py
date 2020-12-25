"""
Your module description
"""

def reverse(words):
    words=words.split('.')
    print(words)
    w=""
    # can also use this for loop
    # for i in reversed(range(len(words))):
    for i in range(len(words)-1,-1,-1):
       w+="".join([words[i], "."])
    print(w)


print("\n \n")
words="i.like.this.program.very.much"
reverse(words)


print "***********Worked Method************"
print(".".join(words.split(".")[::-1]))


print("\n \n")
print "method2"
words="i.like.this.program.very.much"
string = words.split('.')
l = len(string)-1
output = ""
while l >= 0:
    output += string[l]+"."
    l -= 1
print(output)

print("\n \n")
print "***********method3************"
words = words.split(".")
words = words[::-1]
words = ".".join(words)
print words

print("\n \n")
print "***********method3.1 ************"
words = "hello there how is it going".split(" ")[::-1]
print(" ".join(words))