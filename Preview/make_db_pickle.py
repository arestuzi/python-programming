#!/usr/bin/env python
# coding=utf-8
from initdata import db
import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
