import os
import sys
import pandas as pd
from matplotlib import pyplot, pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import linear_model, metrics, model_selection, svm
import seaborn as sns
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

df = pd.read_csv('anemiaPredictionDataset.csv')
print(df.to_string())
# plt.figure()
# df.hist()
# scatter_matrix(df)
# sns.scatterplot(df)
# plt.show()
# df.plot()
# pyplot.show()

log_regress_model = linear_model.LogisticRegression(max_iter=3000)
# svm_model = svm.SVC(max_iter=3000)
y = df.values[:, 11]
X = df.values[:, 0:11]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

print(X)
print(y)

log_regress_model.fit(X_train, y_train)
# svm_model.fit(X_train, y_train)

print(log_regress_model.predict([[28, 0, 0, 34, 60, 17, 28, 20, 11, 0, 14]]))

y_predict_log = log_regress_model.predict(X_test)
print(metrics.accuracy_score(y_test, y_predict_log))

# metrics.confusion_matrix(log_regress_model,X_test,y_test)

# y_predict_svm = svm_model.predict(X_test)
# print(metrics.accuracy_score(y_test, y_predict_svm))


def exit_program():
    response = messagebox.askokcancel("Confirm Exit", "You sure you want to exit program?")
    if response:
        sys.exit(0)


def clicked_detect():
    try:
        age = float(age_entry.get())
        sex = float(sex_entry.get())
        rbc = float(rbc_entry.get())
        pcv = float(pcv_entry.get())
        mcv = float(mcv_entry.get())
        mch = float(mch_entry.get())
        mchc = float(mchc_entry.get())
        rdw = float(rdw_entry.get())
        tlc = float(tlc_entry.get())
        plt = float(plt_entry.get())
        hgb = float(hgb_entry.get())

        if sex == 0 or sex == 1:
            print(log_regress_model.predict([[age, sex, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt, hgb]]))
            result = log_regress_model.predict([[age, sex, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt, hgb]])

            if result != 0:
                result_label.configure(text="Result: You are Anemic!Consult Doctor")
            else:
                result_label.configure(text="Result: Your are NOT ANEMIC")
        else:
            messagebox.showerror("Input Error", "Please enter 0 or 1 in the SEX field")
    except Exception as e:
        print(e)
        (messagebox.showerror("Input Error", "Please enter all values"))


window = Tk()
window.title("Anemia Detection")
window.minsize(width=700, height=800)
window.config(padx=50, pady=50, bg="#001427")

title_label = Label(text="ANEMIA DETECTION", width=40, font=("Monaco", 20, "bold", "underline"),
                    fg="#F4D58D", bg="#001427", anchor=CENTER)
title_label.grid(column=1, columnspan=2, row=2, pady=(20, 20), padx=(0, 10))

lab_label = Label(text="Please enter values below:", width=56, font=("Monaco", 12, "bold"), fg="#F4D58D",
                  bg="#001427")
lab_label.grid(column=1, row=3, columnspan=2, sticky=W)

age_label = Label(text="AGE", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
age_label.grid(column=1, row=4, pady=(10, 0), padx=(0, 0), sticky=E)
age_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
age_entry.grid(column=2, row=4, pady=(20, 0), padx=(0, 10), sticky=W)

sex_label = Label(text="SEX (0==Male, 1==Female)", width=30, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
sex_label.grid(column=1, row=5, pady=(10, 0), padx=(0, 0), sticky=E)
sex_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
sex_entry.grid(column=2, row=5, pady=(10, 0), padx=(0, 10), sticky=W)

rbc_label = Label(text="RBC", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
rbc_label.grid(column=1, row=6, pady=(10, 0), padx=(0, 0), sticky=E)
rbc_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
rbc_entry.grid(column=2, row=6, pady=(10, 0), padx=(0, 10), sticky=W)

pcv_label = Label(text="PCV", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
pcv_label.grid(column=1, row=7, pady=(10, 0), padx=(0, 0), sticky=E)
pcv_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
pcv_entry.grid(column=2, row=7, pady=(10, 0), padx=(0, 10), sticky=W)

mcv_label = Label(text="MCV", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
mcv_label.grid(column=1, row=8, pady=(10, 0), padx=(0, 0), sticky=E)
mcv_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
mcv_entry.grid(column=2, row=8, pady=(10, 0), padx=(0, 10), sticky=W)

mch_label = Label(text="MCH", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
mch_label.grid(column=1, row=9, pady=(10, 0), padx=(0, 0), sticky=E)
mch_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
mch_entry.grid(column=2, row=9, pady=(10, 0), padx=(0, 10), sticky=W)

mchc_label = Label(text="MCHC", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
mchc_label.grid(column=1, row=10, pady=(10, 0), padx=(0, 0), sticky=E)
mchc_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
mchc_entry.grid(column=2, row=10, pady=(10, 0), padx=(0, 10), sticky=W)

rdw_label = Label(text="RDW", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
rdw_label.grid(column=1, row=11, pady=(10, 0), padx=(0, 0), sticky=E)
rdw_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
rdw_entry.grid(column=2, row=11, pady=(10, 0), padx=(0, 10), sticky=W)

tlc_label = Label(text="TLC", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
tlc_label.grid(column=1, row=12, pady=(10, 0), padx=(0, 0), sticky=E)
tlc_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
tlc_entry.grid(column=2, row=12, pady=(10, 0), padx=(0, 10), sticky=W)

plt_label = Label(text="PLT/mm3", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
plt_label.grid(column=1, row=13, pady=(10, 0), padx=(0, 0), sticky=E)
plt_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
plt_entry.grid(column=2, row=13, pady=(10, 0), padx=(0, 10), sticky=W)

hgb_label = Label(text="HGB", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
hgb_label.grid(column=1, row=14, pady=(10, 0), padx=(0, 0), sticky=E)
hgb_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
hgb_entry.grid(column=2, row=14, pady=(10, 0), padx=(0, 10), sticky=W)

ttk.Style().configure('main.TButton', font=("Monaco", 12, "bold"), foreground="#F4D58D", background="#001427",
                      activebackground="#001427", activeforeground="#690500",
                      highlightbackground="#001427", highlightforeground="#934B00")

predict_enter_button = ttk.Button(width=17, text="Detect", command=clicked_detect, style='main.TButton')
predict_enter_button.grid(column=1, row=15, columnspan=2, pady=(20, 0))
predict_enter_button = Entry( fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")




result_label = Label(text="", width=60, font=("Monaco", 14, "bold"), fg="#F4D58D", bg="#001427")
result_label.grid(column=1, row=17, columnspan=2, pady=(20, 10))

exit_button = ttk.Button(width=17, text="Exit Program", command=exit_program, style='main.TButton')
exit_button.grid(column=1, row=19, columnspan=2, pady=(40, 0))

window.mainloop()

