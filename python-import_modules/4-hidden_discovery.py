#!/usr/bin/python3
import hidden_4.pyc
names_list = dir(hidden_4.pyc)

for name in names_list:
    if name[0:2] != '__':
        print(name)
