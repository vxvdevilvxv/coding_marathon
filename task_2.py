'''
Задание: Напишите функцию, которая будет принимать словарь с именем студента и списком его оценок (типа { "name": "John", "notes": [3, 5, 4] }) и возвращать словарь с именем студента и его самой высокой оценкой ({ "name": "John", "top_note": 5 }).

Примечание: входящие данные всегда будут валидны, список никогда не будет пустым.

Примеры:

top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''

def top_note(student):
    return {'name': student['name'], 'top_note': max(student['notes'])}

