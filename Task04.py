#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#Примеры:  3 2 4 -> yes 3 2 1 -> no

print("Enter number m:    ")
m = int(input())

print("Enter number n:    ")
n = int(input())

print("Enter number k:    ")
k = int(input())
# при условии, что k < n*m
if ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')

