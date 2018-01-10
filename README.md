# PCA

Метод Главных Компонент (англ. Principal Components Analysis, PCA) — один из основных способов уменьшить размерность данных, потеряв наименьшее количество информации.
Есть матрица F - исходные признаки, хотим получить матрицу G - новые признаки, так чтобы F линейно восстанавливалась по G как можно точнее на исходной выборке F.
U - матрица линейных преобразований

хотим получить: 

![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f1.gif)

решив задачу:

![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f2.gif)

воспользуемся главной теоремой

Теорема:
Если m <= rank F, то
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f2.gif)
достигается когда
    
U - собственные вектора ковариационной матрицы F, соответствующие максимальным m собственным значения L1,L2...Lm, то есть
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f5.gif)
и
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f4.gif)

Для эффективного выбора размерности выборки, воспользуемся правилом (из [лекций Воронцова]( http://www.machinelearning.ru/wiki/images/a/a2/Voron-ML-regression-slides.pdf) ):

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/i1.png)

# Реализуем:

ковариационную матрицу считаем так:

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/i2.png)

для нахождения U, воспользуемся готовым методом в python (сингулярным разложением) **np.linalg.eigh( матр. )**, он нам вернет с.в. и с.з.

**def GetComponents(X, m):** принимает выборку исходную и m - кол-во компонент (размерность), которую нужно получить
данные X передаются нормализованные,  G и U получилм из теоремы
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f5.gif)
и
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f4.gif)

```
def GetComponents(X, m):
    L, U = SingularDecomposition(X)
    G = X.dot(U)
    return G[:,np.arange(m)]
```

также можем **восстановить данные**, по формуле
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f1.gif)

```
def RestoreOriginal(G, X):
    L, U = SingularDecomposition(X)
    n = U.shape[1]
    m = G.shape[1]
    l = G.shape[0]
    zeros = np.zeros((l, n-m))
    G = np.hstack((G,zeros))
    return G.dot(U.T)
```

код в файле **PCAwithRestore.py**

#### Посмотрим как работает программа на Ирисах 

Картинка ниже показывает, **сколько процентов информации мы сохраним**, если выберем 1 компоненту, 2 компоненты, 3 компоненты и так далее:
(нужно вызвать метод **ShowPercentage(X)**, принимает исходную выборку Х)

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/n11.png)

Мы видим, что двух компонент достаточно (мы сохраним 97% инф.), выведем их:
Также выведем собственные значения и ошибку SSE при восстановлении данных для 1й компоненты, для 2х и для 3х

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/n2.png)

**Преимущества метода** в том, что мы понизили размерность выборки, при этом, сохранили 97% информации








