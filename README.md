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
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f3.gif)
и
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f4.gif)

Для эффективного выбора размерности выборки, воспользуемся правилом (из [лекций Воронцова]( http://www.machinelearning.ru/wiki/images/a/a2/Voron-ML-regression-slides.pdf) ):

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/i1.png)

# Реализуем:

ковариационную матрицу считаем так:

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/i2.png)

для нахождения U, воспользуемся готовым методом в python (сингулярным разложением) **np.linalg.eigh( ков. матр. )**, он нам вернет с.в. и с.з.

**def GetComponents(X, m):** принимает выборку исходную и m - кол-во компонент (размерность), которую нужно получить
данные X передаются нормализованные, получили G и U из теоремы
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f3.gif)
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


#### Посмотрим как работает программа на Ирисах 

Картинка ниже показывает, сколько процентов информации мы сохраним, если выберем 1 компоненту, 2 компоненты, 3 компоненты и так далее:

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/n11.png)

Мы видим, что двух компонент достаточно, выведем их:

![](https://raw.githubusercontent.com/okiochan/PCA/master/img/n1.png)

**Преимущества метода** в том, что мы понизили размерность выборки, при этом, сохранили 97% информации








