from django.db import models

class UserRegistration(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=10,default='admin')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=10)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()

# class user_address(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
#     address_type =models.CharField()
#     address1 = models.CharField()
#     address2 = models.CharField()
#     city = models.CharField()
#     zipcode = models.IntegerField()
#     state = models.CharField()
#     country = models.CharField()
#     create_datetime = models.DateTimeField()
#     update_datetime = models.DateTimeField()

# class user_accounts(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
#     accounts_no = models.IntegerField()
#     accounts_type = models.CharField()
#     From_past = models.CharField(blank =True)
#     create_datetime = models.DateTimeField()
#     update_datetime = models.DateTimeField()

# class user_recipients(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
#     recipient_account_no =models.ForeignKey(user_accounts,on_delete=models.CASCADE)
#     recipient_accounttype =models.ForeignKey(user_accounts,on_delete=models.CASCADE)
#     transfer_type =models.CharField()
#     ifsc_code =models.CharField()
#     recipient_name =models.CharField()
#     create_datetime = models.DateTimeField()
#     update_datetime = models.DateTimeField()

# class transcations(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
#     user_accounts_id =models.IntegerField()
#     txn_type =models.CharField()
#     amount = models.FloatField
#     status =models.CharField()
#     create_datetime = models.DateTimeField()
#     update_datetime = models.DateTimeField()

# class transfers(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
#     recipient_id =models.IntegerField()
#     user_accounts_id =models.ForeignKey(transcations,on_delete=models.CASCADE)
#     amount =models.FloatField()
#     status =models.CharField()
#     create_datetime = models.DateTimeField()
#     update_datetime = models.DateTimeField()

