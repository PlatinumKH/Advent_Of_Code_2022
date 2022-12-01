def part1(inputs):
	maxCalories = 0;
	localCalories = 0;
	for i in inputs:
		if (i == ''):
			if localCalories > maxCalories:
				maxCalories = localCalories
			localCalories = 0
		else:
			localCalories += int(i)
	return maxCalories
	
def part2(inputs):
	calories = [];
	localCalories = 0;
	for i in inputs:
		if (i == ''):
			calories.append(localCalories)
			localCalories = 0
		else:
			localCalories += int(i)
	calories.sort(reverse=True)		
	return calories[0] + calories[1] + calories[2]

f = open("input.txt", "r")
lines = f.readlines()
input = [line.rstrip() for line in lines]
f.close()
print('Part 1: ' + str(part1(input)))
print('Part 2: ' + str(part2(input)))