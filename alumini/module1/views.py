from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from module1.models import Alumi

# Create your views here.

def home(request):
    results=list(Alumi.objects.all()[::-1])[0:6]
    if request.method=="POST":
        s=request.POST.get('search')
        objs=Alumi.objects.filter(person_first_name__icontains=s)
        return render(request,'home.html',{'res':objs})
    return render(request,'home.html',{'res':results})


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def profile(request):
    return render(request,'profile.html')


def dedicated(request,rid):
    if Alumi.objects.filter(id=rid).exists():
        single=Alumi.objects.get(id=rid)
        return render(request,'dedicated.html',{'alumi':single})
    else:
        return redirect('home')


def more(request):
    return render(request,'more.html')

@login_required(login_url='loginPage')
def register(request):
    
    if request.method=="POST" and request.user.is_staff:
        roll=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        branch=request.POST.get('branch')
        batch=request.POST.get('batch')
        company=request.POST.get('company')
        role=request.POST.get('role')
        location=request.POST.get('location')
        exp=request.POST.get('exp')
        achievements=request.POST.get('achievements')
        linkedin=request.POST.get('linkedin')
        port=request.POST.get('port')
        github=request.POST.get('github')
        pic=request.FILES.get('pic')

        usr = User.objects.create_user(username=roll,first_name=fname,last_name=lname,email=mail,password="dummy@123")
        usr.save()

        alu = Alumi(person=usr,branch=branch,passedOut=batch,achievements=achievements,company=company,
                    role=role,exp=exp,workLocation=location,gitHub=github,linkedIn=linkedin,portfolio=port,image=pic)
        alu.save()
        redirect('register')

    return render(request,'register.html')

@login_required(login_url='loginPage')
def staff(request):
    result=Alumi.objects.all()[::-1]
    return render(request,'staff.html',{'res':result})

@login_required(login_url='loginPage')
def update(request,rid):
    if request.user.is_staff:
        if request.method=="POST":
            obj=Alumi.objects.get(id=rid)
            obj.person.username=request.POST.get('uname')
            obj.person.first_name=request.POST.get('fname')
            obj.person.last_name=request.POST.get('lname')
            obj.person.email=request.POST.get('mail')
            obj.branch=request.POST.get('branch')
            obj.passedOut=request.POST.get('batch')
            obj.company=request.POST.get('company')
            obj.role=request.POST.get('role')
            obj.workLocation=request.POST.get('location')
            obj.exp=request.POST.get('exp')
            obj.achievements=request.POST.get('achievements')
            obj.linkedIn=request.POST.get('linkedin')
            obj.portfolio=request.POST.get('port')
            obj.gitHub=request.POST.get('github')
            obj.save()
            return redirect('staff')
            
        if Alumi.objects.filter(id=rid).exists():
            obj=Alumi.objects.get(id=rid)
            return render(request,'update.html',{'res':obj})
        return redirect('staff')
    return redirect('home')

def loginView(request):
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        obj=authenticate(request,username=a,password=b)
        if obj:
            login(request,obj)
            return redirect('home')
        else:
            return redirect('loginPage')

    return render(request,'login.html')


def logoutView(request):
    return redirect('home')

@login_required(login_url='loginPage')
def delete(request,rid):
    if request.user.is_staff:
        obj=Alumi.objects.get(id=rid)
        usr_id=obj.person.id
        obj2=User.objects.get(id=usr_id)
        obj.delete()
        obj2.delete()
        return redirect('staff')
    else:
        return redirect('home')

    return redirect('staff')