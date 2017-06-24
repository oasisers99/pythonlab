#more on list
cubes = [1,8,27,65,125]
cubes[3] = 4 ** 3
cubes.append(6 ** 3)
print(cubes)

squares = [1,4,9,16,25]
squares.extend(cubes)
print(squares)

squares.insert(5,2)
print(squares)

squares.remove(2) #remove the value, not index
print(squares)

lastNum = squares.pop(len(squares) - 1) #extract the value, removing the value in the list
print(lastNum)

squares.sort()
print(squares)

squares.reverse()
print(squares)


#Stack, last-on, first-out
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)


#Queues, first-in, first-out
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft() #Eric popped out
print(queue)

queue.popleft() #John popped out
print(queue)


#list comprehensions
squares = []
for x in range(10):
	squares.append(x**2)

print(squares)

#equivalent
squares = [x**2 for x in range(10)]
print(squares)


#comb list
combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x, y))

print(combs)

#equivalent
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


#nested list comprehensions
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
]

transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])	#first value of each row
	transposed.append(transposed_row)
print(transposed)

#equivalent
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print(transposed)

#more compressed equivalent
transposed = []
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

#even more compressed equivalent
transposed = []
transposed_list = zip(*matrix)
transposed = list(transposed_list)
print('zipped result; ')
print(transposed)


# remove values from a list based on an index
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0:2]
print(a)