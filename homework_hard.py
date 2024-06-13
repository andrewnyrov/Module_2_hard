'''
🖥️ Задача: "Слишком древний шифр"
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешествинниками находился попирус, где были написаны правила для решения этого "ребуса".
Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно сумме их значений.

Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)

К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движуться на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.
Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.

Что является парой?:
Пары являются уникальными на примере следущего:
7 3 3 5 8
В этой последовательности уникальными парами являются:
Для первой 7: 73 73 75 78
Для второй 3: 33 35 38 (с пеервой 7 у этой 3 уже есть пара, поэтому её не берём).

Все пароли для чисел от 3 до 20 (для сверки):
3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
8 - 13172635
9 - 1218273645
10 - 141923283746
11 - 11029384756
12 - 12131511124210394857
13 - 112211310495867
14 - 1611325212343114105968
15 - 1214114232133124115106978
16 - 1317115262143531341251161079
17 - 11621531441351261171089
18 - 12151811724272163631545414513612711810
19 - 118217316415514613712811910
20 - 13141911923282183731746416515614713812911

Примечания:
Можно использовать как цикл for, так и цикл while
Первое число не входит в одно из чисел пары
Пары чисел подбираются от 1 до 20 для текущего числа.
- - - - - - - - - - - - - - - - - - - - - - - - - - -
Этот алгоритм генерирует пары чисел от 1 до 20 для заданного числа n и проверяет, кратно ли n сумме каждой пары.
Если находит подходящую пару, то формирует и возвращает пароль.

Этот скрипт выводит пароли для всех чисел от 3 до 20, как указано в задании.
Функция generate_password использует два вложенных цикла для перебора всех возможных пар чисел от 1 до n и проверяет, кратно ли n сумме каждой пары.
Если кратно, то числа добавляются в пароль.
После перебора всех пар, функция возвращает сформированный пароль.
'''

def generate_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0: # условие проверки кратности суммы двух чисел
                password += str(i) + str(j)
    return password

# Пример использования функции для чисел от 3 до 20
for n in range(3, 21):
    password = generate_password(n)
    # print(generate_password(n))
    print(f"{n} - {password}")