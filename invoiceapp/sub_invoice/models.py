from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser




class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError('Username is required!!')
        user=self.model(username=username,**extra_fields )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(username,password,**extra_field)

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username= models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    objects = UserManager()

class Invoices(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=200)
    date = models.DateField()

class Items(models.Model):
    invoices = models.ForeignKey(Invoices, on_delete=models.CASCADE, related_name="items", blank=True, null=True)
    desc = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()


