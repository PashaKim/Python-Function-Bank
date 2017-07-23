def bank(a, years, proc, snal, minus):
    for year in range(years):
        a = a*(proc/100)+a
        if snal == year:
            if minus<=a:
                print('На', snal,'году вы получите:', a-minus)
                b = a-minus
                b = b*(proc/100)+b
                return "%.2f" % b
            else:
                print('сори браток, такой суммы на счету нету')
                print('На', snal,'году вы получите:', a)
    return a
    print('Вы получите через ',years,' лет:', "%.2f" % a)
a=int(input('Введите сумму вклада: '))
years=int(input('Введите на сколько лет: '))
proc=int(input('Введите процент: '))
snal=int(input('Укажите на каком году вы хотите снять с счета в банке: '))
minus=int(input('Укажите какую сумму: '))
print(bank(a, years, proc, snal, minus))
