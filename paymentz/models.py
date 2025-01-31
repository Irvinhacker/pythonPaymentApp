from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userdata(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customerid = models.IntegerField(default="")

    def __str__(self):
        return self.user
    
class Prepaid(models.Model):   
    prepaidamount = models.DecimalField(max_digits=10,decimal_places=2)
    datavalidity = models.IntegerField(default="")
    datavalue = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'Amount: {self.prepaidamount}, Validity: {self.datavalidity}, Data Value:{self.datavalue}'

class Postpaid(models.Model):
    postpaidid = models.CharField(default="",max_length=50)
    postpaidamount = models.IntegerField(default="")
    month = models.CharField(default="",max_length=50)
    
    def __str__(self):
        return f'Amount: {self.postpaidamount}, Customer ID: {self.postpaidid}, Month: {self.month}'
    
class Dth(models.Model):
    dthamount = models.DecimalField(max_digits=10,decimal_places=2)
    validity = models.IntegerField(default="")

    def __str__(self):
        return f'Amount: {self.dthamount}, Validity: {self.validity}'

class Wifi(models.Model):
    wifiamount = models.DecimalField(max_digits=10,decimal_places=2)
    validity = models.IntegerField(default="")
    speed = models.IntegerField(default="")

    def __str__(self):
        return f'Amount: {self.wifiamount}, Validity: {self.validity}, Speed: {self.speed}'
    
class Upi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upiid = models.CharField(max_length=50)
    upipassword = models.CharField(max_length=50)
    expirydate = models.DateField()
    
    def __str__(self):
        return f'UPI ID: {self.upiid}'

class Carddetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cardnumber = models.ForeignKey(Userdata,on_delete=models.CASCADE)
    cardname = models.DecimalField(max_digits=10,decimal_places=2)
    cvv = models.IntegerField(default="")
    expirydate = models.DateField()
   
    def __str__(self):
        return f'Card Number: {self.cardnumber}, Card Name: {self.cardname}, CVV: {self.cvv}'