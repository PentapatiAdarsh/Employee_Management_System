

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *
import random as r



# Create your views here.
def homepage(request):
    return render(request, 'index.html')

# Create your views here.
def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.POST['aid']
    pwd=request.POST['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')




def feature_selection(request):
    if request.method == 'POST':
        
        from .FeatureSelection import featureselection
        featureselection.calc()
        return render(request, 'feature_selection.html', {'b':True,'msg':'Feature Selection Completed '})

    else:
        return render(request, 'feature_selection.html')


def classification(request):
    return render(request, 'classification.html')

from .FeatureSelection2 import featureselection
def nbtrain(request):
    
    features=featureselection.calc()

    
    
    from .Training import Training
    sc = Training.train(2, features)

    performance.objects.filter(alg_name='Naive Bayes').delete()
    
    d = performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Naive Bayes Algorithm's training & testing completed"})


def dttrain(request):
    features=featureselection.calc()
    from .Training import Training
    sc = Training.train(4, features)
    performance.objects.filter(alg_name='Decision Tree').delete()
  
    d = performance(alg_name='Decision Tree', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Decision Tree Algorithm's training & testing completed"})


def svmtrain(request):
    features=featureselection.calc()
    from .Training import Training
    sc = Training.train(3, features)
    performance.objects.filter(alg_name='SVM').delete()
  
    d = performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "SVM Algorithm's training & testing completed"})



def rftrain(request):
    features=featureselection.calc()
    from .Training import Training
    sc = Training.train(1, features)
    performance.objects.filter(alg_name='Random Forest').delete()
    d = performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])

    d.save()

    return render(request, 'classification.html', {'msg': "Random Forest Algorithm's training & testing completed"})


def lrtrain(request):
    features=featureselection.calc()
    from .Training import Training
    sc = Training.train(5, features)
    performance.objects.filter(alg_name='Logistic Regression').delete()
    d = performance(alg_name='Logistic Regression', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "Logistic Regression Algorithm's training & testing completed"})

def evaluation(request):
    from .Graphs import viewg
    
    d = performance.objects.all()
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc1
        
    try:viewg(val, 'accuracy.png', 'Accuracy')
    except:pass
    
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc2
    try:viewg(val, 'precision.png', 'Precision')
    except:pass
    
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc3
    try:viewg(val, 'recall.png', 'Recall')
    except:pass

    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc4
    try:viewg(val, 'f1.png', 'F1 Score')
    except:pass

    return render(request, 'viewacc.html', {'data': d})





def hrlogin(request):
    return render(request, 'hr.html')


def hrloginaction(request):
    userid=request.POST['aid']
    pwd=request.POST['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='HR' and pwd=="HR":
        request.session['hrid']='admin'
        return render(request, 'hrhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'hr.html',{'msg':err})



def hrhome(request):
    return render(request, 'hrhome.html')


def hrlogout(request):
    return render(request, 'hr.html')



def attrition(request):
    if request.method == 'POST':

        file=request.POST['file']

        from .FeatureSelection2 import featureselection
        features=featureselection.calc()
    
        from .Prediction import Prediction
        empid,res=Prediction.get(features, file)

        d=dict({})

        for i in range(len(empid)):
            d[empid[i]]=res[i]
        
        from .Freq import CountFrequency
        resdict=CountFrequency(res)

        from .Graphs import viewg
        viewg(resdict,'prediction.jpg','Prediction Result')
       
        return render(request, 'attritionres.html', {'data':d})

    else:
        return render(request, 'attrition.html')

