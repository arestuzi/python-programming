#!/usr/bin/env python
# coding=utf-8
"""
split and interactively page a string or file of text
"""
def more(text, numlines=15):
    lines = text.splitlines()
    print(lines)
    print("DEBUG: length of lines: " + str(len(lines)))
    chunk = lines[:numlines]
    print("DEBUG: content of chunk: ")
    print(chunk)
    print("DEBUG: length of chunk: ")
    print(len(chunk))
    lines = lines[numlines:]
    print("DEBUG: content of chunk: ")
    print(lines)
    print("DEBUG: length of lines: ")
    print(len(lines))

if __name__ =='__main__':
    import sys
    more(open(sys.argv[1]).read(), 10)



    
