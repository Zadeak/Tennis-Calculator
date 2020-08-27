import eel
import jinja2

# Helper functions
def scoreConverter(*args):
    #converts string arguments from JS to int for python usage
    for i in args:
        yield int(i)
def betConverter(bet):
    #converts string arguments from JS to float for python usage
    bet = float(bet)

    return bet
def maxadvantagefor1p1set(x1,x2):
  if x2 >=5: x1=7
  else: x1 =6
  p1maxotrqv = x1-x2
  return p1maxotrqv

# Main functions, invoked from JS script file
@eel.expose
def H1set(x1,x2,Var_P1P2,Betnumber1):
    print("x1",x1,"x2",x2,"Var_P1P2",Var_P1P2,'Betnumber1',Betnumber1)
    x1,x2 = scoreConverter(x1,x2)
    Betnumber1 = betConverter(Betnumber1)
    print(" NEW x1",x1,"x2",x2,"Var_P1P2",Var_P1P2,'Betnumber1',Betnumber1)
    p1maxotrqv = maxadvantagefor1p1set(x1,x2)
    p2maxotrqv = maxadvantagefor1p1set(x2,x1)
    print("p1maxotrqv",p1maxotrqv)
    print('p2maxotrqv',p2maxotrqv)
    if Var_P1P2 == "P1":
        print("True, var_p1p2 = ",Var_P1P2)
        result = F1betcalculator(Betnumber1, p1maxotrqv,p2maxotrqv, Var_P1P2)
    else:
        print("False, var_p1p2 = ",Var_P1P2)
        result = F1betcalculator(Betnumber1,p2maxotrqv , p1maxotrqv,Var_P1P2)
    return result


@eel.expose
def Hfullset(x1,x2,x3,x4,x5,x6,Var_P1P2,Betnumber1):
    x1,x2,x3,x4,x5,x6= scoreConverter(x1,x2,x3,x4,x5,x6)
    Betnumber1 = betConverter(Betnumber1)
    print(x1,x2,x3,x4,x5,x6,Betnumber1)
    list = (6, 7)
    if x3 in list or x4 in list:
        p1maxotrqv = MaxadvHfulllastset(x1,x2,x3,x4,x5,x6)
        p2maxotrqv = MaxadvHfulllastset(x1,x2,x3,x4,x6,x5)
    elif x1 in list or x2 in list:
        p1maxotrqv = maxadvantages2setfor1p(x1,x2,x3,x4,x5,x6)
        p2maxotrqv = maxadvantages2setfor2p(x1,x2,x3,x4,x5,x6)
    else:
        p1maxotrqv = maxadvantagefor1p(x1,x2)
        p2maxotrqv = maxadvantagefor2p(x1,x2)
    if Var_P1P2 == "P1":
        result = F1betcalculator(Betnumber1, p1maxotrqv, p2maxotrqv,Var_P1P2)
    else:
        result = F1betcalculator(Betnumber1, p2maxotrqv, p1maxotrqv,Var_P1P2)
    return result

@eel.expose
def TotalOneSet(x1,x2,vector,bet):
    x1,x2 = scoreConverter(x1,x2)
    bet = betConverter(bet)
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
    maxscore = 13
    result = betcalculator1(minscore, maxscore, vector, bet)
    return result

@eel.expose
def TotalMatch(x1, x2, x3, x4, x5, x6, vector, bet):
    list = (6, 7)
    x1,x2,x3,x4,x5,x6 = scoreConverter(x1,x2,x3,x4,x5,x6)
    bet = betConverter(bet)
    if x3 in list or x4 in list:
        minscore = thirdsetmintotal(x1,x2,x3,x4,x5, x6)
        maxscore = thirdsetmaxtotal(x1, x2, x3, x4)
        print("I am Here, IF statement total fullset ")
        print(x1,x2,x3,x4,x5,x6)
        result = betcalculator1(minscore, maxscore, vector, bet)

    elif x1 in list or x2 in list:
        wincounter = 0
        if x2 >= x1:
            wincounter = 1
        minscore = secondsetmintotal(x1,x2,x3,x4,wincounter)
        maxscore = secondsetmaxtotal(x1, x2, wincounter)
        print("I am Here, elif statement total fullset ")
        print(x1, x2, x3, x4, x5, x6)
        result = betcalculator1(minscore, maxscore, vector, bet)
    else:
        x1,x2 = addpoints(x1, x2)
        minscore = x1+x2+6
        maxscore= 13+13+13
        print(x1, x2, x3, x4, x5, x6)
        print("I am Here, else statement total fullset ")
        result = betcalculator1(minscore, maxscore, vector, bet)
    return result


# Additional functions, main calculator logic
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

def maxadvantagefor1p(x1,x2):

  if x2 >=5: x1=7
  else: x1 =6
  p1maxotrqv = (x1 + 6) - (x2)
  return p1maxotrqv
def maxadvantagefor2p(x1,x2):
  if x1 >=5: x2=7
  else: x2 =6
  p2maxotrqv = (x2 +6) - x1
  return p2maxotrqv

