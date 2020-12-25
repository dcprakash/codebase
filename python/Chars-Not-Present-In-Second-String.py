if __name__ == "__main__":
    str1 = "hello"
    str2 = "llo"
    for ch in str1:
        if str2.find(ch) != -1:
            continue
        print (ch)
        print ('')