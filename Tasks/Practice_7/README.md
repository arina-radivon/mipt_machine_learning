## Task 1:
Напишите в классе Vector из примера следующие методы:
__neg__ — получение обратного вектора (–v);

__sub__ — вычитание векторов (v1 — v2);

__truediv__ — деление на число (v / a), не забудьте проверить, что второй операнд а — это число, может быть дробным;

__abs__ — вычисление длины с помощью функции abs(v).

## Task 2:
Последовательность Люка — это обобщение последовательности Фибоначчи, определяемая первыми двумя членами и следующим отношением:

U(n) = P*U(n - 1) – Q*U(n - 2),
где P и Q — некоторые постоянные числа.

Ваша задача — написать итератор, который строит по первым двум числам и коэффициентам P и Q первые n чисел последовательности Люка.

## Task 3:
Создайте переменные с именами zero, one, two, three, four, five, six, seven, eight, nine. При этом должен работать код, описанный в примере работы программы.

Программа должна поддерживать следующие действия:

plus — сложение,

minus — вычитание,

times — умножение.

Вы можете реализовывать любые классы и функции, проверяться будет только работоспособность кода, подобного тому, что написано в примере.

Пример работы программы:

five                              ⇒ 5
five.minus.three                  ⇒ 2
two.plus.two                      ⇒ 4
five.plus.two.times.four          ⇒ 28

порядок операций - слева направо, независимо от порядка сложения и умножения
 
nine.times.nine.times.nine        ⇒ 729