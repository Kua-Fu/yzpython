import sys

modules = sys.modules

class A(object):

    def __init__(se, a):
        se.a = a

    def get_a(se):

        print(se.a)

if __name__ == "__main__":
    
    print("hello!")
    # print(modules)
    a = A(a='111')
    a.get_a()