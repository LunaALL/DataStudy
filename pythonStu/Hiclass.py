import random


class 학생:
    이름=""
    학번=0
    나이=""
    학년=""

    def __init__(self, name, age, 학년):
        self.이름=name
        self.나이=age
        self.학년=학년


    def set학번(id):
        학번=id


    def allprint(self):
        print("이름 = %s" %self.이름)
        print("학번 =%d" % self.학번)
        print("나이 =%d" % self.나이)
        print("학년 =%d" % self.학년)

