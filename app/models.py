from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyManager(BaseUserManager):
    def create_user(self, email,password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password =password
        )
        user.set_password(password)
    
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username =models.CharField(max_length=25,null=True,blank=True,default=None)
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now=True)
    is_varified  = models.BooleanField(default=False)
    email_token = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    sendemails = models.IntegerField(default=0)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS= []  
    
    objects = MyManager()
    
    def  __str__(self):
        return self.email


    def get_fullname(self):
        return self.fullname

    def  get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_active(self):
        return self.active
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    




class CreateInvoice(models.Model):
    brandname =models.CharField(max_length=100,null=True,blank=True)
    sheduledate= models.DateTimeField(null=True,blank=True,)
    send_usermail = models.EmailField()
    reciver_usermail = models.EmailField() 
    invoiceno = models.IntegerField()
    uploadfile = models.FileField(upload_to="create",null=True,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="Invoice_User" , null = True, blank=True)
 

class ItemsDetais(models.Model):
    itemname =models.CharField(max_length=100,null=True,blank=True)
    qty    =  models.CharField(max_length=100,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    total = models.CharField(max_length=100,null=True,blank=True)
    invoice = models.ForeignKey(CreateInvoice,on_delete=models.CASCADE , related_name="CreateInvoice_item" , null = True, blank=True) 


class SendInvoicemail(models.Model):
    fromemial = models.EmailField()
    tomail = models.EmailField()
    shedultime = models.DateTimeField(null=True, blank=True)
    uploadfile = models.FileField(upload_to="pdf",null=True,default=None)
    



    


































# 1034923421644-k7h33dc3iltluc9joadqoif11t2jrkmu.apps.googleusercontent.com
#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