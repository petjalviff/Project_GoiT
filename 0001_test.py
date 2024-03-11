
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

# Параметризований декоратор
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

# Виклик декорованої функції
greet("World")
d="Єілдвопаір іволдпідп"


from collections import UserList

class Gdkfj(UserList)