from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Blog,Student
import datetime
from blogapp.forms import StudentFormClass,StudentModelFormClass,UserRegister
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def aboutpage(request):
    #return HttpResponse("This is about page")
    print("In about page ")
    return HttpResponse("In about page")

def contactpage(request):

    return HttpResponse("This is contact Page")

def edit(request,rid):
    #print("ID to be edited:",rid)
    if request.method=="GET":
        b=Blog.objects.filter(id=rid)
        context={}
        context['blog']=b
        return render(request,'editblog.html',context)
    else:
        #Fetch new changes from the form 
        utitle=request.POST['title']
        udetail=request.POST['detail']
        ucat=request.POST['cat']

        #print("Updated title:",utitle)
        #print("Update detail:",udetail)
        #print("Updated Category:",ucat)
        b=Blog.objects.filter(id=rid)
        b.update(title=utitle,detail=udetail,cat=ucat)
        return redirect('/userdashboard')

def delete(request,rid):
    #print("ID to be deleted:",rid)
    b=Blog.objects.filter(id=rid)
    #print(b)
    b.delete() # to delete object or row from table
    return redirect('/userdashboard')
'''
def homepage(request,x,y):
    print("Value of x:",x)
    print("value of y:",y)

    return HttpResponse("Value of x and Y:"+x+" "+y)
'''
def helloview(request):
    context={}
    context['uname']="Sunny"
    context['x']=1000
    context['y']=200
    context['l']=[10,20,'Itvedant',90.8]
    return render(request,'hello.html',context)


#blog application View function start
def homepage(request):
    b=Blog.objects.filter(is_published=True)
    #select * from blogapp_blog where is_published=1;
    context={}
    context['blog']=b
    return render(request,'home.html',context)


def user_dashboard(request):
  if request.user.is_authenticated: 
    b=Blog.objects.filter(uid=request.user.id)
    #select * from blogapp_blog where uid=4
    #select * from blogapp_blog where uid=3
    context={}
    context['blogs']=b
    return render(request,'dashboard.html',context)
  else:
      return redirect('/login')

def create_blog(request):
    #print("Method Type:",request.method)
 if request.user.is_authenticated:
    if request.method=="GET":#GET==GET T | POST == GET F
       #print("IN GET section")
       return render(request,'create_blog.html')
    else:
       #print("In POST section")
       #Fetching data from Form request using POST dictionary
       btitle=request.POST['title']
       bdet=request.POST['detail']
       bcat=request.POST['cat']

       #print("Title:",btitle)
       #print("Details:",bdet)
       #print("Category:",bcat)

       b=Blog.objects.create(title=btitle,detail=bdet,cat=bcat,uid=request.user.id,created_at=datetime.datetime.now())
       b.save()

       #return HttpResponse("Data Inserted Successfully")
       return redirect('/userdashboard')
    
 else:
     return redirect('/login')
    

def view_details(request,rid):
    #print("Id to be used for details:",rid)
    b=Blog.objects.filter(id=rid)
    #print(b)
    context={}
    context['blog']=b
    return render(request,"blog_details.html",context)


def is_published(request,status,rid):
    #print("Status is:",status)
    #print("Id to be edited:",rid)

    b=Blog.objects.filter(id=rid)
    #print(b)
    context={}
    context['blog']=b
    if status == 'P':
        b.update(is_published=True)
        context['pmsg']="Blog Has been Published Successfully"
    else:
        b.update(is_published=False)
        context['umsg']="Blog Has been Unpublished Successfully"
        
    return render(request,'blog_details.html',context)


def setcookies(request):
    res=render(request,'set_cookies.html')
    print("Response Object:",res)
    res.set_cookie('name','ITVEDANT')
    return res


def getcookies(request):
    cdata=request.COOKIES['name']
    print("Data in the cookies:",cdata)
    context={}
    context['data']=cdata 
    return render(request,'getcookies.html',context)

def setsession(request):

    request.session['learning']="Session and Cookies"
    return render(request,'set_session.html')

def getsession(request):
    sdata=request.session['learning']
    print("Data in the session:",sdata)
    context={}
    context['data']=sdata
    return render(request,'get_session.html',context)


def djangoForm(request):
    context={}
    if request.method=="GET":
        s=StudentFormClass()
        #print(s)
        context['fm']=s
        return render(request,'studentform.html',context)
    else:
        n=request.POST['name']
        r=request.POST['roll_number']
        per=request.POST['percentage']

        #print(n)
        #print(r)
        #print(per)
        s=Student.objects.create(name=n,rno=r,per=per)
        s.save()
        return HttpResponse("Data Inserted")
    
def djangomodelform(request):
    context={}
    if request.method=="GET":
        mfm=StudentModelFormClass()
        #print(mfm)
        context['mform']=mfm
        return render(request,'studentmodelform.html',context)
    else:
        pass

#Registration
def user_register(request):
    context={}
    if request.method=="GET":
        regfm=UserRegister()
        #print("GET:")
        #print(regfm)
        context['rfm']=regfm 
        return render(request,'register.html',context)
    else:
        #print(request.POST)
        print("POST:")
        dregfm=UserRegister(request.POST)
        #print(dregfm)
        dregfm.save()

        return render(request,'register_success.html')
    
#Login

def user_login(request):
    context={}
    loginfm=AuthenticationForm()
    context['lgfm']=loginfm

    if request.method=="GET":
        return render(request,'login.html',context)
    else:
        uname=request.POST['username']
        upass=request.POST['password']
        #print("Username:",uname)
        #print("Password:",upass)
        u=authenticate(username=uname,password=upass)
        #print("Returned Value by authenticate: ",u)

        if u is not None:#firstuser is not None => True|None is not None=> False
            login(request,u)
            return redirect('/userdashboard')
        else:
            context['errmsg']="Invalid Username or Password!!!"
            return render(request,'login.html',context)
        
    
def user_logout(request):
    logout(request)
    return redirect('/')