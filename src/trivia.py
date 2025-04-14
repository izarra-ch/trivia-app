from typing import List

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

    def __init__(self):
        self.questions = []
        self.current_question = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question: Question) -> None:
        self.questions.append(question)
        
    def get_next_question(self) -> Question:
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.current_question += 1
            return question
        return None
    
    def answer_question(self, question: Question, answer: str) -> bool:
      
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
          
    def show_question_results(self) -> None:
        print(f"Preguntas contestadas: {self.current_question}")
        print(f"Respuestas correctas: {self.correct_answers}")
        print(f"Respuestas incorrectas: {self.incorrect_answers}")

    def start_quiz(self):
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
        
