#! /usr/bin/python
# a laconic ping sweeper

import subprocess

nrange = "x.x.x.x" #Change IP

for i in range(1, 10):
    address = nrange + str(i)
    res = subprocess.call(['fping','-a', '-q', address])