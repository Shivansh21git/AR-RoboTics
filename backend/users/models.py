from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    email = models.EmailField(unique=True)          # use email instead
    phone = models.CharField(max_length=15,unique=True,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profiles/',null=True,blank=True)
    role = models.CharField(max_length=20,choices=(("customer", "Customer"),("admin","Admin"),("technician","Technician"),),default="customer")
    
    USERNAME_FIELD = 'email'                        # login with email
    REQUIRED_FIELDS = []

    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.username
    


    


