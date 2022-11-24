
def createpdf(brandname,fromemail,email,address,invoiceno,today,
                  itemname,qty,price,mytotal,alltotal):


    buffer =BytesIO()

    # name  = datetime.today().strftime(("%Y-%m-%d %H:%M:%S"))
    mycanvas = canvas.Canvas(buffer, pagesize=letter)

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

    pdf = buffer.getvalue()

    return  pdf

