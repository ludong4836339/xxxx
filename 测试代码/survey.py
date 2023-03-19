class AnonymousSurvey:
    '''收集匿名调查问卷的答案'''
    def __int__(self,question):
        '''存储一个问题，并未存储答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_responses(self,new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        '''显示手机到的所有答案'''
        print("Survey results")
        for response in self.responses:
            print(f"- {response}")