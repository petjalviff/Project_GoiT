# Створення та виклик функції
c=39 #my age
def hello_en():
    print("Hello world")
    print("What is your name?")
    a=input("Enter your name: ")
    print(f"Hello {a}, how old you?")
    b=int(input("Enter years old: "))
    try:
        if b<c:
            d=c-b
            print(f"I am {d} years older than you, {a}" )
        else:
            if b==c:
                print("We are the same age as you")
            else: d=b-c
            print(f"I am {d} years younger than you, {a}")
    
    except ValueError:
        print("You enterned not Integer!")
        b=int(input("Enter years old: "))
    except IndentationError:
        print("You enterned not Integer!")
        b=int(input("Enter years old: "))
def hello_ua():
    print("****************")
    print("Привіт")
    print("Як тебе звати?")
    a=input("Введи своє імя: ")
    print(f"Привіт, {a}, скільки тобі років?")
    b=int(input("Введи свій вік: "))
    try:
        if b<c:
            d=c-b
            print(f"Я на {d} роки(ів) старший від тебе, {a}" )
        else:
            if b==c:
                print("Ми з тобою одного віку")
            else: d=b-c
            print(f"я на {d} роки(ів) молодший, {a}")
    
    except ValueError:
        print("You enterned not Integer!")
        b=int(input("Enter years old: "))
    except IndentationError:
        print("You enterned not Integer!")
        b=int(input("Enter years old: "))
while True:
    leng=input("Enter lenguage (en for English or ua for Ucrainian): ")
    if leng=="ua":
        hello_ua()
    else: hello_en()
    print("Godbye")
    print("*******************")
