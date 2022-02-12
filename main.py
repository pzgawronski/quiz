from question_model import Question
from data import question_data

question_bank = []

for datum in question_data:
    input_text = datum["text"]
    input_answer = datum["answer"]
    output_question = Question(input_text, input_answer)
    question_bank.append(output_question)
