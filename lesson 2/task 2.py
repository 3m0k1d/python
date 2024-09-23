summa = int(input())
if summa <= 0:
    print('введена неверная сумма')
if summa > 20:
    print(f'итоговая стоимость составила {summa-(summa/100)*35}, cкидка составила {(summa/100)*35}')
else:
    print(f'итоговая стоимость составила {summa}, cкидка отсуствует')