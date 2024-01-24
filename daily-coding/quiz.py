fragen = [
    {"question": "Wie heißt die Hauptstadt von Namibia?", "answer": "Windhuk"},
    {"question": "Wie lautet die Hauptstadt von Guatemala?", "answer": "Guatemala-Stadt"},
    {"question": "Wie lautet die Hauptstadt von Slowenien?", "answer": "Ljubljana"},
    {"question": "Wie lautet die Hauptstadt von Belize?", "answer": "Belmopan"},
    {"question": "Wie lautet die Hauptstadt von Republik Kongo?", "answer": "Brazzaville"},
]




import random

def run_quiz(fragen):
    score = 0
    random.shuffle(fragen)

    for question_data in fragen:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(f"{question}: ")

        if user_answer.lower() == correct_answer.lower():
            print("Korrekt")
            score += 1

        else:
            print(f"Falsch! Die richtige Antwort ist: {correct_answer}.")

    print(f"\nQuiz beendet! Du hast {score} von {len(fragen)} Fragen richtig beantwortet.") 

run_quiz(fragen)




