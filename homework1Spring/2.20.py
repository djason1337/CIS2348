# Dominic Jason 2203959

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print(f'\nLemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_juice:.2f} cup(s) lemon juice')
print(f'{water:.2f} cup(s) water')
print(f'{agave_nectar:.2f} cup(s) agave nectar')
# Find ratio for servings to ingredients
num_lemon = lemon_juice / servings
num_water = water / servings
num_agave = agave_nectar / servings

serving_num = float(input('\nHow many servings would you like to make?\n'))

real_lemon = num_lemon * serving_num
real_water = num_water * serving_num
real_agave = num_agave * serving_num


print(f'\nLemonade ingredients - yields {serving_num:.2f} servings')
print(f'{real_lemon:.2f} cup(s) lemon juice')
print(f'{real_water:.2f} cup(s) water')
print(f'{real_agave:.2f} cup(s) agave nectar')

# Convert to gallons
gallons_lemon = real_lemon / 16
gallons_water = real_water / 16
gallons_agave = real_agave / 16

print(f'\nLemonade ingredients - yields {serving_num:.2f} servings')
print(f'{gallons_lemon:.2f} gallon(s) lemon juice')
print(f'{gallons_water:.2f} gallon(s) water')
print(f'{gallons_agave:.2f} gallon(s) agave nectar')
