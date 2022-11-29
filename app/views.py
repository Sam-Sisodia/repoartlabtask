from django.shortcuts import render ,HttpResponse,redirect

from django.contrib import messages

# Create your views here.
import uuid
from . email  import *
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from django.core.mail import send_mail,EmailMessage
from datetime import datetime, timedelta,date

from .models import *

def RegisterUser(request,):
    form  = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get('email')
            print("This is email, ", email)
            
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()
            user.email_token = str(uuid.uuid4())
            user.save()
            Verification_email(email,user.email_token)
            return redirect('login')
           
        else:
            form  = UserRegisterForm(request.POST)
            return render(request,'register.html',locals())
        
    return render(request,'register.html')


def Login(request):
    if  request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
        user = authenticate(request,email=email,password=password)

        if user is not None:
            auth_login(request, user)
            user=request.user
            if user.is_varified == True:
                return render(request,'dashboard.html')

            else:
                messages.info(request ,"Please Verify Your Accounts ")
        else:
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'login.html')
    return render(request,'login.html')


def logout(request):
    user_logout(request)
    return redirect('/login')


from pdf_mail import sendpdf
def Dashboard(request):
    

    return render(request,'dashboard.html',locals())




def verifyaccount(request,token):
    try:
        obj = User.objects.get(email_token=token )
        obj.is_varified=  True
        obj.save()
        return HttpResponse("Verifie  Suessfully")

    except Exception as e:
        return HttpResponse("<h1> Invalid Token </h1>")


def sendinvoice(request):
    now=datetime.now()
    user = request.user
    useremail= user.sendemails
    if useremail > 200 :
        return  render(request, 'sendinvoice.html')
        
    if request.method == "POST": 
        receivermail= request.POST.get("email")
        discription = request.POST.get("discription")
        setdate = request.POST.get("setdate")
        filename = request.FILES['file']
        
        if not setdate:
            setdate = now
            Sendinvoicemailpdf_email(receivermail,filename,discription)
            user.sendemails = useremail +1
            user.save()
        
        maildetails = SendInvoicemail(fromemial=user.email , tomail=receivermail, shedultime=setdate,
                                  uploadfile=filename) 
        maildetails.save()

        return redirect('/dashboard')

    
    return  render(request, 'sendinvoice.html')



def createinvoice(request):
    user = request.user
    fromemail = user.email
    now=datetime.now()
    today = now.strftime("%Y-%m-%d")
    if request.method == "POST":
        brandname = request.POST.get('brandname')
        itemname= request.POST.getlist('itemname')
        qty= request.POST.getlist('quantity')
        price= request.POST.getlist('price')      
        email = request.POST.get("email")
        address = request.POST.get('address')
        invoiceno = request.POST.get('invoiceno')
        sdate = request.POST.get("datetime")
        if not sdate:
            sdate = now

     
        invoicedata= CreateInvoice.objects.create(brandname=brandname,send_usermail=fromemail,address=address,
                              reciver_usermail=email,invoiceno=invoiceno,sheduledate=sdate,user_id=request.user.id)
        
    
       



        mytotal = []
        alltotal = 0
        for i ,j ,k in zip(itemname,qty,price):  
            total = int(j)*int(k)  
            alltotal= total+alltotal
            ItemsDetais.objects.create(itemname=i,qty=j,price=k,total=total,invoice=invoicedata)
            mytotal.append(str(total))
        subtotal = str(alltotal)
     
        invoice = createpdf(brandname,fromemail,email,address,invoiceno,today,itemname,qty,price,mytotal,subtotal)
        
        



       


   
       
        
        

            
            

       
        


            



        
        if invoicedata.sheduledate == now:
            creatinvoicemail(email,invoice)

       

        return redirect('/dashboard')

    return  render(request, 'createinvoice.html')





    






