from typing import List
from db import database
from models import questions_table
class Question:
    """
    Representa una pregunta con sus opciones y respuesta correcta
    """

    def __init__(self, question: str, options: List[str], correct_answer: str) -> None:
        """ Constructor de Question 

        Args:
            question (str): Enunciado de la pregunta
            options (List[str]): Opciones para la pregunta
            correct_answer (str) Respuesta correcta a la pregunta
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer: str) -> bool:
        """
        Verifica si la respuesta a la pregunta es correcta.

        Args:
            answer (str): Respuesta proporcionada por el jugador.
        
        Returns:
            bool
        """
        return self.correct_answer == answer

class Quiz:
    """
    Representa el juego de trivia que contiene múltiples preguntas y controla el flujo del juego.
    """
    
    def __init__(self) -> None:
        """
        Inicializa una instancia de la clase Quiz con estados iniciales.
        """
        self.questions = []
        self.current_question = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question: Question) -> None:
        """
        Agrega una pregunta a la lista del juego.

        Args:
            question (Question): Objeto de tipo Question a agregar.
        """
        self.questions.append(question)
        
    def get_next_question(self) -> Question | None:
        """
        Obtiene la siguiente pregunta del juego.

        Returns:
            Question: La siguiente pregunta, o None si no hay más preguntas.
        """
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.current_question += 1
            return question
        return None
    
    def answer_question(self, question: Question, answer: str) -> bool:
        """
        Verifica la respuesta del jugador y actualiza los contadores de respuestas correctas e incorrectas.

        Args:
            question (Question): La pregunta actual.
            answer (str): La respuesta proporcionada por el jugador.

        Returns:
            bool: True si la respuesta fue correcta, False en caso contrario.
        """
      
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
          
    def show_question_results(self) -> None:
        """
        Muestra el resultado final del juego, total de preguntas respondidas, respuestas correctas e incorrectas del jugador.
        """
        
        print(f"Preguntas contestadas: {self.current_question}")
        print(f"Respuestas correctas: {self.correct_answers}")
        print(f"Respuestas incorrectas: {self.incorrect_answers}")

    def start_quiz(self) -> None:
        """
        Inicia el juego de trivia mostrando las preguntas una a una en consola, solicitando la respuesta del jugador.
        """
        
        try:
            print("Bienvenido al juego de trivia!")
            print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
                    
            while self.current_question < len(self.questions):
                question = self.get_next_question()
                if question:
                    print(f"Pregunta {self.current_question}: {question.question}")
                    for idx, option in enumerate(question.options):
                        print(f"{idx + 1}) {option}")
                    
                    while True:
                        try:
                            answer_to_question = int(input("Tu respuesta: "))
                            if answer_to_question in range(1, 5):
                                break
                            else:
                                print("Ingrese el numero de opción correcta.")
                        except ValueError:
                          print("Entrada inválida. Ingrese el numero de las opciones.")
                    answer = question.options[answer_to_question-1]
                          
                    if self.answer_question(question, answer):
                        print("¡Correcto!")
                    else:
                        print("Incorrecto.")
                else:
                    break

            print("Juego terminado.")
            self.show_question_results()
            
        except KeyboardInterrupt:
            print("\nJuego interrumpido por el usuario. ¡Hasta luego!")

    async def load_questions(self, limit: int = 10) -> None:
        """
        Carga preguntas desde la base de datos

        Args:
            limit (int): Número de preguntas a obtener, por default un maximo de 10.
        """
        await database.connect()

        query = questions_table.select().limit(limit)
        rows = await database.fetch_all(query)

        for row in rows:
            question = Question(
                question=row["question"],
                options=row["options"],
                correct_answer=row["correct_option"]
            )
            self.add_question(question)

        await database.disconnect()