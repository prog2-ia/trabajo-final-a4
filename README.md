[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# Enunciado del proyecto :

*Aplicación para organizar una liga con modalidades heredadas que definen reglas y puntuaciones específicas. La sobrecarga de operadores facilita combinar clasificaciones, aplicar desempates y comparar el rendimiento de los jugadores de forma directa. Se controlarán excepciones relacionadas con partidas inválidas, resultados contradictorios o inscripciones duplicadas. Además, se mantendrán actas y tablas en formato de texto, junto con una persistencia binaria completa mediante pickle para conservar la información de la competición.*

En este proyecto podremos gestionar un torneo de juegos de mesa simulando una liga, donde se podrán realizar de manera presencial o online.

Dentro del código encontramos 10 clases:

- Persona: clase abstracta de la que heredan clases cómo coach, jugador o equipo

- Coach: clase que hace referencia a los entrenadores de cada equipo. Mantiene cuenta de los juegos a los cuales ha entrenado dentro de los jugadores de su equipo

- Jugador: integrantes de equipo, aquellos que pueden jugar en los torneos y ganar puntos

- Equipo: constituido por jugadores y coach aunque no es obligatorio el último

- Juego: define la estructura de cada juego. Puede registrar la participación y resetearla.

- JuegoCOO: hereda de juego, se utiliza para cuando se trata de juegos con más de un integrante por equipo

- JuegoOnline: Para cuando el juego no se realiza en un entorno físico

- Torneo: clase que define el conjunto de juegos en el cual los jugadores podrán inscribirse

- TorneoOnline: Hereda de juegoCooperativo y JuegoOnline, para los torneos realizados en línea

- Ranking: registro de jugadores y su posición en el podio
