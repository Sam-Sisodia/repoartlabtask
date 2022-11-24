

def createpdf(brandname,fromemail,email,address,invoiceno,today,
                  itemname,qty,price,mytotal,alltotal):
    mycanvas = canvas.Canvas("media/createdpdf/invoice.pdf", pagesize=letter)

    txtobj = mycanvas.beginText()
    txtobj.setTextOrigin(270,700)
    txtobj.setFont('Times-Roman',25)
    txtobj.textLine(text=brandname)
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(50,650)
    txtobj.setFont('Times-Roman',13)
    txtobj.textLine(text="From: ")
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(100,650)
    txtobj.setFont('Times-Roman',12)
    txtobj.textLine(text=fromemail)
    mycanvas.drawText(txtobj)

    #to

    txtobj.setTextOrigin(50,630)
    txtobj.setFont('Times-Roman',13)
    txtobj.textLine(text="to:")
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(120,630)
    txtobj.setFont('Times-Roman',12)
    txtobj.textLine(text=email)
    mycanvas.drawText(txtobj)

    #adress
        
    txtobj.setTextOrigin(50,610)
    txtobj.setFont('Times-Roman',13)
    txtobj.textLine(text="Address: ")
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(120,610)
    txtobj.setFont('Times-Roman',12)
    txtobj.textLine(text=address)
    mycanvas.drawText(txtobj)



# invoice no 
    txtobj.setTextOrigin(430,630)
    txtobj.setFont('Times-Roman',13)
    txtobj.textLine(text="Invoice :")
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(500,630)
    txtobj.setFont('Times-Roman',12)
    txtobj.textLine(text=invoiceno)
    mycanvas.drawText(txtobj)


#date time 
    txtobj.setTextOrigin(430,600)
    txtobj.setFont('Times-Roman',13)
    txtobj.textLine(text="Date  :    ")
    mycanvas.drawText(txtobj)

    txtobj.setTextOrigin(500,600)
    txtobj.setFont('Times-Roman',12)
    txtobj.textLine(text=today)
    mycanvas.drawText(txtobj)

#table 

    mycanvas.drawRightString(1*inch,7.2*inch,'Items')
    mycanvas.drawRightString(3*inch,7.2*inch,'Qty')
    mycanvas.drawRightString(5*inch,7.2*inch,'Price')
    mycanvas.drawRightString(7*inch,7.2*inch,'total')

    y = 5.8*inch
    
    for i in range(0,1):
        
        for j,k,l,m in zip(itemname,qty,price,mytotal):
            print(i,j,k)
            mycanvas.drawRightString(1*inch,y,j)
            mycanvas.drawRightString(3*inch,y,k)
            mycanvas.drawRightString(5*inch,y,l)
            mycanvas.drawRightString(7*inch,y,m)
    

            y =y+0.3*inch

        mycanvas.drawRightString(7*inch,5*inch,"Total : ")
        mycanvas.drawRightString(7.5*inch,5*inch,alltotal)
        
    mycanvas.save()
    

    return  mycanvas


# def fun(x,y):
#     c = x+y 
#     return c

# jj = fun(2,3)





# def myname(k,l):
    
#     m = k+l+jj
#     return m 


# print(myname(9,1))




















































# from cgitb import text

# from . models import *

# from django.core.mail import send_mail,EmailMessage
# from . models import *

# from django.conf  import settings
# from templates import *
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# # Verification email 

# def Verification_email(email,token):
#     #html_tmp_path = "templates/email.html"
#     try:
#         html_content = render_to_string("emailverify.html",{'token':token})
#         text_content = strip_tags(html_content)

#         email =EmailMultiAlternatives(
#             "Verification mail",text_content,settings.EMAIL_HOST,[email]
#         )
#         email.attach_alternative(html_content,"text/html")
#         email.send()

#         print("Message Sent")
#     except Exception as e:
#         return False
#     return True



# # def Sendinvoicemail_email(rceiveremail):
# #     #html_tmp_path = "templates/email.html

# #     print("==================",rceiveremail)
#     # message = 'Your password '
#     # email_from = settings.EMAIL_HOST
# #     send_mail(subject, message, email_from,[rceiveremail] )

# # from pdf_mail import sendpdf

# # def Sendinvoicemailpdf_email(rceiveremail,userfile):
# #     #html_tmp_path = "templates/email.html
# #     try:
# #         print("==================",rceiveremail)

# #         subject = 'Your account login Password mail'
# #         message = 'Your password '
# #         email_from = settings.EMAIL_HOST
# #         email_message = EmailMessage(subject, message,email_from,[rceiveremail],)
# #         email_message.attach_file([userfile])
# #         email_message.send()
# #     except Exception as e:
# #         return False
# #     return True







