import sqlite3
sqliteConnection=sqlite3.connect("Quiz.db")
sqliteConnection.row_factory = lambda cursor, row: row[0]
cursor=sqliteConnection.cursor() 
questions=cursor.execute("SELECT Questions from Project").fetchall()
values=[]
for val in questions:
    values.append(val)
options=cursor.execute("SELECT Options from Project").fetchall()
valueso=[]
for val in options:
    valueso.append(val)
answers=cursor.execute("SELECT Answers from Project").fetchall()
valuesa=[]
for val in answers:
    valuesa.append(val)
cursor.close()
sqliteConnection.close()
'''==============================================='''
import sqlite3
sqliteConnection=sqlite3.connect("Quiz.db")
sqliteConnection.row_factory = lambda cursor, row: row[0]
cursor=sqliteConnection.cursor()
questions=cursor.execute("SELECT Questions from Section2").fetchall()
values2=[]
for val in questions:
    values2.append(val)
options=cursor.execute("SELECT Options from Section2").fetchall()
valueso2=[]
for val in options:
    valueso2.append(val)
answers=cursor.execute("SELECT Answers from Section2").fetchall()
valuesa2=[]
for val in answers:
    valuesa2.append(val)
cursor.close()
sqliteConnection.close()
'''================================================='''
import sqlite3
sqliteConnection=sqlite3.connect("Quiz.db")
sqliteConnection.row_factory = lambda cursor, row: row[0]
cursor=sqliteConnection.cursor()
questions=cursor.execute("SELECT Questions from Section3").fetchall()
values3=[]
for val in questions:
    values3.append(val)
options=cursor.execute("SELECT Options from Section3").fetchall()
valueso3=[]
for val in options:
    valueso3.append(val)
answers=cursor.execute("SELECT Answers from Section3").fetchall()
valuesa3=[]
for val in answers:
    valuesa3.append(val)
cursor.close()
sqliteConnection.close()
'''=================================================='''
class quiz:
    points=0
    total=0
    def __init__(self,name):
        self.name=name
class section1(quiz):
    def __init__(self, name):
        quiz.__init__(self,name)
    def sec1(self):
        print("WELCOME TO SECTION 1 OF THIS QUIZ! YOU WILL BE ASKED FIVE QUESTIONS IN THIS SECTION WITH 4 OPTIONS EACH. SELECT THE CORRECT OPTION.")
        print("-------------------------------")
        print("Your options for the next question are:",valueso[0])
        question1=input(values[0])
        if question1==valuesa[0]:
            quiz.points=quiz.points+1
        else:
            quiz.points=quiz.points+0
        print("-------------------------------")
        print("Your options for the next question are:",valueso[1])    
        question2=input(values[1])
        if question2==valuesa[1]:
            quiz.points=quiz.points+1
        else:
            quiz.points=quiz.points+0
        print("-------------------------------")
        print("Your options for the next question are:",valueso[2])
        question3=input(values[2])
        if question3==valuesa[2]:
            quiz.points=quiz.points+1
        else:
            quiz.points=quiz.points+0
        print("-------------------------------")
        print("Your options for the next question are:",valueso[3])
        question4=input(values[3])
        if question4==valuesa[3]:
            quiz.points=quiz.points+1
        else:
            quiz.points=quiz.points+0
        print("-------------------------------")
        print("Your options for the next question are:",valueso[4])
        question5=input(values[4])
        if question5==valuesa[4]:
            quiz.points=quiz.points+1
        else:
            quiz.points=quiz.points+0
        print("-------------------------------")
class section2(quiz):
    def __init__(self, name):
        quiz.__init__(self,name) 
    def sec2(self):
        print("WELCOME TO SECTION 2 OF THIS QUIZ! YOU WILL BE ASKED FIVE QUESTIONS IN THIS SECTION WITH 4 OPTIONS EACH. SELECT THE CORRECT OPTION.")
        print("-------------------------------")
        print("Your options for the next question are:",valueso2[0])
        question1=input(values2[0])
        if question1==valuesa2[0]:
            quiz.points=quiz.points+3
        else:
            quiz.points=quiz.points-1
        print("-------------------------------")
        print("Your options for the next question are:",valueso2[1])    
        question2=input(values2[1])
        if question2==valuesa2[1]:
            quiz.points=quiz.points+3
        else:
            quiz.points=quiz.points-1
        print("-------------------------------")
        print("Your options for the next question are:",valueso2[2])
        question3=input(values2[2])
        if question3==valuesa2[2]:
            quiz.points=quiz.points+3
        else:
            quiz.points=quiz.points-1
        print("-------------------------------")
        print("Your options for the next question are:",valueso2[3])
        question4=input(values2[3])
        if question4==valuesa2[3]:
            quiz.points=quiz.points+3
        else:
            quiz.points=quiz.points-1
        print("-------------------------------")
        print("Your options for the next question are:",valueso2[4])
        question5=input(values2[4])
        if question5==valuesa2[4]:
            quiz.points=quiz.points+3
        else:
            quiz.points=quiz.points-1
        print("-------------------------------")
class section3(quiz):
    def __init__(self, name):
        quiz.__init__(self,name)
    def sec3(self):
        print("WELCOME TO SECTION 3 OF THIS QUIZ! YOU WILL BE ASKED FIVE QUESTIONS IN THIS SECTION WITH 4 OPTIONS EACH. SELECT THE CORRECT OPTION.")
        print("-------------------------------")
        print("Your options for the next question are:",valueso3[0])
        question1=input(values3[0])
        if question1==valuesa3[0]:
            quiz.points=quiz.points+5
        else:
            quiz.points=quiz.points-2
        print("-------------------------------")
        print("Your options for the next question are:",valueso3[1])    
        question2=input(values3[1])
        if question2==valuesa3[1]:
            quiz.points=quiz.points+5
        else:
            quiz.points=quiz.points-2
        print("-------------------------------")
        print("Your options for the next question are:",valueso3[2])
        question3=input(values3[2])
        if question3==valuesa3[2]:
            quiz.points=quiz.points+5
        else:
            quiz.points=quiz.points-2
        print("-------------------------------")
        print("Your options for the next question are:",valueso3[3])
        question4=input(values3[3])
        if question4==valuesa3[3]:
            quiz.points=quiz.points+5
        else:
            quiz.points=quiz.points-2
        print("-------------------------------")
        print("Your options for the next question are:",valueso3[4])
        question5=input(values3[4])
        if question5==valuesa3[4]:
            quiz.points=quiz.points+5
        else:
            quiz.points=quiz.points-2
        print("-------------------------------")
        quiz.total=quiz.total+quiz.points
        print("Your total score:",quiz.total)
        if quiz.total>=40 or quiz.total<=45:
            print("EXCELLENT! Well done!")
        elif quiz.total>=30 or quiz.total<=39:
            print("GOOD")
        elif quiz.total>=20 or quiz.total<=29:
            print("AVERAGE")
        elif quiz.total>=0 or quiz.total<=19:
            print("CAN DO BETTER") 
