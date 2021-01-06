input = "A man, a plan, a canal: Panama"
input = filter(lambda ch: ch.isalnum(), input)
input = map(lambda ch: ch.lower(), input)
print("".join(input))
