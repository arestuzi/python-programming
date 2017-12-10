#!/usr/bin/env python
# coding=utf-8
"""
split and interactively page a string or file of text
"""
import os
def more(text, numlines=15):
    lines = text.splitlines()
    
