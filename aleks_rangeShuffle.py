import random

pairs = []
for i in range(10):
	for j in range(20, 30):
		pairs.append((i, j))

random.shuffle(pairs)

while len(pairs) > 0:
	rand = pairs.pop(0)
	print "{%s, %s}"%(rand[0], rand[1])