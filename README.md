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

для нахождения U, воспользуемся готовым методом в python **np.linalg.eigh( ков. матр. )**, он нам вернет с.в. и с.з.

**def GetComponents(X, m):** принимает выборку исходную и m - кол-во компонент (размерность), которую нужно получить

```
def GetComponents(X, m):

    нормализуем данные
    X = Normalize(X)
    l = X.shape[0]
    n = X.shape[1]
    
    посчитаем ковариационную матрицу
    Xcov = np.dot(X.T,X)/l
    
    L, U = np.linalg.eigh(Xcov)
    
    найдем **эффективную размерность**, 
    точнее - выведем на экран и пользователь сам решит какой процент данных ему нужен
    L /= np.sum(L)
    for i in range(L.size-2,-1,-1):
        L[i] += L[i+1]
    E = L
    print([E[i] for i in range(E.size-1,-1,-1)])
    
    получим искомую матрицу G - размерности m
    G = X.dot(U)
    return G[:,n - 1 - np.arange(m)]
```