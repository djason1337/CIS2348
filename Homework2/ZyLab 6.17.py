# Dominic Jason 2203959


password = input()
new_password = ''
i = 0
while i < len(password):
    if password[i] == 'i':
        new_password += '!'
    elif password[i] == 'a':
        new_password += '@'
    elif password[i] == 'm':
        new_password += 'M'
    elif password[i] == 'B':
        new_password += '8'
    elif password[i] == 'o':
        new_password += '.'
    else:
        new_password += password[i]
    i = i + 1

print(f'{new_password}q*s')
