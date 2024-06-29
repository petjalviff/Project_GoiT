import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def snowflake(t, order, size):
    for _ in range(6):
        koch_curve(t, order, size)
        t.right(60)

# Відкрити вікно для малювання
window = turtle.Screen()
window.bgcolor("white")
window.title("Сніжинка Коха")

# Створити об'єкт turtle
snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)  # Максимальна швидкість

# Побудувати сніжинку Коха
snowflake(snowflake_turtle, 3, 50)

# Закрити вікно при кліку
window.mainloop()
