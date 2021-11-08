#import pandas library
import pandas as pd
import numpy as np

#define file to be read from.
df = pd.read_csv('input.csv')

#remove spaces in columns.
df.columns = df.columns.str.replace(' ', '')

#variable to hold passing/failing grades
passing_grades = {(80, 100): 'A',
              (70, 79.9): 'B',
              (60, 69.9): 'C',
              (50, 59.9): 'D',
              (40, 49.9): 'E',
              (0, 39.9): 'U'}
#iterate function
def grade_calc(x, b):
    return next((v for k, v in b.items() if k[0] <= x <= k[1]), None)

df['Final_Mark'] = df['Algebra'] + df['Calculus'] + df['Programming'] + df['Databases']

#Get the average by dividing by 4.
df['Average_Mark'] = df['Final_Mark'] / 4



#Check if conditions to passing grade variable to dertemine correct passing/failing grade.
df['Final_Grade'] = df['Average_Mark'].apply(grade_calc, b=passing_grades)



#Print the specific columns to output csv file.
header = ["Firstname", "Surname", "Average_Mark", "Final_Grade"]

#Output to be written to csv file.
df.to_csv('output.csv', columns = header)
