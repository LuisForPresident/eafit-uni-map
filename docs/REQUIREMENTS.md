Los escribimos con esta estructura:

> El sistema debe
>
> \+ [verbo + objeto | frase verbal]
>
> \+ [complemento de agente | null]
>
> \+ {a) condición-1, b) condición-2, ... condición-n}
>
> Fuente: Diapositivas de la semana 7

## Funcionales

### Entrada

* E1: El sistema debe recibir el punto inicial (ubicación) del usuario.

* E2: El sistema debe recibir el punto final (destino) del usuario.

* E3: El sistema debe permitir al usuario seleccionar el destino (E2) a partir de una lista de destinos favoritos (X1).

* E4: El sistema debe permitir al usuario agregar destinos como favoritos (E3) si existe al menos un lugar que no es favorito.

* E5: El sistema debe permitir al usuario remover destinos como favoritos (E3) si existe al menos un lugar que es favorito.

### Procesamiento

* P1: El sistema debe encontrar la ruta más corta desde el punto inicial (E1) al final (E2).

* P2: El sistema debe calcular los pasos totales del usuario caminando del punto inicial (E1) al final (E2).

* P3: El sistema debe calcular el tiempo de recorrido del usuario caminando del punto inicial (E1) al final (E2).

<!-- 
* P4: El sistema debe calcular el tiempo de recorrido del usuario en bicicleta del punto inicial (E1) al final (E2).

Descartamos este requisito después de la entrega 3.
La profesora dijo que hay obstáculos para ir por el campus en bicicleta,
por lo que el recorrido no podría ser el mismo que caminando.
-->

###  Salida

* S1: El sistema debe mostrar al usuario una lista de indicaciones del camino más corto (P1) desde la ubicación (E1) hasta el destino (E2).

* S2: El sistema debe mostrar la estimación de tiempo de recorrido caminando (P3) desde el punto inicial al final (P1) si está en la pantalla de indicaciones (S1).

<!-- 
* S3: El sistema debe mostrar la estimación de tiempo de recorrido en bicicleta (P4) desde el punto inicial al final (P1) si está en la pantalla de indicaciones (S1).

Descartamos este requisito después de la entrega 3.
Ver explicación de P4.
-->

* S3: El sistema debe mostrar la estimación de pasos caminando (P2) desde el punto inicial al final (P1) si está en la pantalla de indicaciones (S1) y ha calculado la ruta.

* S4: El sistema debe mostrar las estadísticas totales de los pasos (X2) y tiempo (X3) que ha caminado el usuario.


### Persistencia

* X1: El sistema debe guardar los destinos favoritos del usuario (E4).

* X2: El sistema debe guardar los pasos totales que ha caminado el usuario (P2).

* X3: El sistema debe guardar el tiempo total que ha caminado el usuario (P3).


***


## No funcionales

### Entrada

* NE1: El sistema debe permitir editar con facilidad los destinos favoritos.

* NE2: El sistema debe permitir volver a la pantalla de inicio o cerrar el programa si está en la pantalla de indicaciones.

### Procesamiento

* NP1: El sistema debe convertir las unidades con código entendible.

### Salida

* NS1: El sistema debe mostrar esta guía de una manera concisa y fácil de entender. 

### Persistencia

* XN1: El sistema debe almacenar los datos en un formato sencillo.
