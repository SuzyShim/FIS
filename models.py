from django.db import models

# Create your models here.
class Crowdfunding_InitiatorInfo(models.Model):
    initiatorInfo_id = models.CharField(max_length=128, primary_key=True)
    initiatorInfo_credit = models.IntegerField(default=0)
    initiatorInfo_companyAddress = models.CharField(max_length=128)
    initiatorInfo_telephone = models.CharField(max_length=128)
    initiatorInfo_bankAccount = models.CharField(max_length=128)
    initiatorInfo_userID = models.CharField(max_length=128)
     
    def __str__(self):
        return self.initiatorInfo_id
         
class Crowdfunding_project(models.Model):
    project_id = models.CharField(max_length=128, primary_key=True)
    project_type = models.CharField(max_length=128)
    project_name = models.IntegerField(default=0)
    project_details = models.CharField(max_length=128)
    project_deadline = models.CharField(max_length=128)
    project_NumOfFollowers = models.IntegerField(default=0)
    project_feedback = models.CharField(max_length=128)
    project_initiatorInfoID=models.CharField(max_length=128)
    project_initiatorInfoID = models.ForeignKey(Crowdfunding_InitiatorInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_id
    
class Crowdfunding_user(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True)
    user_address = models.CharField(max_length=128)
    user_telephone = models.IntegerField(default=0)
    user_supportProjectID = models.CharField(max_length=128)
    user_bankAccount = models.CharField(max_length=128)
    user_orderNumber = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user_id

