print("Hello, world!")
print("Моя перша програма")
print("тут ми познайомимось як праюють рядки")
a=10
b=20
c=b+a**2+b*3
name="Andrii"
Second_name="Petryshyn"
print("тепер виводимо перші значення:")
hello_string=name+" "+Second_name
print(f"<<<<<<<<<<<<<<<Author of the program is {hello_string}.")
name2=input("А як тебе звати: ")
world="Привіт "
h_string=world+" "+name2
print(h_string)
q1=input("Скільки тобі повних років: ")
q1=int(q1)
if q1==None:
  print ("Загальний вік не може дорівнювати 0, чи бути меншим 0")
  q1=int(input("Введи свій актуальний вік: "))
print(f"Я зрозумів, тобі {q1} - це чудовий вік")
q2 = 39 #вік автора програми


#q3=q2>q1 #визначення хто старший
#print(q3)
if q2 > q1:
  print(f"Ти молодший від мене на {q2-q1} років")
  if q2==q1:
     print("Ми однолітки")
else:
  print(f"Ти старший від мене на {int(q1-q2)} років")
for char in name2:
  print(name2)
f=0
while f<=q1:
  print(f"{f} "+name2)
  f=f+1
  if f>=10:
    break
print ("Бувай")