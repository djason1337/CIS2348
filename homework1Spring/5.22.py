# Dominic Jason 2203959

print(f'Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

service1 = input('\nSelect first service:\n')
service2 = input('Select second service:\n')

cost = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,

}
print('\nDavy\'s auto shop invoice\n')

if service1 in cost:
    print(f'Service 1: {service1}, ${cost[service1]}')
else:
    print('Service 1: No service')

if service2 in cost:
    print(f'Service 2: {service2}, ${cost[service2]}\n')
else:
    print('Service 2: No service')

if service1 in cost and service2 in cost:
    total = cost[service1] + cost[service2]
    print(f'Total: ${total}')

if service1 not in cost:
    print(f'Total: ${cost[service2]}')

if service2 not in cost:
    print(f'\nTotal: ${cost[service1]}')
