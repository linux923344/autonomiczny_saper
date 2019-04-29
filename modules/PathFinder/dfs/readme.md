Wszystko zaczyna się w GraphCreatorze. Tworząc instancje tej klasy podajesz plansze na której będzie operwać. Tworzy ona na jej podstawie słownik wierchdzołków (klasy Vertex) gdzie gdy podasz jako argument wierchołek słownik "wyppluje" liste obiektów klasy Vertex, które są danego wierchołka nastepnikami w grafie.

Klasa Vertex przechowuje informacje o tym który punnkt na planszy odzwierciedla. To powinnno być również w waszych algorytmach natomiast nastęne dwa pola

```
...
self.visited = False
self.parent = None
...
```

to są informacje potrzebne w trakcie wykonywana algorytmu dfs. Te pola u was mogą się różnić w zależności od implementowanego algorytmu.
Po stworzeniu instancji klasy GraphCreator można wywołać metode tworzącą graf

```
...
graphCreator = GraphCreator(board)
graph = graphCreator.createGraph()
...
```

Zwróci ona nowy obiekt typu Graph zawierający w sobie tę samą listę następników, którą ma GraphFinder.
W tej klasie zaimplementowany jest cały dfs. By go wykonać wystarczy użyć metody dfs:

```
graph.dfs()
```

Po wykonaniu tego algorytmu wierchołki (typu Vertex) przechowują w sobie Informacje o poprzednikach tak by dojść do wierchołka z którego zaczynaliśmy czyli miejsca gdzie stoi saper. Możemy więc wyciągnąć z graphu teraz informacje jak dojść do danego punktu:

```
...
steps = graph.getPathTo(graphCreator.getVertexByCords(x, y))
...
```

graphCreator.getVertexByCords(x, y) zwraca nam wierchołek który odzwierciedla na mapie punkt (x,y). Metoda ta idzie po jego poprzednikach

```
...
vpoint = vpoint.parent
...
```

tak długo, aż dojedziemy do początkowego punktu. Przez cały ten czas wyciąga on kierunki w jakich szedł by tam wrócić i wpisywał do tablicy "path".
Jako, że szliśmy od tyłu to odwracamy tablicę i ją zwracamy

```
...
path.reverse()
return path
...
```
