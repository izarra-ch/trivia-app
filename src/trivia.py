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

  