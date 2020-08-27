from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Теннис")
window.geometry("430x110")
window.resizable(False, False)
Betnumber1 = DoubleVar()


var1x1 = IntVar(window)
var2x1 = IntVar(window)
var1x2 = IntVar(window)
var2x2 = IntVar(window)
var1x3 = IntVar(window)
var2x3 = IntVar(window)
option1 = OptionMenu(window, var1x1,"0", "1", "2", "3", "4", "5", "6", "7")
option2 = OptionMenu(window, var2x1,"0", "1", "2", "3", "4", "5", "6", "7")
option3 = OptionMenu(window, var1x2,"0", "1", "2", "3", "4", "5", "6", "7")
option4 = OptionMenu(window, var2x2,"0", "1", "2", "3", "4", "5", "6", "7")
option5 = OptionMenu(window, var1x3,"0", "1", "2", "3", "4", "5", "6", "7")
option6 = OptionMenu(window, var2x3,"0", "1", "2", "3", "4", "5", "6", "7")
Var_OU = StringVar()
Var_P1P2 = StringVar()
choiceMenuUO = OptionMenu(window, Var_OU, "Меньше", "Больше")
choiceMenuP1P2 = OptionMenu(window, Var_P1P2, "1 Игрок", "2 Игрок")



def Hfullset(x1,x2,x3,x4,x5,x6,Betnumber1,Var_P1P2 ):
    list = (5, 6, 7)
    if var1x2.get() in list or var2x2.get in list:
        p1maxotrqv = MaxadvHfulllastset(x1,x2,x3,x4,x5,x6)
        p2maxotrqv = MaxadvHfulllastset(x1,x2,x3,x4,x6,x5)
        if Var_P1P2 == "1 Игрок":
            F1betcalculator(Betnumber1, p1maxotrqv, p2maxotrqv)
        else:
            F1betcalculator(Betnumber1, p2maxotrqv, p1maxotrqv)

    elif var1x1.get() in list or var2x1.get() in list:
        p1maxotrqv = maxadvantages2setfor1p(x1,x2,x3,x4,x5,x6)
        p2maxotrqv = maxadvantages2setfor2p(x1,x2,x3,x4,x5,x6)
        if Var_P1P2 == "1 Игрок":
            F1betcalculator(Betnumber1, p1maxotrqv, p2maxotrqv)
        else:
            F1betcalculator(Betnumber1, p2maxotrqv, p1maxotrqv)

    else:
        p1maxotrqv = maxadvantagefor1p(x1,x2)
        p2maxotrqv = maxadvantagefor2p(x1,x2)
        if Var_P1P2 == "1 Игрок":
            F1betcalculator(Betnumber1, p1maxotrqv, p2maxotrqv)
        else:
            F1betcalculator(Betnumber1, p2maxotrqv, p1maxotrqv)

def maxadvantagefor2p(x1,x2):
  if x1 >=5: x2=7
  else: x2 =6
  p2maxotrqv = (x2 +6) - x1
  return p2maxotrqv

def maxadvantagefor1p(x1,x2):

  if x2 >=5: x1=7
  else: x1 =6
  p1maxotrqv = (x1 + 6) - (x2)
  return p1maxotrqv



def maxadvantages2setfor1p(x1,x2,x3,x4,x5,x6):
    wincounter = 0
    if x2 >= x1:
        wincounter = 1

    if wincounter == 0 and x4 > 1:
        x3 = 6 ; x4 = 7 ; x5 = 6 ;
        p1maxotrqv = (x1+x3+x5) - (x2+x4+x6)

    elif wincounter == 0 and x4 <= 1:
        x3 = 6
        p1maxotrqv = (x1+x3+x5) - (x2+x4+x6)
    elif wincounter == 1:
        if x4 <=4:
            x3 = 6 ; x5 = 6
        else:
            x3 = 7 ; x5 = 6
        p1maxotrqv = (x1+x3+x5) - (x2+x4+x6)
    return p1maxotrqv

def maxadvantages2setfor2p(x1,x2,x3,x4,x5,x6):
    wincounter = 0
    if x2 >= x1:
        wincounter = 1
    if wincounter == 1 and x3 > 1:
        x4 = 6 ; x3 = 7 ; x6 = 6 ;
        p2maxotrqv = (x2+x4+x6) - (x1+x3+x5)

    elif wincounter == 1 and x3 <= 1:
        x4 = 6
        p2maxotrqv = (x2+x4+x6) - (x1+x3+x5)
    elif wincounter == 0:
        if x3 <= 4:
            x4 = 6; x6 =6

        else:
            x4 = 7 ; x6 = 6
        p2maxotrqv = (x2 + x4 + x6) - (x1 + x3 + x5)
    return p2maxotrqv


def MaxadvHfulllastset(x1,x2,x3,x4,x5,x6):
  if x6 >=5: x5=7
  else: x5 =6
  result = (x1 + x3 + x5) - (x2 +x4 +x6)
  return result


