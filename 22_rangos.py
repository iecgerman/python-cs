# range(comienzo, fin, pasos)

my_range = range(1,5)
type(my_range)

for i in my_range:
    print(i)


1
2
3
4
my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)
my_range == my_other_range
True
for i in my_range:
    print(i)

0
2
4
6
for i in my_other_range:
    print(i)

0
2
4
6
id(my_range)
139897834758496
id(my_other_range)
139897845009408
my_range is my_other_range
False

for i in range(0, 101, 2):
    print(i)

0
2
4
6
8
10
12
14
16

# Reto:

nones = range(1, 100, 2)

for i in nones:
    print(i)