## trivia-app


El juego de Trivia es un juego de preguntas y respuestas donde los jugadores deben responder preguntas de opción múltiple presentadas en la consola. Cada pregunta contiene exactamente una respuesta correcta entre varias opciones. El juego es simple, pero debe ser implementado de manera que demuestre el manejo efectivo de la lógica básica de programación, estructuras de datos y pruebas unitarias.

#### Reglas y funcionamiento del juego

- **Inicio del juego:**  
  Al lanzar el juego, se muestra un mensaje de bienvenida junto con las instrucciones sobre cómo jugar.
  
- **Número de rondas:**  
  El juego constará de un total de 10 rondas, cada una con una pregunta única.
  
- **Preguntas:**  
  Se presenta una pregunta con cuatro opciones de respuesta numeradas. Solo una opción es correcta.
  
- **Selección de respuesta:**  
  El jugador elige su respuesta ingresando el número correspondiente a la opción elegida.
  
- **Puntuación:**  
  Cada respuesta correcta otorga un punto. No se penaliza por respuestas incorrectas.
  
- **Fin del Juego:**  
  Al finalizar las rondas, se muestra la puntuación total del jugador, junto con un desglose de respuestas correctas e incorrectas.

#### Formato de salida en consola

- **Mensaje de inicio:**  
  ```
  Bienvenido al juego de trivia!
  Responde las siguientes preguntas seleccionando el número de la opción correcta.
  ```

- **Durante el juego:**  
  ```
  Pregunta 1: ¿Cuál es la capital de Francia?
  1) Madrid
  2) Londres
  3) París
  4) Berlín
  Tu respuesta: 3
  ¡Correcto!
  ```

- **Fin del juego:**  
  ```
  Juego terminado. Aquí está tu puntuación:
  Preguntas contestadas: 10
  Respuestas correctas: 8
  Respuestas incorrectas: 2