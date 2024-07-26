import numpy as np
# a = np.array([1,2,3])
# b = np.array([[1,2,3],[4,5,6]])
#
# #BASIC OPERATIONS
# sum_a = np.sum(a)
# mean_b = np.mean(b)
#
# #array operations
# c = a+5
# d = b*2
#
# print("Array a:",a)
# print("sum of array_a", sum_a)
# print("Array b:",b)
# print("mean of array_b",mean_b)
# print("array a+5:",c)
# print("array b",d)
#
# '''np.zeros((m,n))create an m*n array filled with zerores
# np.ones((m,n))create an m*n array filled with ones
# np.full((m,n), value) create an m*n array filled with a range of values
# np.eye(n) create an n*n identity matrix
# np.arrange(start,stop,step) create an array with a range of values
# np.linspace(start,stop,num) create an array with a specified number of evenly spaced values
# between start and stop'''
#
# m,n = 3,4
# a = np.zeros((m,n))
# print(a)
#
# b = np.ones((m,n))
# print(b)
#
#
# value = 10
# c = np.full((m,n),value)
# print(c)
#
# n = 2
# d = np.eye(n)
# print(d)
#
# start,stop,step = 0,8,2
# e = np.arange(start,stop,step)
# print(e)
#
# start,stop,step = 1,9,6
# f = np.linspace(start,stop,step)
# print(f)
#
# #INDEXING AND SLICING
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
#
# #aaccessing element
# element = arr[1,2]
# #slicing
# subarray = arr[:2, 1:3] # (:2 is for rows index and 1:3 is for element)
# print("element at [1,2]",element)
# print("subarray:\n",subarray)
#
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# sum_arr = arr1+arr2
# product = arr1 * arr2
#
# print("sum of array",sum_arr)
# print("product of array",product)
#
# matrix1 = np.array([[1,2],[3,4]])  #1*5 + 2*7
# matrix2 = np.array([[5,6],[7,8]])
# matrix_product = np.dot(matrix1,matrix2)
# '''1*5 + 2*7 = 19
#    1*6  + 2*8 = 22  [19 , 22]
#    3*5  + 4*7 = 43  [43 , 50]
#    3*6  + 4*8 = 50'''
#
# print("matrix product",matrix_product)
#
# #USEFUL FUNCTIONS
#
# array1 = ([1,2,3])
#
# a = np.max(array1)
# print(a)
#
# a = np.min(array1)
# print(a)
#
# a = np.sum(array1)
# print(a)
#
# a = np.mean(array1)
# print(a)
#
# a = np.std(array1)
# print(a)
#
# a = np.var(array1)
# print(a)

x = [2,4,4,4,5,5,7,9]
mean_array = np.mean(x)
print(mean_array)

standard_deviation_array = np.std(x)
print(standard_deviation_array)

#CREATING ARRAYS FROM PYTHON LISTS
list1 = [1,2,3,4,5]
array1 = np.array(list1)

list2 = [[1,2,3],[4,5,6]]
array2 = np.array(list2)

print(array1)
print(array2)

#CREATING ARRAYS BETWEEN 0 AND 1
random_array = np.random.rand(3,3)
print(random_array)

random_int_array = np.random.randint(0, 10, (3,3))
print(random_int_array)

#NORMAL DISTRIBUTION
normal_array = np.random.randn(3,3)
print(normal_array)

# '''METHODS
# max
# min
# reshape
# Argmax
# Argmin
#
# #ATTRIBUTES
#
# shape
# size
# Dtype
# num of dimensions(ndmin)'''

arr = np.array([[5,12,7],[3,8,9]])
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr.ndim)

#RESHAPING THE ARRAY
reshaped_array = arr.reshape((3,2))
print(reshaped_array)

#MAXIMUM VALUE
max_value = arr.max()
print(max_value)

#MINIMUM VALUE
min_value = arr.min()
print(min_value)

#index of maximum value
max_index = arr.argmax()
print(max_index)

#index of minimum value
min_index = arr.argmin()
print(min_index)


#copy array

arr = np.array([1,2,3])
arr_copy= arr.copy()

print(arr_copy)


#appending

arr= [3,4,2]
append_array = np.append(arr, [4,5])
print(append_array)

#INSERTING
arr =[1,2,3]
int_array = np.insert(arr,1,[10,11]) #insert [10,11] at index 1
print(int_array)

#sort
arr=[3,2,1]
sort_array = np.sort(arr)
print(sort_array)

#remove

arr =np.array[1,2,3,4,5,6]
delet_arr= np.delete(arr,[1,3]) # delete element index 1,3
print(delet_arr)

#concatinate

arr1=[1,2,3]
arr2=[4,5,6]
combined_arr=np.concatenate((arr1,arr2))
print(combined_arr)


 #vertical stack
arr1=[1,2,3]
arr2=[4,5,6]
vstack_arr= np.vstack((arr1,arr2))
print(vstack_arr)

 #horizontal
arr1=[1,2,3]
arr2=[4,5,6]
hstack_arr= np.hstack((arr1,arr2))
print(hstack_arr)

#splitting array
#split array in multiple array using:

#np.split,np.vsplit(vertical)
#np.split,np.hsplit(horizontal)

arr = np.array([1,2,3,4,5,6])
 #split 3 arrays
split_arr = np.split(arr,3)
print(split_arr)

#vertical split
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
vsplit_arr=np.vsplit(arr2,3)
print(vsplit_arr)

 #horizontal split
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
hsplit_arr=np.hsplit(arr3,3)
print(hsplit_arr)
