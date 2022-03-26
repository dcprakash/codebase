import sys

# http://book.pythontips.com/en/latest/args_and_kwargs.html
# look for this in ida code

def testArgs(arg1, *args):
    print("testArgs")
    print("printing value of arg1 {}".format(arg1))
    for value in args:
        print("printing values of args {}".format(value))
    
def testKwArgs(**kwards):
    print("testKwArgs")
    for key, value in kwards.items():
        print("key: {}".format(key))
        print("value: {}".format(value))
        
if __name__ == "__main__":
    testArgs("hello", "how", "are", "you")
    print("--------------------------------")
    testKwArgs(name="darshan", dob="4-8-87")