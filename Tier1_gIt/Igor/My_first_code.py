
print("ПРИВІТ")
name_user=input("Як тебе звати? ")
print(f"Приємно познайомитися, {name_user}. Мене звати Роббі")
user_old=int(input("Скільки тобі років? "))
r_old=12
print("А мені ",r_old)
if r_old<user_old:
    a=user_old-r_old
    print("Я молодший ніж ти на ",a)
elif r_old>user_old:
    a=r_old-user_old
    print("Я старший ніж ти на ",a)
else: print("Ми з тобою одного віку")