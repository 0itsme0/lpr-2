spisok = ['name1', 'Petya', 'Gg'] # Создаем переменную со списком гостей 
spisok.insert(0, 'Natasha') # С помощью метода insert добавляем Наташу в начало списка
spisok.insert(1, 'Olya') # С помощью метода insert добавляем Олю в середину списка
spisok.append('Anton') # С помощью метода append добавляем Антона в конец списка
message_0 = 'К сожалению, ко мне могут придти только два гостя' # Сообщаем о том, что может придти только два гостя
print(message_0) # Выводим это сообщение на экран
not_going = spisok.pop(0) # Задаем переменную с методом pop() удаляя значение из контекста, но не из списка
not_going1 = spisok.pop(1) # Задаем переменную с методом pop() удаляя значение из контекста, но не из списка
not_going2 = spisok.pop(2) # Задаем переменную с методом pop() удаляя значение из контекста, но не из списка
not_going3 = spisok.pop(2) # Задаем переменную с методом pop() удаляя значение из контекста, но не из списка 
message = 'Не приходи, ' +  not_going # Cоздаем переменную с информацией, что гость не должен приходить
message1 = 'Не приходи, ' +  not_going1 # Создаем переменную с информацией, что гость не должен приходить
message2 = 'Не приходи, ' +  not_going2 # Создаем переменную с информацией, что гость не должен приходить
message3 = 'Не приходи, ' +  not_going3 # Создаем переменную с информацией, что гость не должен приходить
print(message)  # Выводим эту информацию
print(message1) # Выводим эту информацию
print(message2) # Выводим эту информацию
print(message3) # Выводим эту информацию
print(spisok) # Выводим эту информацию
