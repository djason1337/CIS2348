# Dominic Jason 2203959

import math

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height
print(f'Wall area: {wall_area} square feet')

# Paint needed
paint = wall_area / 350

print(f'Paint needed: {paint:.2f} gallons')

# Cans needed
cans = paint / 1
cans = math.ceil(cans)

print(f'Cans needed: {cans} can(s)')

# choose color

color = input('\nChoose a color to paint the wall:\n')

color_price = {
    'red': 35,
    'blue': 25,
    'green': 23,
}

if color in color_price:
    print(f'Cost of purchasing {color} paint: ${cans * color_price[color]}')
