import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Mall_Costumers.csv')
print(data.head())

average_income_female = data[data['gender'] == 'Female']['income'].mean()
print(f'Средняя доходность женщин: {average_income_female:.2f}')

average_expenses = data.groupby('gender')['expenses'].mean()
print('Средние расходы по полу:')
print(average_expenses)

more_expensive_gender = average_expenses.idxmax()
print(f'Пол с большими расходами: {more_expensive_gender}, Расходы: {average_expenses.max():.2f}')

men_data = data[data['gender'] == 'Male']

plt.figure(figsize=(10, 6))
plt.scatter(men_data['age'], men_data['income'], color='blue')
plt.title('Зависимость доходов от возраста для мужчин')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.grid(True)
plt.show()

# Создание столбчатого графика
plt.figure(figsize=(12, 8))
expenses_by_income_gender = data.groupby(['income', 'gender'])['expenses'].sum().unstack()
expenses_by_income_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Распределение расходов в зависимости от доходов')
plt.xlabel('Доходы')
plt.ylabel('Суммарные расходы')
plt.legend(title='Пол')
plt.grid(axis='y')
plt.show()
