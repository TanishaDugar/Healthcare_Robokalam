import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re
from matplotlib import interactive
interactive(True)
color_palette_list2 = ['#464655','#94958b','#a6a6a6','#b7b6c1','#d5cfe1','#eddfef']

df = pd.read_csv('data.csv')

macronutrients = ['Calories', 'Carbohydrate', 'Fat','Protein']
micronutrients = ['Manganese', 'Potassium','Vitamin B6', 'Vitamin C','Vitamin A',
       'Vitamin E', 'Vitamin K', 'Magnesium', 'Copper', 'Iron']

foods = input('Enter Fruits Separated by a space ')
try :
    food_list = foods.split(' ')
    food_list = [x.lower() for x in food_list]
except:
    food_list = [fruit_list]
    
final = df[df['name'].isin(food_list)].sum()



### Macro
labels = macronutrients
percentages = final[macronutrients].values
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#424242'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12
ax.pie(percentages, labels=labels,  
       colors=color_palette_list2, autopct='%1.000f%%', 
       shadow=False, startangle=0,   
       pctdistance=1.2,labeldistance=1.4)
ax.axis('equal')
# ax.set_title("Elephant in the Valley Survey Respondent Make-up")
ax.legend(frameon=False, bbox_to_anchor=(1.5,1.1))
plt.title('Macronutrients',y = -0.3)
plt.savefig('Macro '+ foods+'.png')
plt.plot()



labels = micronutrients
percentages = final[micronutrients].values
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#424242'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12
ax.pie(percentages, labels=labels,  
       colors=color_palette_list2, autopct='%1.000f%%', 
       shadow=False, startangle=0,   
       pctdistance=1.2,labeldistance=1.4)
ax.axis('equal')
# ax.set_title("Elephant in the Valley Survey Respondent Make-up")
ax.legend(frameon=False, bbox_to_anchor=(1.5,1.1))
plt.title('Micronutrients',y = -0.3)
plt.savefig('Micro '+ foods+'.png')
plt.plot()
