

**Скобки в коде**

_Проверить, правильно ли расставлены скобки в данном коде._

**Вход.** Исходный код программы.

**Выход.** Проверить, верно ли расставлены скобки. Если нет, выдать индекс первой ошибки.

Вы разрабатываете текстовый редактор для программистов и хотите реализовать проверку корректностирасстановкискобок.Вкодемогут встречаться скобки []{}(). Из них скобки [,{ и ( считаются открывающими, а соответствующими им закрывающими скобками являются
],} и ).

В случае, если скобки расставлены неправильно, редактор должен также сообщить пользователю первое место, где обнаружена ошибка. В первую очередь необходимо найти закрывающую скобку, для которой либо нет соответствующей открывающей (например, скобка ] в строке “]()”), либо же она закрывает не соответствующую ей открывающую скобку (пример: “()[}”). Если таких ошибок нет, необходимо найти первую открывающую скобку, для которой нет соответствующей закрывающей (пример: скобка ( в строке “{}([]”).

Помимо скобок, исходный код может содержать символы латинского алфавита, цифры и знаки препинания.

**Формат входа.** Строка _s_[1_...n_], состоящая из заглавных и прописных букв латинского алфавита, цифр, знаков препинания и скобок из множества []{}().

**Формат выхода.** Если скобки в _s_ расставлены правильно, выведите строку “Success". В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для которой нет соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки, для которой нет соответствующей закрывающей.

**Ограничения.** 1 ≤ _n_ ≤ 105.

**Пример 1.**

Вход:

[]

Выход:

Success

**Пример 2.**

Вход:

{}[]

Выход:

Success

**Пример 3.**

Вход:

[()]

Выход:

Success

**Пример 4.**

Вход:

(())

Выход:

Success

**Пример 5.**

Вход:

{[]}()

Выход:

Success

**Пример 6.**

Вход:

{

Выход:


**Пример 7.**

Вход:

{[}

Выход:

3

**Пример 8.** Вход:

foo(bar);

Выход:

Success

**Пример 9.** Вход:

foo(bar[i);

Выход:

10



Memory limit: 512 MB
Time limit: 3 seconds
