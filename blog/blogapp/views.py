from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def aboutpage(request):
    #return HttpResponse("This is about page")
    return redirect('/contact')

def contactpage(request):

    return HttpResponse("This is contact Page")

def edit(request,rid):
    print("ID to be edited:",rid)
    return HttpResponse("Id to be edited:"+rid)

def delete(request,rid):
    print("ID to be deleted:",rid)
    return HttpResponse("ID to be deleted:"+rid)
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
    return render(request,'dashboard.html')
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

       return HttpResponse("Data Fetched")