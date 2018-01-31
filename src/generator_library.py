import json


class QuestionPaper:

    def __init__(self, subject='Subject Name', code='1234', subject_code='ABCD', date_of_ex='0/0/0', max_marks=100):

        self.subject = subject
        self.code = code
        self.subject_code = subject_code
        self.date_of_ex = date_of_ex
        self.max_marks = max_marks