# def Sendinvoicemailpdf_email(email,file):
#     try:
#         email =EmailMessage(
#             "Invoice mail ","Your Invoice repoart",settings.EMAIL_HOST,[email],
#         )   
    
#         email.content_subtype="html"
        
#         email.attach(file.name, file.read(),file.content_type)

#         email.send()

#         print("Message Sent")
#     except Exception as e:
#         print(e)
#         print("not send")



# from datetime import datetime, timedelta
    
# def sendsheduletimemail():
#     try:
#         subject = "reminder mail"
#         message = "This is my Task of Verifications "
#         email_from = settings.EMAIL_HOST
#         send_mail(subject,message, email_from,["hello@yopmail.com"])
#         print("verification msg send ")
    


#     now=datetime.now()
#     now = now.strftime("%Y-%m-%d %H:%M:00")
#     try:
#         mail =SendInvoicemail.objects.filter(shedultime=now)
#         print("this is mail =============",mail)
        
#         for i in mail:
#             print(i)

#             email_from = settings.EMAIL_HOST

#             email =EmailMessage(
#                 "Invoice mail ","Your Invoice repoart",email_from, [i.tomail],
#             )   
#             file = i.uploadfile
#             email.content_subtype="html"
            
#             email.attach(file.name, file.read(),file.content_type)

#             email.send()

#         print("Message Sent")
#     except Exception as e:
#         print(e)
#         print("not send")


# def mymail():
#     subject = 'Your account login Password mail'
#     message = 'Your password '
#     email_from = settings.EMAIL_HOST
#     email_message = EmailMessage(subject, message,email_from,["Sajal@yopmail.com"],)
#     email_message.send()


































    
    # now=datetime.now()
    # now = now.strftime("%Y-%m-%d %H:%M:00")
    # today = datetime.today()
    # print("This is today ", today)
    # print("This is now time --------------", now)
    # print("this is now type -------",type(now))

    # ll = SendInvoicemail.objects.filter(shedultime=now)
    # print(ll)
    
































# from reportlab.pdfgen import canvas

# from django.shortcuts import render
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units  import inch
# from reportlab.platypus import SimpleDocTemplate

# from reportlab.platypus.tables import Table,TableStyle,colors

# from datetime import datetime, timedelta



# def createpdf(brandname,fromemail,email,address,invoiceno,today,itemname,qty,price,mytotal,alltotal):

#     mycanvas = canvas.Canvas("invoice.pdf", pagesize=letter)

#     txtobj = mycanvas.beginText()
#     txtobj.setTextOrigin(270,700)
#     txtobj.setFont('Times-Roman',25)
#     txtobj.textLine(text=brandname)
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(50,650)
#     txtobj.setFont('Times-Roman',13)
#     txtobj.textLine(text="From: ")
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(100,650)
#     txtobj.setFont('Times-Roman',12)
#     txtobj.textLine(text=fromemail)
#     mycanvas.drawText(txtobj)


#     #to

#     txtobj.setTextOrigin(50,630)
#     txtobj.setFont('Times-Roman',13)
#     txtobj.textLine(text="to:")
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(120,630)
#     txtobj.setFont('Times-Roman',12)
#     txtobj.textLine(text=email)
#     mycanvas.drawText(txtobj)

#     #adress
        
#     txtobj.setTextOrigin(50,610)
#     txtobj.setFont('Times-Roman',13)
#     txtobj.textLine(text="Address: ")
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(120,610)
#     txtobj.setFont('Times-Roman',12)
#     txtobj.textLine(text=address)
#     mycanvas.drawText(txtobj)



# # invoice no 
#     txtobj.setTextOrigin(430,630)
#     txtobj.setFont('Times-Roman',13)
#     txtobj.textLine(text="Invoice :")
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(500,630)
#     txtobj.setFont('Times-Roman',12)
#     txtobj.textLine(text=invoiceno)
#     mycanvas.drawText(txtobj)


# #date time 
#     txtobj.setTextOrigin(430,600)
#     txtobj.setFont('Times-Roman',13)
#     txtobj.textLine(text="Date  :    ")
#     mycanvas.drawText(txtobj)

#     txtobj.setTextOrigin(500,600)
#     txtobj.setFont('Times-Roman',12)
#     txtobj.textLine(text=today)
#     mycanvas.drawText(txtobj)

# #table 

