from django.http import HttpResponse
from django.shortcuts import render, redirect
from validation.models import UserAuth
from userinfo.models import Info, Name

import json

# Create your views here.

# Login method
def login(request):
    if request.is_ajax():
        try:
            post = request.POST
            user = UserAuth.objects.get(username = post['username'])
            if user.password == encrypt_md5(post['password']):
                request.session['userid'] = user.userid
                request.session.set_expiry(900)
                return shortcut_ajax({'loginCode':0, 'redirection':'/myblog/userinfo'})
            else:
                return shortcut_ajax({'loginCode':1})
        except UserAuth.DoesNotExist:
            return shortcut_ajax({'loginCode':2})
    else:
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/myblog/userinfo')
        return render(request, 'myblog/userauth.html')

# Register method
def register(request):
    if request.is_ajax():
        post = request.POST
        try:
            UserAuth.objects.get(username = post['username'])
            return shortcut_ajax({'result': 1})
        except UserAuth.DoesNotExist:
            if (post['firstname'] != '') and (post['lastname'] != ''):
                if username_policy_check(post['username']) and password_policy_check(post['password']):
                    user = UserAuth(
                                    username = post['username'],
                                    password = encrypt_md5(post['password']),
                                    userid = get_last_uid()            
                    )
                    user.save()
                    name = Name(firstname=post['firstname'], lastname=post['lastname'])
                    name.save()
                    info = Info(name=name, user=user)
                    info.save()
                    return shortcut_ajax({'result': 0})
                else:
                    return shortcut_ajax({'result': 2})
            else:
                return shortcut_ajax({'result': 3})
    else:
        return render(request, 'myblog/userauth-register.html')
        
def logoff(request):
    request.session.flush()
    print(dir(request.META))
    return redirect(request.META.get('HTTP_REFERER', '/myblog'))

# ================================================================================

# Check username avilable
def username_policy_check(username):
    if username != '':
        import re
        pattern = re.compile(r'[\S]{5,}[@][\w]{2,}[.][\w]{2,}')
        if pattern.search(username):
            return True
    
    return False

# Check password avilable
def password_policy_check(password):
    import re
    if len(password) >= 7:
        if re.search(r'\d', password) and re.search(r'[a-zA-Z]', password):
            return True
        elif re.search(r'\d', password) and re.search(r'[\W]', password):
            return True
        elif re.search(r'[a-zA-Z]', password) and re.search(r'[\W]', password):
            return True
    
    return False

# get userid
def get_last_uid():
    user = UserAuth.objects.all().order_by('-id')
    if user:
        newid = user[0].userid + 1
    else:
        newid = 10000
    return newid

# ======================================================================
# Encrypt password for safety
def encrypt_md5(string):
    import hashlib
    return hashlib.md5(string.encode('utf-8')).hexdigest()

# ======================================================================
def shortcut_ajax(data):
    return HttpResponse(json.dumps(data), content_type='application/json')
    