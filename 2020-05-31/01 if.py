direction = input("Введите направление: ")
speed = 60

if direction == "left" and speed > 0:
    print("<------")
    print("Повернем налево")
elif direction == "right" and speed > 0:
    print("Повернем направо")
elif direction == "back" and speed > 0:
    print("Повернем назад")
else:
    print("Непонятно, куда ехать!!")


if speed >= 0:
    print("... и поехали")
else:
    print("... и остановились")