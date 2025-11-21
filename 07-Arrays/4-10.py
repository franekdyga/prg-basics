###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
incorrect_answers = 0
for answer in test_results:
    if answer == True:
      correct_answers += 1
    else:
      incorrect_answers += 1

percentage = round((correct_answers/question_number)*100, 1)

# calculates the number of incorrect answers
...

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print(f'Correct answers: {correct_answers}')
print(f'Incorrect answers: {incorrect_answers}')
print(f'Percentage of correct answers: {percentage}')