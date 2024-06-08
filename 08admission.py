"""Admission to a professional course is subject to the following conditions:
a) Marks in mathematics >=60
b) Marks in physics >=50
c) Marks in chemistry >=40
d) Total in all three subjects >=200

Or
Total in mathematics and physics >=150
Given the marks in three subjects, write a program to process the applications to list eligible candidates."""
mathematics = float(input("Enter your marks in mathematics : "))
physics = float(input("Enter your marks in physics : "))
chemistry = float(input("Enter your marks in chemistry : "))
if mathematics >= 60 and physics >= 50 and chemistry >= 40 and (mathematics + physics + chemistry) >= 200 :
    print("\nYou are admitted to the course.")
elif (mathematics + physics) >= 150 and chemistry >= 40 :
    print("\nYou are admitted to the course.")
else :
    print("\nYou are not admitted to the course.")