a = [[' ']*3 for i in range(3)]

def game():
    print('  0 1 2')

    for i in range(3):
        row = " ".join(a[i])
        print(f"{i} {row} ")

game()

def ask():
    while True:
        cords = (input("    введите число").split())

        if len(cords) != 2:
            print("введите две координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" введите числа")
            continue

        x, y = int(x), int(y)

        if x > 2 or y > 2:
            print("введите координаты меньше")
            continue

        if a[x][y] != " ":
            print("клетка занята")
            continue
        return x, y

num = 0
while True:
    num += 1
    game()

    if num % 2 == 1:
        print("ходит 0")
    else:
        print("ходит X")

    x, y = ask()
    if num % 2 == 1:
        a[x][y] = 'O'
    else:
        a[x][y] = 'X'

    if num == 9:
        print("у Вас НИЧЬЯ")
        print("Game over")
        break
