# Primera aproximación del algoritmo de filtrado colaborativo
## Información previa
Este motor de recomendación está basado en el algoritmo de los vecinos cercanos. Los datos que se utilizan para la ejecución del mismo se encuentran en los tres ficheros json que aparecen en el proyecto.

En el método main, se realiza una llamada al método obtenerRestaurantesRecomendados, cuyos parámetros se deben  modificar para realizar pruebas:

- El primero de ellos debe ser el atributo "reviewer_id" del docuemnto users_json del usuario del cual queremos obtener la recomendación.
- El segundo debe ser el numero de restaurantes que queremos qe se recomienden

El diagrama de clases de la aplicación es el siguiente:

![image](https://user-images.githubusercontent.com/123477724/219514913-d47c5afe-678b-45d2-9ee7-8fa06351a998.png)