#     mycanvas.drawRightString(1*inch,7.2*inch,'Items')
#     mycanvas.drawRightString(3*inch,7.2*inch,'Qty')
#     mycanvas.drawRightString(5*inch,7.2*inch,'Price')
#     mycanvas.drawRightString(7*inch,7.2*inch,'total')
    
    
   
#     for j in (0,4):
#         print("THis is J ----------------------------",j)

    
#     y = 5.8*inch
    
#     for i in range(0,1):
        
#         for j,k,l,m in zip(itemname,qty,price,mytotal):
#             print(i,j,k)
#             mycanvas.drawRightString(1*inch,y,j)
#             mycanvas.drawRightString(3*inch,y,k)
#             mycanvas.drawRightString(5*inch,y,l)
#             mycanvas.drawRightString(7*inch,y,m)
    

#             y =y+0.3*inch

#         mycanvas.drawRightString(7*inch,5*inch,"Total : ")
#         mycanvas.drawRightString(7.5*inch,5*inch,alltotal)
        

        
        
        
#         print(y)
        
        
        

#     mycanvas.save()

    




    























# class  sendinvoicemail(email,filename,discription):

#     email =EmailMessage(
#         "Invoice Mail",discription,settings.EMAIL_HOST,[email])
#     email.content_subtype="html"
    
#     email.attach(filename.name, filename.read(),filename.content_type)

#     email.send()
#     print("done")












   
#     print("today date ",today)
#     if request.method == "POST":
#         date = request.POST.get('date')
#         print(type(date))
#         print("Post Date ",date)
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
#         c_width = [1*inch]
#         table = Table(data,rowHeights=40, repeatRows=1,colWidths=c_width)
#         table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen)]))

#         elements= []
#         elements.append(table)
#         mydoc.build(elements)
#         print("Done hi bro")
        



        # now = datetime.now() 
        # tt = str(now)

        # print("This ====================", type(str(now)))

        # subject = request.POST.get("subject")
        # print(subject)
        # email= request.POST.get("email")
        # print(email)
        # print("This is s=======================",settings.EMAIL_HOST_USER )

        







    
    
# def create(x,y):
    # mycanvas = canvas.Canvas("invoice.pdf", pagesize=letter)

    # txtobj = mycanvas.beginText()
    # txtobj.setTextOrigin(250,700)
    # txtobj.setFont('Times-Roman',30)
    # txtobj.textLine(text="Invoice")
    # mycanvas.drawText(txtobj)

    # txtobj.setTextOrigin(100,600)
    # txtobj.setFont('Times-Roman',15)
    # txtobj.textLine(text="From: ")
    # mycanvas.drawText(txtobj)


    # txtobj.setTextOrigin(100,570)   
    # txtobj.setFont('Times-Roman',15)     
    # txtobj.textLine(text=x)
    # mycanvas.drawText(txtobj)


    # txtobj.setTextOrigin(400,600)
    # txtobj.setFont('Times-Roman',15)
    # txtobj.textLine(text="DATE : ")
    # mycanvas.drawText(txtobj)





    # txtobj.setTextOrigin(400,570)   #user date cordinate
    # txtobj.setFont('Times-Roman',15)     
    # txtobj.textLine(text=y)
    # mycanvas.drawText(txtobj)




    # mycanvas.save()
    





# c.drawString(200,700,"<b1> hello SAJAL<b1>")
# c.save()
# print("Ho gyi") 





# listo = [[1,3,8], [88,88,8],[2,33,99]]

# for  i , j , k in listo:
#   print(i,j,k)














# def sendinvoice(request):
#     now=datetime.now()
#     print("This sis now  time -------------",now)
#     print(now)
#     user = request.user
#     useremail= user.sendemails
#     #emailcount =User.objects.all()
#     if useremail >10:
#         return  render(request, 'sendinvoice.html')
        
#     if request.method == "POST": 
#         receivermail= request.POST.get("email")
#         discription = request.POST.get("discription")
#         setdate = request.POST.get("setdate")
#         filename = request.FILES['file']
        
#         if not setdate:
#             setdate = now
        
#         print("THisis set Date============-----------",setdate)

        
#         email =EmailMessage(
#             "Invoice Mail",discription,settings.EMAIL_HOST,[receivermail])
#         email.content_subtype="html"
        
#         email.attach(filename.name, filename.read(),filename.content_type)
        
    
   
        
#         user.sendemails = useremail +1
#         user.save()
#         maildetails = SendInvoicemail(fromemial=user.email , tomail=receivermail, shedultime=setdate) 
#         maildetails.save()
#         email.send()


#         return redirect('/dashboard')

    
#     return  render(request, 'sendinvoice.html')