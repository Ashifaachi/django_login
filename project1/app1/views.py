from django.shortcuts import render,redirect
from . form import UserForm,LogginForm
from . models import UserProfile,GALLERY
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallary(request):
    images=GALLERY.objects.all()
    
    return render(request,'gallary.html',{'images':images})
def details(request, id): 
    images=GALLERY.objects.get(id=id)
    return render(request,'details.html',{'images':images}) 
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            na = form.cleaned_data['name']
            ag = form.cleaned_data['age']
            pl = form.cleaned_data['place']
            emal = form.cleaned_data['email']
            paswd = form.cleaned_data['password']
            sql = UserProfile(name=na,age=ag,place=pl,email=emal,password=paswd)
            sql.save()
            return redirect(reverse('app1:login'))
        else:
            print(form.errors)
    else:
        form = UserForm()

    return render(request,'register.html',{'form':form})
def login(request):
    if request.method == 'POST':
        form =LogginForm(request.POST)
        if form.is_valid():
            emal = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
            # sql =UserProfile(email=emal,password=passwd)
            try:
                user=UserProfile.objects.get(email=emal)
                if not user:
                    messages.warning(request,'Email does not exist')
                    return redirect(reverse('app1:register'))
                elif passwd != user.password:
                    messages.warning(request,'Password Incorrect')
                    return redirect(reverse('app1:register'))
                else:
                    messages.success(request,'success')
                    return redirect(reverse('app1:gallary'))
            except:
                messages.warning(request,'Email or Password Incorrect')
                return redirect(reverse('app1:register'))
    else:
        form=LogginForm()



    return render(request,'login.html',{'form':form})

