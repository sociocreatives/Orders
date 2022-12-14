from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()

# Create your models here.
class Order(models.Model):
    PIZZA_SIZES=(
        ('SMALL','Small'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
        ('EXTRA_LARGE','Extra_Large'),
    )

    ORDER_STATUSES=(
        ('PENDING','Pending'),
        ('IN_TRANSIT','In_Transit'),
        ('DELIVERED','delivered')
    )

    order_status=models.CharField(max_length=25,choices=ORDER_STATUSES,default=ORDER_STATUSES[0][0])
    size=models.CharField(max_length=25,choices=PIZZA_SIZES,default=PIZZA_SIZES[0][0])
    quantity=models.IntegerField()
    flavour=models.CharField(max_length=40)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    placed_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.flavour} by {self.customer}>"

class About(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=30000)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:  
        verbose_name_plural = 'About Us'

class Faq(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=5000)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:  
        verbose_name_plural = 'FAQs'

class Terms(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=5000)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:  
        verbose_name_plural = 'Terms & Conditions'

class Partners(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=500)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    picture=models.ImageField(default='default.jpg', upload_to='partner_pics', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:  
        verbose_name_plural = 'Partners'