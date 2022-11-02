# самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    while (x % 5 != 0) :
        x+=1
    return x
    return "I don't know :("

print(closest_mod_5(11))