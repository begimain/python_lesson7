
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
person = {'name': 'Begimai', 'age': 17}
element = { 'Aluminum': 27, 'Ferrum': 56}
person.update(element)
if __name__ == '__main__':
    d = {'dict': 1, 'dictionary': 2}
    # print(d)
    d = dict(short='dict', long='dictionary')
    # print(d)
    d = dict([(1, 1), (2, 4)])
    # print(d)
    # d.clear()  # Метод очищает словарь.
    # print(d)
    d.copy()  # Метод возвращает копию словаря.
    # print(d)
    print(vowels)  # Метод создает новый словарь со значением, предоставленным пользователем.
    print(person.get('name'))  # Метод возвращает значение для указанного ключа , если ключ находится в словаре.
    print(person.get('age'))  # Метод возвращает значение для указанного ключа , если ключ находится в словаре.
    print(person.items())  # Метод возвращает пары ключа и значение.
    print(person.keys())  # Метод возвращает ключи в словаре.
    print(element.pop('Ferrum'))  # Метод удаляет и возвращает элемент из словаря , имеющего заданный ключ.
    print(person.popitem())  # Метод удаляет ключ и возвращает значение.
    print(element.setdefault('Aluminum'))  # Метод возвращает значение ключа.
    print(element.update())  # Метод обновляет словарь с элементами из другого объекта.





    




