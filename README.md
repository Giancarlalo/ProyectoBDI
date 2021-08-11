# ProyectoBDI
Proyecto Base de Datos I 0701

## Integrantes:

-Alonso Pinto


-Giancarlo Peralta 20171003045


-Tony Galo 20141004617


-Kattia Gonzales






## Programas Necesarios  **¡Importante!**

Guizero


MySQL Connector

#Hurry Up!!
Giancarlo:
- El sistema debe incluir una ventana splash screen de bienvenida al iniciar el programa.
- El sistema debe incluir una ventana de login. Sólo puede ingresar un usuario registrado en el sistema. Debe existir un usuario administrador previamente registrado en el sistema. Si el usuario administrador se autentica en el juego, éste debe disponer de una pantalla adicional para poder crear, eliminar y editar los datos de autenticación de usuarios (jugadores)
- Una vez autenticado, el sistema debe mostrar una ventana de inicio donde el jugador puede retomar su último juego pausado, o puede iniciar un nuevo juego usando botones para acceder al juego de Flood It o de Destroy the Dots.
- El sistema debe incluir una tabla en pantalla llamada tabla o tablero de score con los 10 mejores tiempos de los juegos exitosos del jugador autenticado, indicando sobre cuál juego (Flood It o Destroy the Dots), con cuál tiempo (formato HH:MM:SS) y sobre cuál fecha (formato YYYY/MM/DD HH:mm:SS) obtuvo dicho resultado. El equipo de desarrolladores decidirá dónde incrustar/llamar/mostrar dicho componente.
- Se deben modificar los juegos de Flood it and Destroy de Dots para que hagan un mejor uso de la pantalla, haciendo más grandes los recuadros y otros elementos.
- Independientemente del tipo de juego, la ventana del juego debe incluir en algún lugar el tiempo de juego que lleva un jugador sobre el juego actual (formato HH:MM:SS). Si el jugador cierra la ventana o pausa/detiene el juego [mediante un botón destinado para ello que debe existir en esta ventana], el sistema debe recordar el tiempo jugado y los datos registrados actuales del juego. A este estado se le llamará juego en espera, juego pausado o juego actual en progreso. Sólo puede haber un juego actual en progreso, por jugador. Cuando el jugador retome el juego pausado, el juego debe mantener el mismo estado de cuando se pausó.
- La ventana del juego (exclusivamente cuando se juega Flood it) debe incluir un botón “Rewind” el cual debe eliminar el último movimiento. Eliminar el último movimiento refiere a una cola de movimientos del jugador, de tal forma que dicho botón remueve el movimiento más reciente y por tanto posee la capacidad de borrar uno a uno los movimientos realizados por el jugador.(pendiente la unión con la base de datos)
- El jugador debe poder tener la opción de finalizar el juego actual como derrota, para iniciar un nuevo juego. Elegir un nuevo juego (eligiendo el mismo o un nuevo Board) deberá requerir confirmación del usuario (mediante una pantalla dialogbox) para marcar como derrota su juego en progreso (si es que existe un juego en espera) antes de iniciar su nuevo juego (Funcionalidad Alonso y Tony).


Kattia:
- La configuración hacia las bases de datos se debe realizar mediante un archivo de texto llamado config.ini 

Lo más díficil
- Independientemente del tipo de juego, la ventana del juego debe incluir en algún lugar el tiempo de juego que lleva un jugador sobre el juego actual (formato HH:MM:SS). Si el jugador cierra la ventana o pausa/detiene el juego [mediante un botón destinado para ello que debe existir en esta ventana], el sistema debe recordar el tiempo jugado y los datos registrados actuales del juego. A este estado se le llamará juego en espera, juego pausado o juego actual en progreso. Sólo puede haber un juego actual en progreso, por jugador. Cuando el jugador retome el juego pausado, el juego debe mantener el mismo estado de cuando se pausó.
- La bitácora deberá guardar todas las acciones del usuario, incluyendo, autenticación, inicio de un juego, acción dentro del juego, fin de un juego, pausa de un juego, visualización de tabla de resultados, y cualquier otra acción bajo el criterio de los programadores, incluyendo a todos los usuarios del sistema.

Tony y Alonso:
- Para evitar el uso de trampa, los datos de la base de datos debe encriptarse. El equipo de desarrolladores debe usar su criterio según todas las lecturas de la clase, y la libertad de investigación, para reconocer cómo y dónde se debe aplicar la encriptación en un sistema de base de datos. La encriptación debe ser manejada mediante SQL.
- Estados del juego (pausa, continuar, etc...)
- Movimientos y rewind
