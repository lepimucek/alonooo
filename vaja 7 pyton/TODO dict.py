#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'Welcome to TODO'
todo_dict = {}
while True:
    task = raw_input('vnesi task:')
    status = raw_input('Narejeno? (YES/NO)')
    print 'Your task is: %s' % task

    if status == 'YES':
        todo_dict[task] = True
    else:
        todo_dict[task] = False

    new = raw_input('Dodaj novo? (YES/NO)')
    if new != 'YES':
        break

print'All tasks: {0}' .format(todo_dict)

print "Completed tasks:"
for item in todo_dict:
    if todo_dict[item] is True:
        print "- " + item

print "Incomplete tasks:"
for item in todo_dict:
    if todo_dict[item] is False:
        print "- " + item
print 'END'