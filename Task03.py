
#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
#номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
#последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
#которая проверяет счастливость билета.
#Примеры: 385916 -> yes 123456 -> no

#Вариант 1:
print("Enter 6-digit's number: ")
n = str(input())

n1 = n[0:3]
n2 = n[3:]

a1 = int(n1[0])
b1 = int(n1[1])
c1 = int(n1[2])
d1 = a1+b1+c1

a2 = int(n2[0])
b2 = int(n2[1])
c2 = int(n2[2])
d2 = a2+b2+c2

if d1 == d2:
    print(f"{n} -> {'yes'}")
else:
    print(f"{n} -> {'no'}")


#Вариант 2:

numb = input("Enter number:     ")
numb2 = (numb[0:3])
numb3 = (numb[3:])

print(numb2, numb3)
sum = (0)
for i in numb2:
    sum = sum + int(i)
print(sum)

sum2 = (0)
for j in numb3:
    sum2 = sum2 + int(j)
print(sum2)

if sum == sum2:
    print("Your ticket is lucky")
else:
    print("Ticket is not lucky")

