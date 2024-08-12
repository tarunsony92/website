import datetime
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    pincode=models.IntegerField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20, null=True)
    regdate=models.DateTimeField(auto_now_add=True)


    def is_exists(self):
        if Customer.objects.filter(emailaddress=self.emailaddress):
            return True
        else:
            False

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(emailaddress=email)



class Login(models.Model):
    userid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    



class Laptop(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    desc =models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='newlaptops/')
    


    @staticmethod
    def get_laptops_by_categoryid(category_id):
        return Laptop.objects.filter(category=category_id)


    @staticmethod
    def get_all_laptops():
        return Laptop.objects.all()
    @staticmethod
    def get_laptop_by_id(laptopid):
        return Laptop.objects.get(id=laptopid)


class Mobile(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    desc =models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image= models.ImageField(upload_to='newmobiles/')


    @staticmethod
    def get_mobiles_by_categoryid(category_id):
        return Mobile.objects.filter(category=category_id)


    @staticmethod
    def get_all_mobiles():
        return Mobile.objects.all()
    @staticmethod
    def get_mobile_by_id(mobileid):
        return Mobile.objects.get(id=mobileid)




class Orders(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    laptop=models.ForeignKey(Laptop,on_delete=models.DO_NOTHING)
    price=models.IntegerField()
    address=models.CharField(max_length=200)
    pincode=models.CharField(max_length=10)
    quantity= models.IntegerField()
    order_date=models.DateField(default=datetime.datetime.today)
    completed= models.BooleanField(default=False)

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    laptop = models.ForeignKey(Laptop, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()


