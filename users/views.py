from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def userregistration(request):
    try:
        if request.method == 'POST':
            print (request)
            request.body = json.loads(request.body)
            print(request.body)
            userregistration = request.body()
            print(userregistration)
            response = userregistration.objectmap(object.map, username='username',
                                  password ='password',
                                  first_name='frist name',
                                  last_name='lastname',
                                  email_id='emailid',
                                  phoneno='phoneno',
                                  status = 'staus',
                                  create_datetime='createdatetime',
                                  update_datetime='updatedatetime')  
            return JsonResponse({"status": "Success","code": "OLB_S003"})
    except:
        print("500")    