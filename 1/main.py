i = 1
elves = {}
with open('input.txt') as f:
    line = f.readline()
    foods = []
    calories = 0
    while line:
        line_strip = line.strip()
        if line_strip:
            calory = int(line_strip)
            foods.append(calory)
            calories += calory
        else:
            elves[i] = {
                'foods': foods,
                'calories': calories,
            }
            i += 1
            foods = []
            calories = 0

        line = f.readline()
    
    elves[i] = {
        'foods': foods,
        'calories': calories,
    }

print('=======================================')
print(f'elves = {elves}')

elves_sorted = sorted(elves.items(), key=lambda x: x[1]['calories'], reverse=True)

print('=======================================')
print(f'sorted = {dict(elves_sorted)}')

print('=======================================')
print(elves_sorted[0])

print('=======================================')
print(elves_sorted[0][1]['calories'] + elves_sorted[1][1]['calories'] + elves_sorted[2][1]['calories'])
