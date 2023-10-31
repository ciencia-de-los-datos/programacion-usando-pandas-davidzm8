"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40 

    """
    return len(tbl0)


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    return len(tbl0.columns)


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    return tbl0.groupby("_c1")["_c1"].count()


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return tbl0.groupby("_c1")["_c2"].mean()


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return tbl0.groupby("_c1")["_c2"].max()


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    return [x.upper() for x in sorted(tbl1["_c4"].unique())]


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return tbl0.groupby("_c1")["_c2"].sum()


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0_08=tbl0.copy()
    tbl0_08["suma"]=tbl0_08["_c0"]+tbl0_08["_c2"]

    return tbl0_08


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tbl0_09=tbl0.copy()
    tbl0_09["year"]=tbl0_09["_c3"].str.split("-").str.get(0)

    return tbl0_09


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    newtbl0=tbl0[["_c1"]].drop_duplicates(subset="_c1",ignore_index=True)
    newtbl0=newtbl0.assign(_c2="")
    newtbl0=newtbl0.sort_values(by="_c1",ignore_index=True)
    tblNew=pd.DataFrame()
    lst=[]
    for i in range(0, len(newtbl0)):
        tblNew=tbl0[tbl0["_c1"]==newtbl0.iloc[i]["_c1"]]
        lst=sorted(tblNew["_c2"].tolist())
        c2=":".join(map(str, lst))
        newtbl0.loc[i,"_c2"]=c2

    newtbl0.set_index("_c1", inplace=True)

    return newtbl0


print("Pregunta 10")
print(pregunta_10().equals(pd.DataFrame(
     {
         "_c2": [
             "1:1:2:3:6:7:8:9",
             "1:3:4:5:6:8:9",
             "0:5:6:7:9",
             "1:2:3:5:5:7",
             "1:1:2:3:3:4:5:5:5:6:7:8:8:9",
         ]
     },
     index=pd.Series(["A", "B", "C", "D", "E"], name="_c1"),
 )))
print( pd.DataFrame(
     {
         "_c2": [
             "1:1:2:3:6:7:8:9",
             "1:3:4:5:6:8:9",
             "0:5:6:7:9",
             "1:2:3:5:5:7",
             "1:1:2:3:3:4:5:5:5:6:7:8:8:9",
         ]
     },
     index=pd.Series(["A", "B", "C", "D", "E"], name="_c1"),
 ))



def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    newtbl0=pd.DataFrame(tbl0["_c0"])

    lst=[]
    for i in range(0, len(newtbl0)):
        tblNew=tbl1[tbl1["_c0"]==newtbl0.iloc[i]["_c0"]]
        lst=sorted(tblNew["_c4"].tolist())
        c2=",".join(map(str, lst))
        newtbl0.loc[i,"_c4"]=c2

    return newtbl0


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    newtbl2=tbl2[["_c0"]].drop_duplicates(subset="_c0",ignore_index=True)
    newtbl2=newtbl2.assign(_c5="")

    temtbl2=pd.DataFrame()
    for i in range(0,len(newtbl2)):
          mydic={}
          list5a=[]
          list5b=[]
          temtbl2=tbl2[tbl2["_c0"]==newtbl2.iloc[i]["_c0"]]
          list5a=temtbl2["_c5a"].tolist()
          list5b=temtbl2["_c5b"].tolist()
          mydic={list5a:list5b for (list5a, list5b) in zip(list5a,list5b)}
          mydic=dict(sorted(mydic.items()))
          newtbl2.loc[i,"_c5"]=str(mydic).replace("{","").replace("}","").replace("'", "").replace(" ", "")

    return newtbl2


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    tbl1_2=pd.merge(tbl0, tbl2, on="_c0")

    return tbl1_2.groupby("_c1")["_c5b"].sum()
