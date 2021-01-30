import sys
def main():
    args=sys.argv
    print("this is args")
    print(type(args))
    print(args)

if __name__ == "__main__":
    main()

# >>> python 02_arglist.py arg1 arg2 haha
# this is args
# <class 'list'>
# ['02_arglist.py', 'arg1', 'arg2', 'haha']
