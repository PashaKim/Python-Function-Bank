def bank(a, years, proc):
    for year in range(years):
        a = a*(proc/100)+a 
    return "%.2f" % a
a=int(input('Введите сумму вклада: '))
years=int(input('Введите на сколько лет: '))
proc=int(input('Введите процент: '))
print(bank(a, years, proc))
