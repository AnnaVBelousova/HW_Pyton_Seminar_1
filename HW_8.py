# Задача 8 Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input())
m = int(input())
k = int(input())
for i in range (n):
    for a in range (m):
        
        if k == a*n or k == i*m:
            answer = f"{n}, {m}, {k} -> yes"
        else: answer = f"{n}, {m}, {k} -> no"
print(answer)
