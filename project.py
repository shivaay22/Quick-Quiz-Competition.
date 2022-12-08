q1="""Who is going to become the player of the tournament in ICCWC
a.suryakumar Yadav
b.Virat Kohli
c.Sahin Afridi
d.Wanindu Hasranga"""

q2="""Heighest Run scorer in ICCWC 2022
a.Sikandar Raza
b.Kusal Mendis
c.SuryaKumar Yadav
d.None of the Above"""

q3="""Heighest Wicket Taker in T20 WC
a.Blesing Muzerbani 
b.Sam Curran
c.Bas De Lede
d.Wanindu Hasrnga"""

q4="""In which country Icc T20 WC 2022  which Happening
a.India
b.England
c.Australia
d.Sri Lanka
"""
q5="""Currently Who is the Batting coach of india
a.Garry Christan
b.Rahul Dravid
c.Lalchand Rajput
d.Vikram Rathore
"""

questions = {q1:"b",q2:"c",q3:"d",q4:"a",q5:"b"}

name = input("Enter your name: ")
print("hello",name,"Welcome to the quiz world")
score=0
for i in questions:
    print(i)
    flag1=input("Do you want to skip this question (yes/no):")
    if flag1=="yes":
        continue
    ans = input("Enter your answer (a/b/c/d): ")
    if ans==questions[i]:
        print("correct answer,you got 1 point")
        score = score + 1
        print("current score is:",score)
    else:
        print("wrong answer, you lost 1 point")
        score = score - 1
        print("correct score is:",score)
    flag2=input("Do you want to quit (yes/no):")
    if flag2 == "yes":
        break
print("Final score is:", score)







