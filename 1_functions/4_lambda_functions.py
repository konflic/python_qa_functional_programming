# Лямбда функция это функция у которой нет имени
lambda_function = lambda x: x ** 2
lambda_function(10)

# Вызов функции без присвоения имени
print((lambda x: x ** 2)(8))

# Применим lambda для сортировки массива
names = ["Генадий Букин", "Тим Эпл", "Аркадий Волож", "Билл Гейтс", "Илон Маск", "Игорь Николаев", "Джеф Безос", "Майк Тайсон"]

# 1. Сортируем по имени
# 2. Сортируем по фамилии
sorted_names = sorted(names)

print(sorted_names)
