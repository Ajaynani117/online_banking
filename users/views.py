from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404,response
import json
from .models import * 
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime




class Userregistrations:
    @csrf_exempt
    def registrations(self,request):
        try:
            if request.method == 'POST':
                request_body = json.loads(request.body)
                user = User(user_name=request_body.get('userName'),
                                    password =request_body.get('password'),
                                    first_name=request_body.get('firstName'),
                                    last_name=request_body.get('lastName'),
                                    email=request_body.get('email'),
                                    phone=request_body.get('phone'),
                                    status = 'success',
                                    create_datetime=datetime.now(),
                                    update_datetime=datetime.now()) 
                user.save()
                return JsonResponse({"status": "Success","code": "OLB_S003"})
        except Exception as exc:
            print(exc)
            return JsonResponse({"invalid input"})    
    
    @csrf_exempt
    def login(self,request):
        
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
                user_deatils = User.objects.filter(user_name = request_body.get("username"),
                                      password = request_body.get("password"))
                return HttpResponse(user_deatils,{ "status": "Success","message": "Login Success","code": "OLB_S000"})
      
        except Exception as exc:
            print('user creditinals error ,Enter the valid input')       


    @csrf_exempt
    def dashboard(self,request):
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
                response = []
                user_accounts_info = User_accounts.objects.filter(user_id=request_body['user_id'])
                for user_account in user_accounts_info:
                    user_output = {
                        "account_id": user_account.id,
                        "account_no": user_account.account_no,
                        "accounttype": user_account.accounttype
                    }
                user_account_transcations=transactions.objects.filter(user_id=request_body['user_id'],
                                                                      account_id=user_account.id)
                Total = 0
                for user_account_transaction in user_account_transcations:
                    if user_account_transaction.txn_type == "debit":
                        Total = Total+user_account_transaction.amount
                    else:
                        Total = Total-user_account_transaction.amount
                user_output["amount"] = Total
                response.append(user_output)
            return HttpResponse(response)

        except Exception as exc:
            print(exc)
            raise Http404(({"error":"Internal Server Error"}))
            print({"error":"Internal Server Error"})
            
    @csrf_exempt
    def deposite(self,request):
        try:
            print('first')
            if request.method == 'POST':
                request_body = json.loads(request.body)
                print(request_body)
                deposited = transactions(user_id=request_body.get('user_id'),
                                         account_id=request_body.get('account_id'),
                                         txn_type ='debit',    
                                         amount=request_body.get('amount'),
                                         status='success'  ,
                                         create_datetime=datetime.now(),
                                         update_datetime=datetime.now())                                        
                
                deposited.save()

            return HttpResponse([{"status":"success","code":"OLB_S004"}])
    
        except Exception as error:
            print(error)
            print("error")


    @csrf_exempt
    def withdraw(self,request):
        try:
            if request.method =='POST':
                request_body = json.loads(request.body)
                print(request_body)
                cash_withdrawl = transactions(user_id=request_body.get('user_id'),
                                         account_id=request_body.get('account_id'),
                                         txn_type ='credit',    
                                         amount=request_body.get('amount'),
                                         status='success'  ,
                                         create_datetime=datetime.now(),
                                         update_datetime=datetime.now())                                        
                
                cash_withdrawl.save()                                               

                print(cash_withdrawl)
            return HttpResponse([{"status":"success","code":"OLB_S005"}])
        
        except Exception as error:
            print(error)
            print('invalid entry ')
    
    @csrf_exempt
    def AccountSummary(self,request):
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
                print(request_body)

                user_accounts_info = User_accounts.objects.filter(user_id=request_body['user_id'],
                                                                  id = request_body['account_id'])
        
                for user_account in user_accounts_info:
                    user_output = {
                        "account_id": user_account.id,
                        "account_no": user_account.account_no,
                        "account_type":user_account.accounttype
                    }
                accountsummary = transactions.objects.filter(user_id=request_body.get("user_id"),
                                                             account_id=request_body.get("account_id")
                                                             )
        
                total_debit=0
                total_credit =0
                net_total =0
                for summary in accountsummary:
                    if summary.txn_type == "debit":
                        total_debit = total_debit + summary.amount
                    elif summary.txn_type == "credit":
                        total_credit = total_credit + summary.amount

                net_total=total_debit-total_credit

                user_output["total_debit"] = total_debit
                user_output['total_credit'] = total_credit
                user_output['net_total'] = net_total

            
            return HttpResponse(json.dumps(user_output))


        except Exception as exc:
    
            print("raised an issue")        

        
    @csrf_exempt
    def Ministatement(self,request):
        
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
                print(request_body)

                statement_info = transactions.objects.filter(user_id = request_body['user_id'],
                                                            account_id=request_body['account_id'],
                                                            ).order_by('user_id')[:10:1]
                print(statement_info)
                response =[]
                for min in statement_info:
                    print(min)
                    print(response)
                    output = {
                        "txn_id":min.id,
                        "amount":min.amount,
                        "txn_type":min.txn_type,
                        "date":min.create_datetime,
                        "user_id": request_body['user_id']
                     }   
                    print(output)
                         
                    response.append(output)
                    print(response)        
                     
            return HttpResponse((response))
        except Exception as exe:
             print(exe)
             print("Inside Exception block ")

    @csrf_exempt
    def DetailedStatement(self,request):
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
            user_info = User_accounts.objects.filter(user_id = request_body['user_id'],
                                                            account_no =request_body['account_no']
                                                            )
            transaction_info = transactions.objects.filter(user_id = request_body['user_id'],
                                                           )
            response=[]
            for info in transaction_info:
             out_info = {
                 "txn_id":info.id,
                 "amount":info.amount,
                 "txn_type":info.txn_type,
                 "date":info.create_datetime

             }
                
             response.append(out_info)
             return HttpResponse((response))
        except Exception as exec:
            print("exception block")


    @csrf_exempt
    def Addreceipient(self,request):

        try:

         if request.method == 'POST':
            request_body = json.loads(request.body)
            print(request_body)

            addrecep = User(id = request_body.get('id')) 
            addrecep_info = User_recipients(user_id=request_body.get('user_id'),
                                            recipient_name=request_body.get('recipient_name'),
                                            account_no=request_body.get('account_no'),
                                            accounttype=request_body.get('accounttype'),
                                            transfer_type=request_body.get('transfer_type'),
                                            ifsc_code=request_body.get('ifsc_code'))
            addrecep.save()
            addrecep_info.save()
            return HttpResponse([{"status":"success","code":"OLB_S006"}])

        except Exception as exc :   

            print("exception block")

            print(exc)  

    @csrf_exempt
    def Deletereceipient(self,request):
        try:
            if request.method == 'GET':
                request_body = json.loads(request.body)
                print(request_body)

                del_user_info = User_recipients.objects.filter(id = request_body.get('recipient_id'),
                                                               user_id = request_body.get('user_id')).delete()
                print("its deleted")

                return HttpResponse([{"status":"success","code":"OLB_S007"}])
            
        except Exception as exe:

            print("expcetion block")    

    @csrf_exempt
    def TransferFunds(self,request):
        try:
            if request.method == 'POST':
                request_body = json.loads(request.body)
                print(request_body)

                user_recip_info=User_recipients(user_id=request_body.get('user_id'))

                print("first")
                transfer_info = transfers(user_id = request_body.get('user_id'),
                                          recipient_id=request_body.get('recipient_id'),
                                          user_account_id=request_body.get('user_account_id'),
                                          amount=request_body.get('amount'))
                print("second")
                transfer_info.save()
                print("third")
                print(user_recip_info)
                print(transfer_info)
                return HttpResponse([{"status":"success","code":"OLB_S008"}])
            
        except Exception as exe:

            print("Inside Exception block")    

    
    @csrf_exempt
    def TranferHistory(self,request):
        try :
            if request.method == 'GET':
                request_body = json.loads(request.body)
                print(request_body)
                
                transfer_history = transfers.objects.filter(user_id = request_body.get('user_id')
                                                            )
                
                transfer_name = User_recipients.objects.filter(user_id = request_body.get('user_id'))
                
                response=[]
            
                print('outside for loop')

                for info in transfer_history:
                       
                        output = {
                          "amount": info.amount,
                          "status": "completed",
                          "transfr_date" :info.update_datetime
                             }
                for info_name in transfer_name:
                        output_name = {
                            "recipient_name":info_name.recipient_name
                        }
             
                response.append(output_name)
                response.append(output)

                print(response)

                return HttpResponse((response))
                 
        except Exception as exe:
            print("error block ")

    @csrf_exempt
    def createAccount(self,request):
        try:
            if request.method == 'POST':
                request_body = json.loads(request.body)
                print(request_body)
            account_info = User(user_name = request_body.get("user_name"),
                                first_name = request_body.get("firstName"),
                                last_name = request_body.get("lastName"),
                                email_id = request_body.get("emailid"),
                                phone = request_body.get("phone")
                                    )
            account_info.save()
            # acc_info = User_accounts(accounttype = request_body.get("account_type"))
                                                        
            # acc_info.save()
            

            return HttpResponse([{"status":"success","code":"OLB_S008"}])
        except:
            print("Expecation block")
    
    @csrf_exempt
    def Adduseraddress(self,request):
        try:
            if request.method == 'POST':
                request_body = json.loads(request.body)
                print(request_body)
            
            # add_user_id = User(id = request_body.get("user_id"))
            # print(add_user_id)
            print('middle')
            add_user_address_info = address(user_id= request_body.get("user_id"),
                                        address_type=request_body.get("address_type"),
                                        address1 = request_body.get("address1"),
                                        address2=request_body.get("address2"),
                                        city = request_body.get("city"),
                                        zipcode = request_body.get("zipcode"),
                                        state = request_body.get("state"),
                                        country=request_body.get("country"))
                                        # create_datetime=,
                                        # update_datetime=)
            add_user_address_info.save()
            print('outrside')

            return HttpResponse([{"status":"success","code":"OLB_S000"}])
        except Exception as exc:
            print(exc)
            print({
                  "status": "Failed",
                  "message": "user_id not availble",
                  "code": "OLB_E002"
                   })
            
    # @csrf_exempt
    # def getuseraddresses(self,request):
    #     try:
    #         if request.method == 'GET':
    #          request_body = json.loads(request.body)

    #          addres_info = address.objects.filter(user_id = request_body.get("user_id"),
    #                                                 address_type=request_body.get("address_type"),
    #                                                 address1 = request_body.get("addres1"),
    #                                                 address2=request_body.get("address2"),
    #                                                 city = request_body.get("city"),
    #                                                 zipcode = request_body.get("zipcode"),
    #                                                 state = request_body.get("state"),
    #                                                 country=request_body.get("country")
    #                                               )
    #          return HttpResponse(addres_info)
            
    #     except:
    #         print("in expecation block")

    # @csrf_exempt
    # def Updateuseraddress(self,request):
    #     try:
    #         if request.method == 'PUT':
    #             request_body = json.loads(request.body)

    #         update_address = address(id= request_body.get("user_id"),
    #                                     address_type=request_body.get("address_type"),
    #                                     address1 = request_body.get("addres1"),
    #                                     address2=request_body.get("address2"),
    #                                     city = request_body.get("city"),
    #                                     zipcode = request_body.get("zipcode"),
    #                                     state = request_body.get("state"),
    #                                     country=request_body.get("country"))

    #         update_address.save()
            
    #         return HttpResponse([{"status":"success","code":"OLB_S009"}])
        
    #     except:
    #         print("in exception block")
    
    # @csrf_exempt
    # def DeleteUseraddress(self,request):
    #     try:
    #         if request.method == 'DELETE':
    #             request_body = json.loads(request.body)



    #         delete_address = address.objects.filter(user_id = request_body.get('user_id'),
    #                                                  id = request_body.get('address_id'))

    #         delete_address.delete()

    #         return HttpResponse([{"status":"success","code":"OLB_S018"}])
    #     except:
    #         print("in exception block")

        














