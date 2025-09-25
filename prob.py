import numpy as np



#mean/median calculation
purchases = np.array([10,20,30,200,300])

mean_value = purchases.mean()
median_purchases = np.median(purchases)

# print(median_purchases)
# print(mean_value)


income = np.array([500, 600, 700, 800, 1000, 10000, 50000, 200])

mean_income = income.mean() #mean
median_value = np.median(income) #median

print(mean_value)
print(median_value)



employee_salary = np.array([45,50,52,55,60,65,150,200])

average = employee_salary.mean()
middle = np.median(employee_salary)

print (f"The average salary is: {average}\nThe median salary is:, {middle}")