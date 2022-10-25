"""Sequences - September 29th - Syncronous"""

# An example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

# Printing a tuple produces its literal syntax
print(goat)

# Print both items in the same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences have length``
len(goat)

# Sequences are iterable with for...in loops
# Meaning you can loop over them with for...in
for item in goat:
    print(item)

# Tuples, unlike lists, are imutable
# Which means we cannot reassign items, nor append, not pop, etc
# goat[0] = "LBJ"

# We can "invent" out own type with the type alias
Player = tuple[str, int]

#Once we have aliased a type, we can create variables of that type 
unc_poy: Player = ("Bacot", 5)

# In a strange world where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)

# A rnage is anothoer common sequence type
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

names: list[str] = ["Kris", "Alyssa", "Michael", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")

print(odds_to_99)