def num(A):

	return (all(numers[i] <= numers[i + 1] for i in range(len(numers) - 1)) or
			all(numers[i] >= numers[i + 1] for i in range(len(numers) - 1)))

# Driver program
numers = [6,5,3,2]
anio = (False: "NE")
ino = (True: 'DA')
print(Monotonic(numers))
