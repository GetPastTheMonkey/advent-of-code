from utils import get_input_lines

question_count = 0
new_group = True
questions = set()

for line in get_input_lines(__file__):
    if len(line) > 0:
        new_questions = set()
        for char in line:
            new_questions.add(char)

        if new_group:
            questions = new_questions
            new_group = False
        else:
            questions = questions.intersection(new_questions)
    else:
        question_count += len(questions)
        questions = set()
        new_group = True

# Last question not counted yet
question_count += len(questions)
print(question_count)
