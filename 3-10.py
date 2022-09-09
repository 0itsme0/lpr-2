
cities = ['vorkuta', 'inta', 'pechora', 'ukhta'] # соЗДАЕМ СПИСОК
print(cities) # ВЫВОДИМ НА ЭКРАН

print(cities[3]) # ВЫВОДИМ КОНКРЕТНОЕ ЗНАЧЕНИЕ ПО ИНДЕКСАЦИИ

message = "Я живу в " + cities[0] + "." # ВЫЧЛЕНЯЕМ ОПРЕДЕЛЕННОЕ ЗНАЧЕНИЕ СПИСКА

cities.append('syktyvkar') # ДОБАВЛЯЕМ К КОНЦУ СПИСКА ГОРОД
print(cities)

cities.remove('vorkuta') # УБИРАЕМ ОПРЕДЕЛЕННОЕ ЗНАЧЕНИЕ
print(cities)

cities.sort() # СОРТИРУЕМ ПО АЛФАФИТНОМУ ПОРЯДКУ
print(cities)

cities.reverse() # ПЕРЕМЕШИВАЕМ СПИСОК
print(cities)

print(len(cities)) # СЧИТАЕМ КОЛИЧЕСТВО ГОРОДОВ
