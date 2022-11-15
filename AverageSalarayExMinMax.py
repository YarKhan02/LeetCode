def avg(salary):
    salary = sorted(salary)

    i = 1
    total = 0
    count = len(salary) - 2

    while i <= len(salary) - 2:
        total += salary[i]
        i += 1

    avg_salary = total//count

    return avg_salary

print(avg([4000, 3000, 1000, 2000]))
