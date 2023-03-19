from survey import AnonymousSurvey

'''定义一个问题并创建一个列表'''
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

'''显示问题并存储答案'''
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_responses(response)

'''显示问卷调查结果'''
print("\nThank  you to everyone who partticioated in the survet!")
my_survey.show_results()