from django.shortcuts import render, redirect
from myblog.toolbox import shortcut_ajax, isalive
# from validation.models import UserAuth
from userinfo.models import Info, Blog, Tag
import traceback

# Create your views here.
def userinfo(request):
    if not isalive(request):return redirect('/myblog/userauth/login')
    info = Info.objects.get(user__userid=request.session.get('userid'))
    blogs = info.blogs.all().order_by('-blog_publish_date')
    context = {'user': info.name, 'blogs':blogs, 'words':info.name.promisewords}
    return render(request, 'myblog/userinfo.html', context)
    
# User publish interface
def publish(request):
    if not isalive(request):return redirect('/myblog/userauth/login')
    if request.is_ajax():
        post = request.POST
        if len(post['title']) >= 1 and len(post['content']) >= 15:
            blog = Blog.objects.create(blog_title=post.get('title'), blog_body = post.get('content'))
            info = Info.objects.get(user__userid = request.session['userid'])
            info.blogs.add(blog)
            if post.get('tags', '') != '':
                for tag in post.get('tags').split(','):
                    t = Tag.objects.create(name=tag)
                    blog.blog_tags.add(t)
                    
            return shortcut_ajax({'addCode': 0})
        else:
            return shortcut_ajax({'addCode': 1})
    else:
        return render(request, 'userinfo/userinfo_add.html')
    
def update(request):
    if not isalive(request):return redirect('/myblog/userauth/login')
    if request.is_ajax():
        post = request.POST
        if len(post['title']) >= 1 and len(post['content']) >= 15:
            info = Info.objects.get(user__userid = request.session['userid'])
            blog = info.blogs.get(id=post['blogid'])
            blog.blog_title = post['title']
            blog.blog_body = post['content']
            blog.save()
            info.blogs.get(pk=17).blog_tags.all().delete()
            if post.get('tags', '') != '':
                for tag in post.get('tags').split(','):
                    t = Tag.objects.create(name=tag)
                    blog.blog_tags.add(t)
                    
            return shortcut_ajax({'updateCode': 0})
        else:
            return shortcut_ajax({'updateCode': 1})
    else:
        return render(request, 'userinfo/userinfo_edit.html')

# User delete interface
def delete(request):
    if not isalive(request):return redirect('/myblog/userauth/login')
    if request.is_ajax():
        try:
            blogid = request.POST['blogid']
            info = Info.objects.get(user__userid=request.session.get('userid'))
            if info.blogs.get(id=blogid).delete():
                return shortcut_ajax({'delCode':0})
            else:
                raise KeyError
        except:
            print(traceback.format_exc())
            return shortcut_ajax({'delCode':1})
    else:
        return render(request, 'userinfo/userinfo_add.html')