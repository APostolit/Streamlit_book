import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Вывод текста
'''
# Заголовок страница
Это текст с использованием _markdown_.
'''

# Формирование набора данных
df = pd.DataFrame({'Данные': [1,2,3]})
"Пример вывода таблицы"
df  # Вывод набора данных

# Формирование числового объекта
x = 10
'x=', x  # Вывод строки и значения объекта X

# Формирование графика с библиотекой matplotlib
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

'Пример вывода графика'
fig  # Вывод графика matplotlib