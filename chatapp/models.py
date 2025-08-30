from django.db import models

# Create your models here.
class Users(models.Model): 
    USER_ROLES=(
        ("USER","user"),
        ("ADMIN","admin")
    )
    id= models.AutoField(auto_created=True, serialize=False, unique=True, primary_key=True)
    username= models.TextField(unique=True, db_index=True)
    password= models.CharField()
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    role = models.CharField(choices=USER_ROLES, default="USER", serialize=False)
    
    def __str__(self):
        return self.username