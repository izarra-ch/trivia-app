import asyncio
from trivia import Quiz

async def main():

    quiz = Quiz()
    await quiz.load_questions()
    quiz.start_quiz()

if __name__ == "__main__":
    asyncio.run(main())
