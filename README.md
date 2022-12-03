## Proyecto TeoComp 2022 - Grafos
### Enzo Bueno, José Curti, Pablo Haller

## 1. Requerimientos

* Python 3.11.0

### 1.1 Dependencias

Instalar las siguientes dependencias con pip:

```
pip install xmltodict
```

## 2. Como ejecutar el proyecto


Ejecutar el siguiente comando en donde se haya descargado el proyecto.
```
$ py main.py
```

## 3. Funcionalidades


- [x] 3.1. DFS
- [x] 3.2. BFS
- [x] 3.3. Componentes Conexas
- [ ] 3.4. Cantidad de Componentes Conexas
- [ ] 3.5. Es Conexo
- [ ] 3.6. Camino más corto entre dos nodos
- [ ] 3.7. Largo del camino más corto
- [ ] 3.8. Verificar si un camino es el más corto


### 3.1. DFS

Búsqueda en profundidad. Dado un nodo como enttrada, devolver el recorrido realizado por la búsqueda en profundidad 
partiendo de dicho nodo.

### 3.2. BFS

Dado un Nodo como entrada, devolver el recorrido realizado por la búsqueda en amplitud
partiendo de dicho nodo. Si el nodo no existe, retornar la lista vacía.

### 3.3. Componentes Conexas

Dado un grafo, devolver una lista de listas de nodos. Cada sub lista representara una
componente conexa del grafo.

### 3.4. Cantidad de Componentes Conexas

Dado un grafo, retorna la cantidad de componentes conexas que lo componen.

### 3.5. Es conexo

Dado un grafo, se devuelve True si el grafo es conexo. False en cualquier otro caso

### 3.6. Camino más corto entre 2 nodos

Dados dos Nodos, devolver el camino mas corto partiendo del primero y llegando al segundo.
Este camino debe ser representado como una lista de nodos. En caso de que el camino no
exista, se devuelve la lista vacía.

### 3.7. Largo del camino más corto
Dados dos nodos se retorna la distancia entre ellos.

### 3.8. Verificar si un camino es el más corto
Dado una lista de nodos, verificar si el camino representado por ella, es el más corto.

(Pueden existir varios caminos más cortos)

## 4. Entrega
Lunes 5 de diciembre de 2022

- Breve informe detallando los siguientes puntos:
- Motivo de elección de la implementación de grafos realizada, fundamentada sobre
las características solicitadas de los grafos a representar, así como las
funcionalidades requeridas por la tarea.
- Observaciones de implementación de funciones (ej. elección de algoritmos
recursivos sobre iterativos, o viceversa)
- Comentarios que los estudiantes consideren pertinentes.
