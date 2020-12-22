from django.db import models


class Worker(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    
    class Meta:
      db_table = 'Worker'
  
class Recruiter(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
       
    class Meta:
      db_table = 'Recruiter'
     
 