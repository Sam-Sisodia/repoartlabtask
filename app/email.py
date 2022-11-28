from cgitb import text

from . models import *

from django.core.mail import send_mail,EmailMessage
from . models import *

from django.conf  import settings
from templates import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#pdf  create


from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units  import inch


from datetime import datetime, timedelta



def Verification_email(email,token):
    try:
        html_content = render_to_string("emailverify.html",{'token':token})
        text_content = strip_tags(html_content)

        email =EmailMultiAlternatives(
            "Verification mail",text_content,settings.EMAIL_HOST,[email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        print("Message Sent")
    except Exception as e:
        return False
    return True

def Sendinvoicemailpdf_email(email,file,discription):
    try:
        email =EmailMessage(
            "Invoice mail ",discription,settings.EMAIL_HOST,[email],
        )   
    
        email.content_subtype="html"
        
        email.attach(file.name, file.read(),file.content_type)

        email.send()

        print("Message Sent")
    except Exception as e:
        print(e)
        print("not send")




#cron job



def sendsheduletimemail():
    now=datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:00")
    try:
        mail =SendInvoicemail.objects.filter(shedultime=now)
        for i in mail:
            tomail = i.tomail
            print(tomail)
            file = i.uploadfile

            email_from = settings.EMAIL_HOST

            email =EmailMessage(
                "Invoice mail ","Your Invoice  details",email_from, [tomail] )   
            file = i.uploadfile
            #email.content_subtype="html"
           
            
            email.attach(file.name, file.read())

            email.send()

            print("Message Sent")
    except Exception as e:
        print(e)
        print("not send")




from django.shortcuts import render ,HttpResponse,redirect
from io import BytesIO
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas



def createpdf(brandname,fromemail,email,address,invoiceno,today,
                  itemname,qty,price,mytotal,alltotal):
   

    buffer =BytesIO()

    # name  = datetime.today().strftime(("%Y-%m-%d %H:%M:%S"))
    mycanvas = canvas.Canvas(buffer, pagesize=A4)
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

    mycanvas.showPage()
    mycanvas.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
        
   



def creatinvoicemail(email,invoice):
    try:
        email =EmailMessage(
            "Invoice mail ","hello",settings.EMAIL_HOST,[email],
        )  
        pdf = invoice
        email.attach('generated.pdf', pdf, 'application/pdf') 
       

        email.send()

        print("Message Sent")

    except Exception as e:
        print(e)
        print("not send")


def creatinvoicemailcron():
    pass






            


    




    




















