from django.shortcuts import render, redirect
from userinfo.models import Info

# Create your views here.

def index(request):
    user = request.session.get('userid', 'null')
    info = Info.objects.all()
    # all_user = UserAuth.objects.all()
    #context = {'blogs':blogs}
    if user != 'null':
        # user = UserAuth.objects.get(userid = user)
        #userinfo = UserInfo.objects.get(user__userid = user)
        #context ['user']= userinfo
        pass
    return render(request, 'myblog/index.html') 
    
    
    


