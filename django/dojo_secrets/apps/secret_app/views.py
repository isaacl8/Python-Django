from django.shortcuts import render, redirect
from .models import Secret, Like
from ..login_app.models import User
from django.db.models import Count

# Create your views here.

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('logins:index')

    user = User.objects.get(pk=user_id)
    list_of_my_likes_ids = Like.objects.filter(user=user).values_list('secret__id', flat=True)
    secrets = Secret.objects.all().annotate(Count("like")).order_by("-created_at").values()[:5]
    for secret in secrets:
        if secret['id'] in list_of_my_likes_ids:
            secret['already_liked'] = True
        else:
            secret['already_liked'] =  False

    context = {
        "user": user,
        "secrets": secrets

    }
    return render(request, 'secret_app/dashboard.html', context)

def popular_secret(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('logins:index')
    user = User.objects.get(pk=user_id)
    list_of_my_likes_ids = Like.objects.filter(user=user).values_list('secret__id', flat=True)
    secrets = Secret.objects.all().annotate(Count("like")).order_by("like__count").values()
    for secret in secrets:
        if secret['id'] in list_of_my_likes_ids:
            secret['already_liked'] = True
        else:
            secret['already_liked'] =  False

    context = {
        "user": user,
        "secrets": secrets

    }



    return render(request, 'secret_app/secrets.html', context)

def create_secret(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('logins:index')
    user = User.objects.get(pk=user_id)

    Secret.objects.create(content=request.POST['content'], user=user)
    return redirect ('secrets:dashboard')

def like(request,id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('logins:index')
    user = User.objects.get(pk=user_id)
    secret = Secret.objects.get(pk=id)

    check_likes = Like.objects.filter(user=user, secret=secret)
    if not check_likes:
        Like.objects.create(user=user, secret=secret)

    return redirect ('secrets:dashboard')

def delete(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('logins:index')
    Secret.objects.get(pk=id).delete()

    return redirect ('secrets:dashboard')
