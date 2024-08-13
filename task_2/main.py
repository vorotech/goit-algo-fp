"""Module for drawing a forked tree using the turtle graphics library."""

import turtle

REDUCE_FACTOR = 0.7


def draw_fork(t, order, trunk_length, branch_length, angle=45):
    """Draws a forked tree using turtle graphics."""
    if order == 0:
        return

    # Малюємо стовп дерева
    t.forward(trunk_length)

    # Підготовка до малювання лівої гілки
    t.left(angle)
    t.forward(branch_length)

    # Рекурсивний виклик для лівої гілки
    draw_fork(t, order - 1, 0, branch_length * REDUCE_FACTOR, angle)

    # Повернення до роздоріжжя між гілками
    t.backward(branch_length)
    t.right(angle * 2)

    # Малювання правої гілки
    t.forward(branch_length)

    # Рекурсивний виклик для правої гілки
    draw_fork(t, order - 1, 0, branch_length * REDUCE_FACTOR, angle)

    # Повернення до бази стовпа
    t.backward(branch_length)
    t.left(angle)

    # Повернення до основи стовпа
    t.backward(trunk_length)


def setup_turtle():
    """Set up the turtle graphics window."""
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.pencolor("brown")

    return t, window


def main():
    """Main function."""
    order = int(input("Вкажіть рівень рекурсії: "))
    trunk_length = 150
    branch_length = trunk_length * REDUCE_FACTOR

    t, window = setup_turtle()
    draw_fork(t, order, trunk_length, branch_length)
    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    main()
