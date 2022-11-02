#reverse tuple
my_tup = ("a", "h", 32, 2.6, None, False)
print(my_tup[::-1])
# slice tuple
my_tuple = (101, [], 10.1, 1.01, 'Love', 'Python', 'Java', 'C++', 'C#', 'SQL', 0, 0.1, (80,))
x = my_tuple[4:-3:5]
print(x)
#ranges
print(list(range(5,15,3)))
print(list(range(-50,-80,-10)))
# ranes and index
r1 = range(10, 100, 10)
print(r1.index(30))
# ranges and slicing
r = range(3, 21)
my_slice = list (r[6:9:])
print(my_slice)

x = "Hello Python"

if x.startswith("H") or len(x) > 12:

	print('/'.join(x[:7]))

elif x[-1] == "n" and len(x.split('o')) >= 3:

    print(x.lower()[4:])

else:

	print((x + ' ') * 3 + "!")