def maxadvantagefor1p1set(x1,x2):
  if x2 >=5: x1=7
  else: x1 =6
  p1maxotrqv = x1-x2
  return p1maxotrqv

def F1setcal(x1,x2,Betnumber1,Var_P1P2):
    p1maxotrqv = maxadvantagefor1p1set(x1,x2)
    p2maxotrqv = maxadvantagefor1p1set(x2,x1)
    if Var_P1P2 == "1 Игрок":
        F1betcalculator(Betnumber1, p1maxotrqv,p2maxotrqv )
    else:
        F1betcalculator(Betnumber1,p2maxotrqv , p1maxotrqv)

def F1betcalculator(Betnumber1,p1maxotrqv,p2maxotrqv):
    display_var = StringVar()

    if Betnumber1 < -p1maxotrqv:
        #result = "F1(%s) bet is Lost" % (Betnumber1)
        #print(" L | R | W \n---|---|---\n ↑ %s   %s   " % (-p1maxotrqv, p2maxotrqv))
        display_var.set("Ф1(%s) проигрыш\n L | R | W \n---|---|---\n ↑ %s   %s   " % (Betnumber1,-p1maxotrqv,p2maxotrqv))
    elif -p1maxotrqv <= Betnumber1 <= p2maxotrqv:
        #result = "F1(%s) bet is Refund" % (Betnumber1)
        #print(" L | R | W \n---|---|---\n  %s ↑  %s   " % (-p1maxotrqv, p2maxotrqv))
        display_var.set("Ф1(%s) возврат\n L | R | W \n---|---|---\n  %s ↑  %s   " % (Betnumber1,-p1maxotrqv,p2maxotrqv))
    else:
        #result = "F1(%s) bet is Win" % (Betnumber1)
        #print(" L | R | W \n---|---|---\n   %s   %s ↑ " % (-p1maxotrqv, p2maxotrqv))
        display_var.set("Ф1(%s) выигрыш\n L | R | W \n---|---|---\n   %s   %s ↑ " % (Betnumber1,-p1maxotrqv,p2maxotrqv))
    messagebox.showinfo("Результат\n", "%s" % (display_var.get()))



def secondsetmintotal(x1,x2,x3,x4,wincounter):
  if wincounter == 0 and x4<=4:
    x3 =6
  elif wincounter == 0 and x4>4:
    x3 =7
  elif wincounter == 1 and x3 <=4:
    x4=6
  else: x4=7
  print("Min (%s:%s),(%s:%s)" %(x1,x2,x3,x4))
  count = x1+x2+x3+x4
  return count

def secondsetmaxtotal(x1,x2,wincounter):
  count = x1+x2+13+13
  if wincounter == 0:
    print("Max (%s:%s),(6:7),(6:7)" % (x1,x2))
  else:
    print("Max (%s:%s),(7:6),(7:6)" % (x1,x2))
  return count

def betcalculator1(minscore,maxscore,betvector,bettotnumber):
    display_var = StringVar()
    if betvector == "Меньше":
        if bettotnumber < minscore:
            display_var.set("Тотал %s %s проигрыш\n L | R | W \n---|---|---\n ↑  %s  %s   " % (
            betvector, bettotnumber, minscore, maxscore))
        elif minscore <= bettotnumber and bettotnumber <= maxscore:
            display_var.set("Тотал %s %s возврат\n L | R | W \n---|---|---\n  %s ↑ %s   " % (
            betvector, bettotnumber, minscore, maxscore))
        else:
            display_var.set("Тотал %s %s выигрыш! \n L | R | W \n---|---|---\n  %s   %s ↑ " % (
            betvector, bettotnumber, minscore, maxscore))
    else:
        if bettotnumber < minscore:
            display_var.set("Тотал %s %s выигрыш! \n W | R | L \n---|---|---\n ↑ %s   %s   " % (
            betvector, bettotnumber, minscore, maxscore))
        elif minscore <= bettotnumber and bettotnumber <= maxscore:
            display_var.set("Тотал %s %s возврат\n W | R | L \n---|---|---\n  %s ↑ %s   " % (
            betvector, bettotnumber, minscore, maxscore))
        else:
            display_var.set("Тотал %s %s проигрыш \n W | R | L \n---|---|---\n  %s   %s ↑" % (
            betvector, bettotnumber, minscore, maxscore))
    messagebox.showinfo("Результат", "%s" % (display_var.get()))

def thirdsetmintotal(x1,x2,x3,x4,x5, x6):
    x5, x6 = addpoints(x5, x6)
    print(x1, x2, x3, x4, x5, x6)
    count = x1 + x2 + x3 + x4 + x5 + x6
    return count

def thirdsetmaxtotal(x1, x2, x3, x4):
    count = x1 + x2 + x3 + x4 + 13
    return count
def addpoints(x1, x2):
    if x1 >= x2 and x2 <= 4:
        x1 = 6
    elif x1 >= x2 and x2 > 4:
        x1 = 7
    elif x1 < x2 and x1 <= 4:
        x2 = 6
    else:
        x2 = 7
    return x1,x2

