from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Blog
import datetime
# Create your views here.
def aboutpage(request):
    #return HttpResponse("This is about page")
    return redirect('/contact')

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
    return render(request,'home.html')
def user_dashboard(request):
    b=Blog.objects.all() #select * from blogapp_blog
    context={}
    context['blogs']=b
    return render(request,'dashboard.html',context)


def create_blog(request):
    #print("Method Type:",request.method)
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

       b=Blog.objects.create(title=btitle,detail=bdet,cat=bcat,created_at=datetime.datetime.now())
       b.save()

       #return HttpResponse("Data Inserted Successfully")
       return redirect('/userdashboard')
