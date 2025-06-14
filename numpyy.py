import numpy as np

arr=np.array([1,4,6,2,8])
print(*arr)
zeroes=np.zeros((2,3))
print(zeroes)
ones=np.ones((2,3))
print(*ones)
random=np.random.rand(3,2)
print(*random)
print(arr.min())
print(arr.max())

#slicing

array=np.array([10,20,30,40,50,60])
print(array[1:4])
print(array[-4:4])
print(array[2:-2])
print(array[-6:-1])

#indexing

matrix=np.array([[1,2,3],[4,5,6]])
print(matrix[0][2])
print(matrix[:,1])
print(matrix[:,2])
print(matrix[1:,2])

#broadcasting

a=np.array([1,2,3,4,5])
b=10
print(a+b)
c=np.array([[1],[2],[3]])
d=np.array([10,20,30])
print(c+d)

#Q1: Normalize an array (scale 0 to 1)

ar=np.array([10, 20, 30, 40, 50])
normalized=(arr-arr.min())/(arr.max()-arr.min())
print(normalized)

#Q2: Filter values greater than mean

a=np.array([10,24,7,25,8,25])
mean_value=a.mean()
print(mean_value)
filtered=a[a>mean_value]
print(filtered)

#Q3: Add a column to a 2D array

data=np.array([[1,2],[3,4],[5,6]])
new = np.array([[10],[20],[30]])
result=np.hstack((data,new))
print(result)