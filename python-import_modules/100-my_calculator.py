#!/usr/bin/python3
import sys
from calculator_1 import add, mul, div, sub


def main():
    operator_list = ['+', '-', '*', '/']
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
        exit()
    else:
        if sys.argv[2] not in operator_list:
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")
            exit()
        else:
            if sys.argv[2] == '+':
                print("{:d} {} {:d} = {:d}". format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), add(int(sys.argv[1]), int(sys.argv[3]))))
                print("0")
                exit()
            elif sys.argv[2] == '-':
                print("{:d} {} {:d} = {:d}". format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sub(int(sys.argv[1]), int(sys.argv[3]))))
                print("0")
                exit()
            elif sys.argv[2] == '*':
                print("{:d} {} {:d} = {:d}". format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), mul(int(sys.argv[1]), int(sys.argv[3]))))
                print("0")
                exit()
            elif sys.argv[2] == '/':
                print("{:d} {} {:d} = {:d}". format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), div(int(sys.argv[1]), int(sys.argv[3]))))

if __name__ == '__main__':
    main()

