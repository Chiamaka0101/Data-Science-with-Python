import matplotlib.pyplot as plt
import numpy as np

# arr = np.array([1,2,3,4,5]) #1-dimensional

# print(arr)

# arr = np.array((45)) #0-dimensional

# print(arr)

# 2-dimensional array
# arr = np.array([[1,2,3], [4,5,6]])
# # print(arr)
# print(arr[0,1])


# # to access data
#                   #0         #1        #2
#               #  0 1 2    0  1 2    0  1   2 
# arr = np.array([[1,2,3], [4,5,6], [40,30,100]])
# print(arr[2,1]) #access 30
# print(arr[2,2]) #access 100


# 3-D array
# arr = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
# print(arr)
# print(arr.ndim) #to check the number of dimensions


# arr = np.array([1,2,3,4], ndmin=6)
# print(arr)
# print(arr.ndim)


# lst = [10,20,30,40,50]
# print(type (lst))
 
# arr = np.array([10,20,30,40,50])
# print(type(arr))
# print(arr[1])  #behaves like python list
# print(arr.sum())




fruits = np.array(["mango", "apple", "lemon", "orange"])
# print(fruits.dtype)

# arr = np.array([10,20,30,40,50])
# newArr = arr.astype("i")
# print(newArr.dtype)


arr = np.array([[1,2,3], [4,5,6], [40,30,100]])
#to get the shape; no of rows and columns
# print(arr.shape)
# print(arr.size)


# print(arr[0, 0])  #(row 0, col 0)


#probab

# print(np.random.rand(100,3)) 


# Sales of bread, milk, egg in a store for 5days
sales = np.array([
  [50, 30, 20], #day1
  [60, 35, 22], #day2
  [55, 40, 25], #day3
  [70, 45, 30],
  [65, 42, 28]
])

# print("Sales Data: \n", sales)
# print("Total per product:", sales.sum(axis=0)) 
# print("Total per product:", sales.sum(axis=1)) #total sales per day

# print("Total eggs sold: ", sales[::,2].sum())
# print("Total eggs sold: ", sales[::,2].mean())





days = [1,2,3,4,5]
sales = [50,60,55,70,65]

plt.plot(days, sales, marker='o')
plt.title("Sales over 5 days")
plt.xlabel("Day")
plt.ylabel("Unit Sold")
plt.show()

products = ["Bread", "Milk", "Eggs"]
unit_sold = [300,220,180]

plt.bar(products, unit_sold, color=['blue','green','orange'])

plt.title("Sales over 5 days")
plt.xlabel("Day")
plt.ylabel("Unit Sold")
plt.show()












