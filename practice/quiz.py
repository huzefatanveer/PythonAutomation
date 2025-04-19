import random

from filehandling.generate_quiz.generate_quiz import correctAnswer, wrongAnswers

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



for quizNum in range(35):
    quizFile = open(f'capitalsquiz{quizNum + 1}', 'w')
    answerFile = open(f'capitalsquiz_answers{quizNum + 1}', 'w')

    quizFile.write('Date:\n\nName:\n\nPeriod\n\n')

    quizFile.write(' ' * 20 + 'CapitalsQuiz\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for quizQuestion in range(50):

        correct = capitals[states[quizQuestion]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correct)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOption = wrongAnswers + [correct]
        random.shuffle(answerOption)



        quizFile.write(f'{ quizQuestion +1}. What is the capital of {states[quizQuestion]}\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. {answerOption[i]}")

        quizFile.write('\n')



        answerFile.write(f'{quizQuestion + 1}. {"ABCD"[answerOption.index(correct)]}')
    quizFile.close()
    answerFile.close()











#generate quiz in random order
