# Декораторы

def answer(question):
    return 'Думайте сами'

def dialog():
    def answer(question):
        if question.lower().startswith('когда'):
            return 'Никогда'
        else:
            return 'Упс'
    question = input()
    while question != '':
        print(answer(question))
        question = input()

dialog()