from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for datum in question_data:
    input_text = datum["text"]
    input_answer = datum["answer"]
    output_question = Question(input_text, input_answer)
    question_bank.append(output_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your total score is {quiz_brain.user_score}/{quiz_brain.question_number}")