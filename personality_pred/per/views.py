from django.shortcuts import render
import numpy as np
import datetime
import pickle
from .models import Applicant
# Create your views here.
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

def calculate(answers):
    o = 0
    c = 0
    e = 0
    a = 0
    n = 0

    # for ques 1
    temp0 = int(answers[0])
    n += temp0

    # for ques 2
    temp1 = int(answers[1])
    c += temp1

    # for ques 3
    temp2 = int(answers[2])
    o += (6-temp2)

    # for ques 4
    temp3 = int(answers[3])
    e += temp3

    # for ques 5
    temp4 = int(answers[4])
    c += (6-temp4)

    # for ques 6
    temp5 = int(answers[5])
    a += (6-temp5)

    # for ques 7
    temp6 = int(answers[6])
    n += (6-temp6)

    # for ques 8
    temp7 = int(answers[7])
    e += temp7

    # for ques 9
    temp8 = int(answers[8])
    o += temp8

    # for ques 10
    temp9 = int(answers[9])
    a += temp9

    return o, c, e, a, n
def predict(request):
    if request.method == 'POST':
        ans = []
        ans.append(request.POST['mycheckbox'])
        ans.append(request.POST['mycheckbox1'])
        ans.append(request.POST['mycheckbox2'])
        ans.append(request.POST['mycheckbox3'])
        ans.append(request.POST['mycheckbox4'])
        ans.append(request.POST['mycheckbox5'])
        ans.append(request.POST['mycheckbox6'])
        ans.append(request.POST['mycheckbox7'])
        ans.append(request.POST['mycheckbox8'])
        ans.append(request.POST['mycheckbox9'])
        # essentials = details.split('%')
        essentials=[None,None,request.POST['Gender'],request.POST['dob']]
        name=request.POST['name']
        email=request.POST['email']
        o1, c1, e1, a1, n1 = calculate(ans)
        data = []
        if(essentials[2].lower() == 'male'):
            encoded_gender=0
        else:
            encoded_gender=1
        data.append(int(datetime.datetime.today().year) -
                    int(essentials[3].split('-')[0]))
        data.append(o1)
        data.append(n1)
        data.append(c1)
        data.append(a1)
        data.append(e1)
        data = np.array(data).reshape(1, 6)
        data=scaler.transform(data)
        data = np.concatenate((np.array([[encoded_gender]]), data), axis=1)
        p = model.predict(data)
        print(p)
        applicant=Applicant(name=name, email=email, dob=essentials[3], gender=essentials[2], 
                            personality=p[0], openness=o1, neuroticism=n1, conscientiousness=c1, agreeableness=a1, extraversion=e1)
        applicant.save()
        d = {"serious": "Characterized by a focused, solemn, and earnest demeanor; displaying a no-nonsense attitude in various aspects of life.",
    "extraverted": "Outgoing and sociable; enjoys being around people, seeks social interaction, and tends to be energetic in social settings.",
    "dependable": "Reliable, trustworthy, and consistent in fulfilling responsibilities; demonstrates a high level of dependability and accountability.",
    "lively": "Full of energy, enthusiasm, and vivacity; characterized by an animated and spirited approach to various activities.",
    "responsible": "Conscientious, accountable, and diligent in fulfilling obligations; exhibits a sense of duty and reliability in various roles."}
        var=d[applicant.personality]
        return render(request, 'results.html', {'applicant':applicant, 'var':var})

def quiz(request):
    return render(request, 'quiz.html')