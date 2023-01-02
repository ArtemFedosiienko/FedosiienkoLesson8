def mane_function(a, b):
    return a + b, a - b, a * b, a / b, a // b

print (mane_function(3, 4))

def test_function(a, b, c):
    return a + b + c, a * b * c

print (test_function(2, 3, 4))

#Конфлікт виникає, коли в двох гілках було змінено той самий рядок у файлі або коли якийсь файл видалено в одній гілці і відредаговано в іншій.