#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'Welcome to TODO'
todo_list = []
while True:
    task = raw_input('Vnesi task: ')
    opis, avtor, datum_do, narejeno = task.split(';')
    if narejeno == 'YES':
        narejeno = True
    else:
        narejeno = False
    dict_task = {
        'opis': opis,
        'avtor':avtor,
        'datum:do': datum_do,
        'narejeno': narejeno
    }
    todo_list.append(dict_task)

    new = raw_input('Dodaj novega? YES/NO')
    if new != 'YES':
        break

for task in todo_list:
    print task

todo_file = open("todo.txt", "w+")  # open the TXT file (or create a new one)


todo_file.write("Completed tasks:\n")  # write into the TXT file
for item in todo_list:
    if item['narejeno'] == True:
               todo_file.write("- {0}\n".format(item))  # add task into the TXT file

todo_file.write("\n")


todo_file.write("Incomplete tasks:\n")  # write into the TXT file
for item in todo_list:
    if item['narejeno'] == False:
                todo_file.write("- {0}\n".format(item))  # add task into the TXT file

todo_file.close()  # close the TXT file
