prompt = """Витязь на распутье
Налево (L) пойдешь, жену найдешь
Направо (R) пойдешь, славу обретешь
Прямо (F) пойдешь, смерть свою сыщешь"""
print(prompt)
choice = input('Куда идем (L, R, F): ')
if choice == 'L' or choice == 'l':
    print('нашел жену')
elif choice == 'R' or choice == 'r':
    print('обрел славу')
elif choice == 'F' or choice == 'f':
    print('сыскал смерть')
else:
    print('Пон')
print('Вот и сказочке конец')

"""
Python console
print("The list of keywords is : ")
print(keyword.kwlist)
The list of keywords is : 
['False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
'try', 'while', 'with', 'yield'] """
