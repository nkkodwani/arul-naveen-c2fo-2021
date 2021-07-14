class Question:
    def __init__(self, prompt, answer):
        self.prompt == prompt
        self.answer == answer


question_prompts = [
    "what are the color of apples?\n(a) red/green\n(b) purple\n(c) orange\n\n"
    "What are the color of bananas?\n(a) Teal\n(b) Magenta\n(b) Yellow\n\n"
    "what are the color of strawberries?\n(a) Yellow\n(b0 Red\n(c0 Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score = + 1
        print(~f"you got" + str(score) + '/' + str(len(questions)) + 'correct')


question_prompts = [
    "what are the color of apples?\n(a) red/green\n(b) purple\n(c) orange\n\n"
    "What are the color of bananas?\n(a) Teal\n(b) Magenta\n(b) Yellow\n\n"
    "what are the color of strawberries?\n(a) Yellow\n(b0 Red\n(c0 Blue\n\n"
]