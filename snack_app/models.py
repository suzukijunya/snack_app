import re
from django.db import models
from django.core.validators import ValidationError

def number_only(value):
    if (re.match(r'^[0-9]*$', value) == None):
        raise ValidationError(
            '%(value)s is not Number!', \
            params={'value': value},
        )

class Friend(models.Model):
    name = models.CharField(max_length=100, \
        validators=[number_only])
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'

class Store(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    business_hours = models.TimeField(auto_now=False, auto_now_add=False)
    store_type = models.CharField(max_length=5)
     
    def __str__(self):
        return '<Store:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'

class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '<Message:id=' + str(self.id) + ', ' + \
            self.title + '(' + str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)

# Create your models here.
