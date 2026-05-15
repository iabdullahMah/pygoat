from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=16)                                  
    ssn = models.CharField(max_length=9)                          
    api_key = models.CharField(max_length=32)                             
    
    def __str__(self):
        return f"Data for {self.user.username}"
    
                                                               
                                          
    
                                                                
                                  
                                                    
                                
