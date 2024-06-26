#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, mul, div, sub


def main():
    operator_list = ['+', '-', '*', '/']
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in operator_list:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[2] == '+':
                print("{:d} {} {:d} = {:d}". format(int(argv[1]),
                                                    argv[2],
                                                    int(argv[3]),
                                                    add(int(argv[1]),
                                                        int(argv[3]))))
                exit(0)
            elif argv[2] == '-':
                print("{:d} {} {:d} = {:d}". format(int(argv[1]),
                                                    argv[2],
                                                    int(argv[3]),
                                                    sub(int(argv[1]),
                                                        int(argv[3]))))
                exit(0)
            elif argv[2] == '*':
                print("{:d} {} {:d} = {:d}". format(int(argv[1]),
                                                    argv[2],
                                                    int(argv[3]),
                                                    mul(int(argv[1]),
                                                        int(argv[3]))))
                exit(0)
            elif argv[2] == '/':
                print("{:d} {} {:d} = {:d}". format(int(argv[1]),
                                                    argv[2],
                                                    int(argv[3]),
                                                    div(int(argv[1]),
                                                        int(argv[3]))))
                exit(0)


if __name__ == '__main__':
    main()
