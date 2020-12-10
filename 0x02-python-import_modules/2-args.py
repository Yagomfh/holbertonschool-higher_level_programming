#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_t = len(sys.argv) - 1
    if argv_t == 0:
        print("{} arguments.".format(argv_t))
    else:
        print("{} argument{}:".format(argv_t, "s" if argv_t > 1 else ""))
        for i in range(argv_t):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