def totalfulset(x1, x2, x3, x4, x5, x6, betvector, bettotnumber):
    list = (6, 7)
    if var1x2.get() in list or var2x2.get in list:
        minscore = thirdsetmintotal(x1,x2,x3,x4,x5, x6)
        maxscore = thirdsetmaxtotal(x1, x2, x3, x4)
        print("I am Here, IF statement total fullset ")
        print(x1,x2,x3,x4,x5,x6)
        betcalculator1(minscore, maxscore, betvector, bettotnumber)

    elif var1x1.get() in list or var2x1.get() in list:
        wincounter = 0
        if x2 >= x1:
            wincounter = 1
        minscore = secondsetmintotal(x1,x2,x3,x4,wincounter)
        maxscore = secondsetmaxtotal(x1, x2, wincounter)
        print("I am Here, elif statement total fullset ")
        print(x1, x2, x3, x4, x5, x6)
        betcalculator1(minscore, maxscore, betvector, bettotnumber)
    else:
        x1,x2 = addpoints(x1, x2)
        minscore = x1+x2+6
        maxscore= 13+13+13
        print(x1, x2, x3, x4, x5, x6)
        print("I am Here, else statement total fullset ")
        betcalculator1(minscore, maxscore, betvector, bettotnumber)

def addMinMax(x1,x2,betvector,bettotnumber):

    display_var = StringVar()
    minscore = 0
    if x1 > x2:
        if x2 <= 4:
            x1 = 6
        else:
            x1 = 7
    else:
        if x1 <= 4:
            x2 = 6
        else:
            x2 = 7
    minscore = x1 + x2
    print(minscore)
    print(bettotnumber)
    print(betvector)
    maxscore = 13
    betcalculator1(minscore, maxscore, betvector, bettotnumber)

def func(*args):
    choiceMenuUO.grid_forget()
    option1.grid_forget()
    option2.grid_forget()
    option3.grid_forget()
    option4.grid_forget()
    option5.grid_forget()
    option6.grid_forget()
    choiceMenuP1P2.grid_forget()
    if Var_choice1.get() == "Тотал сета":
        choiceMenuUO.grid(row=2, column =0)
        option1.grid(row=0,column=1)
        option2.grid(row=0,column=2)
        Entry_1 = Entry(window, textvariable=Betnumber1)
        Entry_1.grid(row=3,column=0)
        button_RashetTotSet = Button(window,text="Расчёт",command= lambda: addMinMax(var1x1.get(),var2x1.get(), Var_OU.get(),Betnumber1.get())).grid(row=4,column=0)
    elif Var_choice1.get() == "Тотал матча":
        choiceMenuUO.grid(row=2, column =0)
        option1.grid(row=0, column=1)
        option2.grid(row=0, column=2)
        option3.grid(row=0, column=3)
        option4.grid(row=0, column=4)
        option5.grid(row=0, column=5)
        option6.grid(row=0, column=6)
        Entry_1 = Entry(window, textvariable=Betnumber1)
        Entry_1.grid(row=3,column=0)
        button_RashetTotSet = Button(window, text="Расчёт",
                                     command=lambda: totalfulset(var1x1.get(), var2x1.get(),var1x2.get(),var2x2.get(),var1x3.get(),var2x3.get(), Var_OU.get(),Betnumber1.get())).grid(row=4,column=0)
    elif Var_choice1.get() == "Фора сета":
        choiceMenuP1P2.grid(row=2, column =0)
        option1.grid(row=0, column=1)
        option2.grid(row=0, column=2)
        Entry_1 = Entry(window, textvariable=Betnumber1)
        Entry_1.grid(row=3,column=0)
        button_RashetTotSet = Button(window, text="Расчёт",
                                  command=lambda: F1setcal(var1x1.get(), var2x1.get(), Betnumber1.get(),
                                                           Var_P1P2.get())).grid(row=4,column=0)
    else:
        choiceMenuP1P2.grid(row=2, column =0)
        option1.grid(row=0, column=1)
        option2.grid(row=0, column=2)
        option3.grid(row=0, column=3)
        option4.grid(row=0, column=4)
        option5.grid(row=0, column=5)
        option6.grid(row=0, column=6)
        Entry_1 = Entry(window, textvariable=Betnumber1)
        Entry_1.grid(row=3,column=0)
        button_RashetTotSet = Button(window, text="Расчёт",
                                     command=lambda: Hfullset(var1x1.get(), var2x1.get(),var1x2.get(),var2x2.get(),var1x3.get(),var2x3.get(), Betnumber1.get(),
                                                              Var_P1P2.get())).grid(row=4,column=0)
Var_choice1 = StringVar()
choiceMenu = OptionMenu(window, Var_choice1 , "Тотал сета", "Тотал матча", "Фора сета", "Фора матча", command= func)
choiceMenu.grid(row=0,column=0)
window.mainloop()