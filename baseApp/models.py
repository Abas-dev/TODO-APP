from django.db import models
from django.contrib.auth.models import User

# creation of user table
class UserDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName

# creating of todo content table
class TodoTable(models.Model):
    userName = models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True,null=True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




