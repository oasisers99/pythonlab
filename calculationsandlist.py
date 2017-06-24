
print (2 + 2)
print (17 % 3)
print (5 ** 2)

width = 5
height = 15
print (width * height)

print ('spam eggs')
print ('doesn\'t')

print ('happy new year\nhappy new day!')

print (3 * 'um' + 'hum')

word = 'python'

print(word[0])
print(word[1])
print(word[-3])

print(word[0:3])

print(word[:3])
print(word[3:])

print(word[3:45]) #no out of range error

print('J' + word[1:])

print(len(word))
print(u'hello world!')

print(u'hellp\u0020world ~!')

squares = [1,4,9,16,25]
print(squares)
print(squares[0])

print(squares[:]) #shallow copy - new copy

print(squares + [1,2,3,4,5])

cubes = [1,8,27,65,125]
cubes[3] = 64
print(cubes[3])

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

a, b = 0, 1
while b < 10:
	print(b, end='') # end='' prevents new line
	a, b = b, a + b

i = 256 * 256
print('The value of i is ', i)