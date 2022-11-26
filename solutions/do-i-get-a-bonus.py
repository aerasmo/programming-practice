def bonus_time(salary, bonus):
    salary = salary * 10 if bonus else salary
    return "$" + str(salary)