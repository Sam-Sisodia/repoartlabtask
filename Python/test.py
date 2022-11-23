








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