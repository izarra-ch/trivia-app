from trivia import Question, Quiz

if __name__ == "__main__":
    question_bank = [
        Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], "París"),
        Question("¿En qué país se encuentra la Torre Eiffel?", ["Italia", "Francia", "España", "Alemania"], "Francia"),
        Question("¿Quién escribió 'Cien años de soledad'?", ["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Pablo Neruda"], "Gabriel García Márquez"),
        Question("¿Cuál es el resultado de 7 x 8?", ["54", "56", "64", "58"], "56"),
        Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "Pacífico"),
        Question("¿Cuál es el idioma más hablado en el mundo?", ["Español", "Inglés", "Chino mandarín", "Hindi"], "Inglés"),
        Question("¿Qué parte del cuerpo bombea la sangre?", ["Pulmones", "Riñón", "Hígado", "Corazón"], 4),
    ]
    
    quiz = Quiz()
    
    for question in question_bank:
        quiz.add_question(question)
    
    quiz.start_quiz()
