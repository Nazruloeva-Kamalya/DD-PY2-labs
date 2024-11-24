salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Расчитываем подушку безопасности, чтобы протащить 10 месяцев без долгов
money_capital = 0
current_spend = spend
for _ in range(months):
  money_capital += current_spend
  current_spend *= (1 + increase)
money_capital -= (salary * months)

result_money_capital = int(round(money_capital))

print(f"Подушка безопасности, чтобы протащить {months} месяцев без долгов: {result_money_capital}")