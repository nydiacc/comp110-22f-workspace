""""Challenge Question #1 Scopes 09/29/22"""


def f(x: float) -> float:
    x += 1.0
    y: float = x + 2.0
    return x + y


def g() -> None:
    global y
    x: float = f(3.0)
    y = f(x + 4.0)


x: float = 0.0
y: float = 0.0
g()
print(f"{x}, {y}")


"""python -m lessons.challenge_question.cq_sep_29_1"""