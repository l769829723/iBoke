from django.http import HttpResponse
import json

# Custom tool, public method

def shortcut_ajax(data):
    return HttpResponse(json.dumps(data), content_type='application/json')

def isalive(request):
    if request.session.get('userid', '') != '':
        return True
    return False