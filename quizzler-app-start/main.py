from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters = {
    "amount":10,
    "type":"boolean",
    "category":"18",
}
question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data=response.json()
# print(data["results"])
for question in data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
