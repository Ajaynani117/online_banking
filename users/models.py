from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default='admin')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100,default=False)
    phone = models.IntegerField(blank=True,default=False)
    status = models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

class address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_type =models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

class User_accounts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account_no = models.IntegerField()
    accounttype = models.CharField()
    FromPast = models.CharField(max_length=100,blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

class User_recipients(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    account_no =models.IntegerField()
    accounttype =models.CharField(max_length=1000,default=False)
    transfer_type =models.CharField(max_length=100)
    ifsc_code =models.CharField(max_length=100)
    recipient_name =models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

class transactions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account =models.ForeignKey(User_accounts,on_delete=models.CASCADE)
    txn_type =models.CharField(max_length=100)
    amount = models.FloatField(default='')
    status =models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

class transfers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipient =models.ForeignKey(User_recipients,on_delete=models.CASCADE)
    user_account =models.ForeignKey(transactions,on_delete=models.CASCADE)
    amount =models.FloatField()
    status =models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)







