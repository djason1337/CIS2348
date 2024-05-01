# Dominic Jason 2203959
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError
    return age

def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError:
        print('Invalid age.\nCould not calculate heart rate info.\n')