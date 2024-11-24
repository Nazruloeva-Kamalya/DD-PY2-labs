money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 1
current_money = money_capital

while current_money >= spend:
  current_money -= spend
  spend *= (1 + increase)
  current_money += salary
  months += 1

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
