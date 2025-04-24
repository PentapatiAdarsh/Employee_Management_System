

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *
import random as r
from .DateTime import getdate


import mimetypes


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


def signuppage(request):
    if request.method == 'POST':
        e_mail = request.POST['mail']

        d = employees.objects.filter(e_mail__exact=e_mail).count()
        if d > 0:
            return render(request, 'signup.html', {'msg': "e_mail Already Registered"})
        else:

            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            role = request.POST['role']
            n_a_m_e = request.POST['n_a_m_e']
        
            d = employees(n_a_m_e=n_a_m_e, e_mail=e_mail, pass_word=pass_word, phone=phone, role=role)
            d.save()

            return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'signup.html')

    
	
def userloginaction(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pass_word=request.POST['pwd']
		d=employees.objects.filter(e_mail__exact=uid).filter(pass_word__exact=pass_word).count()
		
		if d>0:
			d=employees.objects.filter(e_mail__exact=uid)
			request.session['e_mail']=uid
			request.session['n_a_m_e']=d[0].n_a_m_e
			request.session['sc_calls']=""
			

			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')




def userlogoutdef(request):
    if "e_mail" in request.session:
        del request.session['e_mail']
        return render(request, 'user.html')
    else:
        return render(request, 'user.html')




def userhomedef(request):
	if "e_mail" in request.session:
		e_mail=request.session["e_mail"]
		d=employees.objects.filter(e_mail__exact=e_mail)
	
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return redirect('userlogoutdef')

		
def viewprofilepage(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		d=employees.objects.filter(e_mail__exact=uid)
		

		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')


def updateprofile(request):
    if request.method == 'POST':
        name = request.POST["name"] 
        phone = request.POST['phone']
        email = request.session["e_mail"]
        employees.objects.filter(e_mail=email).update(n_a_m_e=name, phone=phone)
        
        return render(request, 'user_home.html',{'msg':'Profile Updated !!'} )
       
    else:
        email = request.session["e_mail"]
        d = employees.objects.filter(e_mail=email)
   
        return render(request, 'updateprofile.html', {'data': d[0]})




def updatepwd(request):
    if request.method == 'POST':
        newpwd = request.POST["newpwd"] 
        old = request.POST['old']
        email = request.session["e_mail"]
        d=employees.objects.filter(e_mail=email).filter(pass_word=old).count()
        if d>0:
            employees.objects.filter(e_mail=email).update(pass_word=newpwd)
        return render(request, 'user_home.html',{'msg':'Password Updated !!'} )
       
    else:
        
        return render(request, 'updatepwd.html')








def fileupload(request):
    if request.method == 'POST':
        file = request.POST['file']
        filen=file
        file2 = 'Data/' + file
        title = request.POST['Title']
        access = request.POST['access']
    
        email = request.session["e_mail"]
        name = request.session["n_a_m_e"]
        f = open(file2, "r")
        dt = f.read()


        
        d = files(user=email, username=name, filename=filen, filetitle=title, access=access, filedata=dt, stz='Online')
        d.save()
    
        return render(request, 'user_home.html', {'msg': 'File Uploaded ! '})
    

        #-------------------------------------------




        
    
    else:
        return render(request, 'uploadfile.html')
        

def viewfiles(request):
    if "e_mail" in request.session:
        email = request.session["e_mail"]
        d = files.objects.filter(stz='Online', user=email)
    
        return render(request, 'viewfiles.html', {'data': d})
    
    else:
        return render(request, 'user.html')

def viewfile(request, op):
    if "e_mail" in request.session:
        d = files.objects.filter(id=op)

        
        return render(request, 'viewfile.html', {'d': d[0]})

    else:
        return render(request, 'user.html')

def filedownload(request):
    if "e_mail" in request.session:
        fid = request.POST['fid']
        fname = request.POST['fname']
        data = request.POST['data']

        print(fname,'<<<<<<<<<<<<<<<<<<<<<<<<<<<')

        
        d = files.objects.filter(id=fid)



        filepath = 'D:\\Django\\EMS\\Data\\'+fname
        print(filepath)
        path = open(filepath)
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % fname
        return response

        return render(request, 'viewfile.html', {'d': d[0]})

    else:
       return render(request, 'user.html')
	   

def fileupdate(request, op):
    if request.method == 'POST':
        pass

    else:
        d = files.objects.filter(id=op)
        return render(request, 'fileupdate.html', {'d': d[0]})


def fileupdateaction(request):
    if request.method == 'POST':
        fid = request.POST['fid']
        fname = request.POST['fname']
        data = request.POST['data']

        files.objects.filter(id=fid).update(filedata=data)

        
        return redirect('viewfiles')
    else:
        pass


def chgaccess(request, op):
    if request.method == 'POST':
        pass
    else:
        d = files.objects.filter(id=op)
        return render(request, 'fileaccess.html', {'d': d[0]})

def chgaccessaction(request):
    if request.method == 'POST':
        fid = request.POST['fid']
        access = request.POST['access']

        files.objects.filter(id=fid).update(access=access)

        

        return redirect('viewfiles')
    else:
        pass


def delete(request, op):
    if request.method == 'POST':
        pass
    else:
        scupdate(request, "FileDelete")
        d = files.objects.filter(id=op).update(stz="ofline")
        return redirect('viewfiles')

def search(request):
    if request.method == 'POST':
        keys = request.POST['keys']
        print(keys)
       
        d=files.objects.filter(filetitle__icontains=keys).filter(stz='Online').filter(access='Public')
        return render(request, 'searchresults.html', {'data': d})
        
    else:
        return render(request, 'search.html')

def newmail(request):
    if request.method == 'POST':
        email = request.session["e_mail"]
        name = request.session["n_a_m_e"] 
        sub = request.POST['sub']
        body = request.POST['body']
        t_o = request.POST['t_o']
        dt=getdate()
        
        d = mails(sender=email, sendername=name, recipient=t_o, title=sub, data=body, datetime=dt)
        d.save()
    
        return render(request, 'user_home.html',{'msg':'Mail Sent !!'} )
        
    else:
        

        return render(request, 'compose.html')


def inbox(request):
    if "e_mail" in request.session:
        email = request.session["e_mail"]
        d = mails.objects.filter(recipient=email).order_by("-id")
    
        
    
        return render(request, 'viewmails.html', {'data': d})
    
    else:
        return render(request, 'user.html')


def viewmail(request, op):
    if request.method == 'POST':
        pass

    else:
        d = mails.objects.filter(id=op)
        return render(request, 'viewmail.html', {'d': d[0]})

def viewemp(request):
    d=employees.objects.filter()
    return render(request, 'viewemp.html', {'data': d})
