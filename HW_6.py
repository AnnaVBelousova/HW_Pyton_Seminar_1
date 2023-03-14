# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал 
#каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
#чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
S = int (input ())
# S = n + n + 2*(n + n) = 6*n
n = S // 6 
 
answer = f'Петя и Сережа сделали по {n} журавликов, а Катя {2 * 2*n} журавликов'
print(answer)