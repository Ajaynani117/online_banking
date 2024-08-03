from rest_framework import serializers
from users.models import address
class addressSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = address
		fields = ['user_id','address_type','address1','address2','city','zipcode','state','country']
		
        
