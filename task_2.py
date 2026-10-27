
import turtle
import math


def draw_square(t, x, y, size, angle, color):
    """Малює квадрат за його нижньою лівою вершиною."""
    t.penup()
    t.goto(x, y)
    t.setheading(math.degrees(angle))
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for _ in range(4):
        t.forward(size)
        t.left(90)

    t.end_fill()


def pythagoras_tree(t, x, y, size, angle, level):
    """Рекурсивно будує дерево Піфагора."""
    if level == 0:
        return

    color = "forestgreen" if level <= 3 else "saddlebrown"
    draw_square(t, x, y, size, angle, color)

    # Верхні кути поточного квадрата
    ux = math.cos(angle)
    uy = math.sin(angle)
    vx = -math.sin(angle)
    vy = math.cos(angle)

    top_left_x = x + size * vx
    top_left_y = y + size * vy

    top_right_x = top_left_x + size * ux
    top_right_y = top_left_y + size * uy

    new_size = size / math.sqrt(2)

    # Лівий дочірній квадрат
    pythagoras_tree(
        t,
        top_left_x,
        top_left_y,
        new_size,
        angle + math.pi / 4,
        level - 1
    )

    # Правий дочірній квадрат
    pythagoras_tree(
        t,
        top_right_x - new_size * math.cos(angle - math.pi / 4),
        top_right_y - new_size * math.sin(angle - math.pi / 4),
        new_size,
        angle - math.pi / 4,
        level - 1
    )


def main():
    try:
        level = int(input("Введіть рівень рекурсії (1-10): "))
    except ValueError:
        print("Помилка: введіть ціле число.")
        return

    if not 1 <= level <= 10:
        print("Рівень має бути від 1 до 10.")
        return

    screen = turtle.Screen()
    screen.title("Фрактал - Дерево Піфагора")
    screen.setup(width=1100, height=850)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pencolor("darkgreen")

    pythagoras_tree(t, -35, -340, 70, 0, level)

    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()
