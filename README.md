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
    
U - собственные вектора ковариационной матрицы F, соответствующие максимальным m собственным значения L1,L2...Lm
    
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f3.gif)
и
![](https://raw.githubusercontent.com/okiochan/PCA/master/formula/f4.gif)