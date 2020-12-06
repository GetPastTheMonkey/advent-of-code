from utils import get_input_lines

question_count = 0
questions = set()

for line in get_input_lines(__file__):
    if len(line) > 0:
        for char in line:
            questions.add(char)
    else:
        question_count += len(questions)
        questions = set()

# Last question not counted yet
question_count += len(questions)
print(question_count)
