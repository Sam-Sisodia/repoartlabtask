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
            print(form.errors)
            print("This is User----------------")
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
    return redirect('/dashboard')



def Dashboard(request):
    now=datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:00")
   
    
    print("This is now time --------------", now)
    print("this is now type -------",type(now))

    ll = SendInvoicemail.objects.filter(shedultime=now)
    print(ll)

    for i in ll:
        print(i.shedultime)
   
   
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
    print(now)
    user = request.user
    useremail= user.sendemails
    if useremail > 200 :
        return  render(request, 'sendinvoice.html')
        
    if request.method == "POST": 
        receivermail= request.POST.get("email")
        discription = request.POST.get("discription")
        setdate = request.POST.get("setdate")
        
        print(setdate)
        filename = request.FILES['file']
        
        if not setdate:
            setdate = now
            Sendinvoicemailpdf_email(receivermail,filename,)
            user.sendemails = useremail +1
            user.save()

        else:
            pass
        
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
        print(brandname)
        itemname= request.POST.getlist('itemname')
        qty= request.POST.getlist('quantity')
        price= request.POST.getlist('price')      
        email = request.POST.get("email")
        address = request.POST.get('address')
        print(address)
        invoiceno = request.POST.get('invoiceno')

        mytotal = []
        alltotal = 0
        for i ,j ,k in zip(itemname,qty,price):  
            total = int(j)*int(k)  
            print(total)
            alltotal= total+alltotal
            

            ItemsDetais.objects.create(itemname=i,qty=j,price=k,total=total)
            
            mytotal.append(str(total))

        subtotal = str(alltotal)

        print("This ismy total ",mytotal)


        createpdf(brandname,fromemail,email,address,invoiceno,today,itemname,qty,price,mytotal,subtotal)
        return redirect('/dashboard')






    return  render(request, 'createinvoice.html')



# from reportlab.pdfgen import canvas

# from django.shortcuts import render
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units  import inch
# from reportlab.platypus import SimpleDocTemplate

# from reportlab.platypus.tables import Table,TableStyle,colors

# from datetime import datetime, timedelta



# def createinvoice(request):
#     now=datetime.now()
#     today = now.strftime("%Y-%m-%d")
#     # print("date  ---------- ", today)
    
#     item = ItemRecords.objects.all()

    

   
#     print("today date ",today)
#     if request.method == "POST":
#         date = request.POST.get('date')
        
#         item = ItemRecords.objects.filter(date=date)
#         print("this is ---",item)

        
#         data = []
#         data.append(["Id ", "NAME", "QUANTITY","PRICE", "TOTAL"])

#         for i in   item:
#             row = []
#             id  = i.id
#             name= i.name
#             qty = i.qty
#             price = i.price
#             total = i.total
#             id = i.id
#             print("Id type ------------",type(id))
#             row.append(id)
#             row.append(name)
#             row.append(qty)
#             row.append(price)
#             row.append(total)
#             data.append(row)


#         print("this sis type------",type(data))

#         mydoc = SimpleDocTemplate('table.pdf',pagesize=letter)
#         c_width = [0.4*inch, 1*inch,1*inch,1*inch,1*inch]
#         table = Table(data,rowHeights=40, repeatRows=1,colWidths=c_width)
#         table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen),
#                         ('FONTSIZE',(0,0),(-1,-1),10 )]))

#         elements= []
#         elements.append(table)
#         mydoc.build(elements)
      

#     return  render(request, 'createinvoice.html',locals())
        




