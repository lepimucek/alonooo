#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'Welcome to TODO'
todo_list = []
while True:
    task = raw_input('Vnesi task: ')
    opis, avtor, datum_do, narejeno = task.split(';')