def MaxadvHfulllastset(x1,x2,x3,x4,x5,x6):
  if x6 >=5: x5=7
  else: x5 =6
  result = (x1 + x3 + x5) - (x2 +x4 +x6)
  return result

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


def F1betcalculator(Betnumber1,p1maxotrqv,p2maxotrqv,Var_P1P2):
    if Var_P1P2 == "P1":
        Var_P1P2 = 1
    else:
        Var_P1P2 = 2
    result = {"first_status": "L",
              "second_status": "R",
              "third_status": "W",
              "first_result": "",
              "vector": Betnumber1,
              "second_result": "",
              "third_result": "",
              "first_limit": -p1maxotrqv,
              "second_limit": p2maxotrqv
              }
    print("Betnumber1 =",Betnumber1,'-p1maxotrqv = ',"-",p1maxotrqv)
    if Betnumber1 < -p1maxotrqv:
        result["first_result"] = "↑L"
        result["vector"] = "Ф%s(%s): Проигрыш" % (Var_P1P2,Betnumber1)
    elif -p1maxotrqv <= Betnumber1 <= p2maxotrqv:
        result["second_result"] = "↑R"
        result["vector"] = "Ф%s(%s): Возврат" % (Var_P1P2, Betnumber1)
    else:
        result["third_result"] = "↑W"
        result["vector"] = "Ф%s(%s): Выигрыш" % (Var_P1P2, Betnumber1)
    htmlCode = getResultcode(result)
    return htmlCode

def maxadvantagefor1p1set(x1,x2):
  if x2 >=5: x1=7
  else: x1 =6
  maxotrqv = x1-x2
  return maxotrqv



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


def thirdsetmaxtotal(x1, x2, x3, x4):
    count = x1 + x2 + x3 + x4 + 13
    return count


def thirdsetmintotal(x1,x2,x3,x4,x5, x6):
    x5, x6 = addpoints(x5, x6)
    print(x1, x2, x3, x4, x5, x6)
    count = x1 + x2 + x3 + x4 + x5 + x6
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





def betcalculator1(minscore,maxscore,vector,bet):

    print("after",vector)
    if vector == "Under": vector = "Меньше"
    else:vector = "Больше"

    print("before",vector)
    if vector == "Меньше":
        result = {"first_status": "L",
                  "second_status": "R",
                  "third_status": "W",
                  "vector": vector,
                  "first_limit": minscore,
                  "second_limit": maxscore
                  }
        if bet < minscore:
            result["first_result"] = "↑L"
            result["vector"] = "Ставка Тотал" + vector + "(" + str(bet) + "):Проигрыш"
            print(result)
        elif minscore <= bet and bet <= maxscore:
            result["second_result"] = "↑R"
            result["vector"] = "Ставка Тотал" + vector + "(" + str(bet) + "):Возврат"
            print(result)
        else:
            result["third_result"] = "↑W"
            result["vector"] = "Ставка Тотал" + vector + "(" + str(bet) + "):Выигрыш"
            print(result)
    else:
        result = {"first_status": "W",
                  "second_status": "R",
                  "third_status": "L",
                  "vector": vector,
                  "first_limit" : minscore,
                  "second_limit" : maxscore
                    }
        if bet < minscore:
            result["first_result"] = "↑W"
            result["vector"] = "Ставка Тотал"+ vector +"("+ str(bet) + "):Выигрыш"
            print(result)
        elif minscore <= bet and bet <= maxscore:
            result["second_result"] = "↑R"
            result["vector"] = "Ставка Тотал"+ vector +"("+ str(bet) + "):Возврат"
            print(result)
        else:
            result["third_result"] = "↑L"
            result["vector"] = "Ставка Тотал"+ vector +"("+ str(bet) + "):Проигрыш"
            print(result)
    print("this is finale",result)
    htmlCode = getResultcode(result)
    return htmlCode


@eel.expose
def getHtmlcode(mode,type):
    handDict = {
        "first_entry": "P1",
        "first_entry_text": "П1",
        "second_entry": "P2",
        "second_entry_text": "П2",
        "bet_name": "Значение форы"
    }
    totalDict = {
        "first_entry": "Under",
        "first_entry_text": "Меньше",
        "second_entry": "Over",
        "second_entry_text": "Больше",
        "bet_name": "Значение тотала"
    }
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('web/templates'))
    if type == "Set":
        template = jinja_env.get_template("formOneSetTemplate.html")
        if mode == "handycap":
            result = template.render(handDict)
        else:
            result = template.render(totalDict)
    elif type == "match":
        template = jinja_env.get_template("formMatchTemplate.html")
        if mode == "handycap":
            result = template.render(handDict)
        else:
            result = template.render(totalDict)
    return result

def getResultcode(argument):
    print("here i am",argument)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('web/templates'))
    template = jinja_env.get_template("resultPage.html")
    result = template.render(argument)
    return result


