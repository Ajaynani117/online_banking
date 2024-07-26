"""
URL configuration for online_banking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import Userregistrations

registration = Userregistrations()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registration.registrations),
    path('login/',registration.login),
    path('dashboard/',registration.dashboard),
    path('deposite/',registration.deposite),
    path('withdraw/',registration.withdraw),
    path('accountSummary/',registration.AccountSummary),
    path('ministatement/',registration.Ministatement),
    path('detailedStatement/',registration.DetailedStatement),
    path('addreceipient/',registration.Addreceipient),
    path('deleterecipient/',registration.Deletereceipient),
    path('transferfunds/',registration.TransferFunds),
    path('transferhistory/',registration.TranferHistory),
    path('createaccount/',registration.createAccount),
    path('saveaddress/',registration.Adduseraddress),
    # path('getaddresses/',registration.getuseraddresses),
    # path('updataddress/',registration.Updateuseraddress),
    # path('delete/useraddress',registration.DeleteUseraddress)
]
