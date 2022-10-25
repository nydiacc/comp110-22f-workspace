"""In class example for Eightball"""

from random import randint
question: str = input("What is your yes/no question?")
response: int = randint(0,2)

if response == 0:
    print("Yes, def")
elif response == 1:
    print("Quite possibly")
elif response == 2:
    print("Ask again later.")
else:
     print("Nope.")
