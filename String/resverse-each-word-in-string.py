# sentence = "GeeksforGeeks is good to learn"
# words = sentence.split(" ")
# new_words = [word[::-1] for word in words]
# new_sentence = " ".join(new_words)
# print(new_sentence)


sentence = "GeeksforGeeks is good to learn"
res=[word[::-1] for word in sentence.split(" ")]
print(" ".join(res))