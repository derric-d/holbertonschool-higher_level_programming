#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    import calculator_1 as c
    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(av[1])
    b = int(av[3])
    op = av[2]
    if op == "+":
        print("{} + {} = {}".format(a, b, c.add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, c.sub(a, b)))
    elif (op == "*"):
        print("{} * {} = {}".format(a, b, c.mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, c.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
