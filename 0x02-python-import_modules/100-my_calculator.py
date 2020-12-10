#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv)
    a = sys.argv
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if a[2] == "+":
            print("{} + {} = {}".format(a[1], a[3], add(int(a[1]), int(a[3]))))
        elif a[2] == "-":
            print("{} - {} = {}".format(a[1], a[3], sub(int(a[1]), int(a[3]))))
        elif a[2] == "*":
            print("{} * {} = {}".format(a[1], a[3], mul(int(a[1]), int(a[3]))))
        elif a[2] == "/":
            print("{} / {} = {}".format(a[1], a[3], div(int(a[1]), int(a[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
