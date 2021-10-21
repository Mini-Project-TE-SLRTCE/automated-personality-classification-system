# importing modules -----------------------------

# to read ".csv" file
import pandas as pd

# to train model
from sklearn import linear_model

#to implement GUI
from tkinter import *

# code to train model ---------------------------

# storing training dataset in variable "dataset"
dataset = pd.read_csv("training-dataset.csv")

# converted "dateset" into "numpy array"
datasetValues = dataset.values

# replacing "Male" with 1
# and "Female" with 0
for i in range(len(datasetValues)):
    if datasetValues[i][0] == "Male":
        datasetValues[i][0] = 1
    else:
        datasetValues[i][0] = 0

# framing modified data into table
# using numpy's DataFrame
df = pd.DataFrame(datasetValues)

# removed "personality" column
mainDF = df[[0,1,2,3,4,5,6]]

# converted "mainDF" into "numpy array"
mainDFValues = mainDF.values

# containes only "personality" column
personality = df[7]

# converted "personality" into "numpy array"
personalityValues = personality.values

# training our model
mul_lr = linear_model.LogisticRegression(multi_class = "multinomial", solver = "newton-cg", max_iter = 1000)
mul_lr.fit(mainDFValues, personalityValues)

# function to check personality -----------------

def checkPersonality(event):
    # getting data
    cp_gender = gender.get()
    cp_age = int(age.get())
    cp_openness = int(openness.get())
    cp_neuroticism = int(neuroticism.get())
    cp_conscientiousness = int(conscientiousness.get())
    cp_agreeableness = int(agreeableness.get())
    cp_extraversion = int(extraversion.get())

    # gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion
    inputDataset = [[cp_gender, cp_age, cp_openness, cp_neuroticism, cp_conscientiousness, cp_agreeableness, cp_extraversion]]

    # type: numpy array
    predictedPersonality = mul_lr.predict(inputDataset)

    # type: list
    predictedPersonality = list(predictedPersonality)

    # type: string
    predictedPersonality = list(predictedPersonality)[0].capitalize()

    # showing personality to user
    personality_displayer.config(state = "normal")
    personality_displayer.delete("1.0", "end")
    personality_displayer.insert(END, predictedPersonality)
    personality_displayer.config(state = "disabled")

# function to reset everything ------------------

def reset(event):
    # resetting gender
    genderMale.select()
    genderFemale.deselect()

    # resetting datas
    age.set(17)
    openness.set(1)
    neuroticism.set(1)
    conscientiousness.set(1)
    agreeableness.set(1)
    extraversion.set(1)

    # hiding personality from user
    personality_displayer.config(state = "normal")
    personality_displayer.delete("1.0", "end")
    personality_displayer.config(state = "disabled")

# gui window ------------------------------------

#creating main window
w = Tk()

#title of main window
w.title("Automatic Personality Prediction System")

#size of main window
w.geometry("830x700")

#background colour of main window
w.configure(background = '#fff')

# heading ---------------------------------------

heading = Label(w, text = "Automatic Personality Prediction System", bg = '#fff', font = ('algerian', 16))
heading.config(pady = 35)
heading.pack()

# choose gender section

label_chooseGender = Label(w, text = "Choose gender:", bg = '#fff', font = ('calibri', 14))
label_chooseGender.pack()
label_chooseGender.place(x = 50, y = 90)

gender = IntVar()

genderMale = Radiobutton(w, text = "Male", variable = gender, value = 1, bg = '#fff', font = ('calibri', 14))
genderFemale = Radiobutton(w, text = "Female", variable = gender, value = 0, bg = '#fff', font = ('calibri', 14))

genderMale.select()
genderFemale.deselect()

genderMale.pack()
genderFemale.pack()

genderMale.place(x = 50, y = 120)
genderFemale.place(x = 130, y = 120)

# code to set age -------------------------------

label_age = Label(w, text = "Age:", bg = '#fff', font = ('calibri', 14))
label_age.pack()
label_age.place(x = 275, y = 90)

age = Scale(w, from_ = 17, to = 28, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 500, bg = '#fff', font = ('calibri', 14))
age.set(17)
age.place(x = 275, y = 120)

# code to set openness --------------------------

label_openness = Label(w, text = "Openness:", bg = '#fff', font = ('calibri', 14))
label_openness.pack()
label_openness.place(x = 50, y = 215)

openness = Scale(w, from_ = 1, to = 8, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 340, bg = '#fff', font = ('calibri', 14))
openness.set(1)
openness.place(x = 50, y = 245)

# code to set neuroticism -----------------------

label_neuroticism = Label(w, text = "Neuroticism:", bg = '#fff', font = ('calibri', 14))
label_neuroticism.pack()
label_neuroticism.place(x = 435, y = 215)

neuroticism = Scale(w, from_ = 1, to = 8, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 340, bg = '#fff', font = ('calibri', 14))
neuroticism.set(1)
neuroticism.place(x = 435, y = 245)

# code to set conscientiousness -----------------

label_conscientiousness = Label(w, text = "Conscientiousness:", bg = '#fff', font = ('calibri', 14))
label_conscientiousness.pack()
label_conscientiousness.place(x = 50, y = 340)

conscientiousness = Scale(w, from_ = 1, to = 8, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 340, bg = '#fff', font = ('calibri', 14))
conscientiousness.set(1)
conscientiousness.place(x = 50, y = 370)

# code to set agreeableness ---------------------

label_agreeableness = Label(w, text = "Agreeableness:", bg = '#fff', font = ('calibri', 14))
label_agreeableness.pack()
label_agreeableness.place(x = 435, y = 340)

agreeableness = Scale(w, from_ = 1, to = 8, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 340, bg = '#fff', font = ('calibri', 14))
agreeableness.set(1)
agreeableness.place(x = 435, y = 370)

# code to set extraversion ----------------------

label_extraversion = Label(w, text = "Extraversion:", bg = '#fff', font = ('calibri', 14))
label_extraversion.pack()
label_extraversion.place(x = 50, y = 465)

extraversion = Scale(w, from_ = 1, to = 8, tickinterval = 1, orient = HORIZONTAL, width = 10, length = 340, bg = '#fff', font = ('calibri', 14))
extraversion.set(1)
extraversion.place(x = 50, y = 495)

# code to display personality -------------------

label_personality = Label(w, text = "Personality:", bg = '#fff', font = ('calibri', 14))
label_personality.pack()
label_personality.place(x = 435, y = 465)

personality_displayer = Text(w, width = '34', height = '3', bg = '#f1f1f1', wrap = WORD, bd = '0', font = ('calibri', 16))
personality_displayer.insert(END, "")
personality_displayer.config(state = "disabled")
personality_displayer.pack()
personality_displayer.place(x = 435, y = 495)

# buttons to perform operations -----------------

button_check_personality = Button(w, text = "Check Personality", width = 16, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)
button_reset = Button(w, text = "Reset", width = 16, height = 2, bg = 'red', fg = '#fff', activebackground = 'darkred', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)

button_check_personality.pack()
button_reset.pack()

button_check_personality.bind('<Button-1>', checkPersonality)
button_reset.bind('<Button-1>', reset)

button_check_personality.place(x = 213, y = 605)
button_reset.place(x = 436, y = 605)

# to display GUI window -------------------------

w.mainloop()