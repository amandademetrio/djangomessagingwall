from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
    if 'logged_in' in request.session and 'user_id' in request.session:
        context = {
            'posted_messages':Message.objects.all(),
            'posted_comments':Comment.objects.all()
        }
        return render(request,'first_app/messaging_wall.html',context)
    else:
        return render(request,'first_app/index.html')

def admin(request):
    if 'logged_in' in request.session and 'user_id' in request.session:
        context = {
            'users':User.objects.all()
        }
        return render(request,'first_app/user_admin.html',context)
    else:
        return redirect('/')

def registration(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request,value,extra_tags='registration_errors')
        return redirect('/')
    
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        new_user.save()
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        request.session['email'] = new_user.email
        request.session['logged_in'] = True
        request.session['user_id'] = new_user.id
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value,extra_tags='login_errors')
        return redirect('/')
    
    else:
        login_user = User.objects.get(email=request.POST['email'])
        request.session['logged_in'] = True
        request.session['user_id'] = login_user.id
        request.session['first_name'] = login_user.first_name
        return redirect('/')

def delete(request,number):
    user_to_be_deleted = User.objects.get(id=number)
    user_to_be_deleted.delete()
    return redirect('/admin')

def postmessage(request):
    errors = Message.objects.message_validator(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request,value,extra_tags='message_errors')
        return redirect('/')
    else:
        new_message = Message.objects.create(message=request.POST['message'],author=User.objects.get(id=request.session['user_id']))
        new_message.save()
        return redirect('/')

def postcomment(request):
    errors = Comment.objects.comment_validator(request.POST)
    
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value,extra_tags='comment_errors')
        return redirect('/')
    else:
        new_comment = Comment.objects.create(comment=request.POST['comment'],message_related=Message.objects.get(id=request.POST['commented_message']),commentator=User.objects.get(id=request.session['user_id']))
        new_comment.save()
        return redirect('/')

def deletemessage(request,number):
    delete_message = Message.objects.get(id=number)
    delete_message.delete()
    return redirect('/')

def deletecomment(request,number):
    delete_comment = Comment.objects.get(id=number)
    delete_comment.delete()
    return redirect('/')