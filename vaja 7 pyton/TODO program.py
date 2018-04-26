#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __builtin__ import raw_input

from pip._internal.req.req_file import break_args_options

print 'Welcome to our TODO'
todo_list = []

while True:
    task= raw_input('Vnesi task: ')
    print 'Your task is %s' % task
    todo_list.append(task)

    new = raw_input('Dodaj še enega? (YES/NO')
    if new != 'YES':
        break

print 'All tasks: {0}'.format(todo_list)

for task in todo_list:
    print task
print 'END'
