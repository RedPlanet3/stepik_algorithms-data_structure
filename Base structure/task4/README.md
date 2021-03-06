

**Стек с поддержкой максимума**

_Реализовать стек с поддержкой операций_ push, pop и max.

**Вход.** Последовательность запросов push, pop и max .
**Выход.** Для каждого запроса max вывести максимальное число, находящееся на стеке.

Стек — абстрактная структура данных, поддерживающая операции push и pop.

Несложно реализовать стек так, чтобы обе 
эти операции работали за константное время. В данной задаче ваша цель — расширить интерфейс стека так, чтобы он дополнительно поддерживал операцию max и при этом чтобы время работы всех операций по-прежнему было константным.

**Формат входа.** Первая строка содержит число запросов _q_. Каждая из последующих _q_ строк задаёт запрос в одном из следующих форматов: push v, pop, or max.

**Формат выхода.** Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.

**Ограничения.** 1 ≤ _q_ ≤ 400000, 0 ≤ _v_ ≤ 100000.

**Пример.**

Вход:
3 
push 1 
push 7 
pop
Выход:

Выход пуст, потому что нет max запросов.

**Пример.**
Вход:
5 
push 2 
push 1 
max 
pop 
max
Выход:
2
2

**Пример.**

Вход:
6
push 7 
push 1 
push 7 
max 
pop 
max
Выход:
7
7

**Пример.**

Вход:
5 
push 1 
push 2 
max 
pop 
max

Выход:
2
1

**Пример.**

Вход:
10 
push 2 
push 3 
push 9 
push 7 
push 2 
max 
max
max 
pop 
max
Выход:
9
9
9
9



Memory limit: 256 MB
Time limit: 3 seconds
