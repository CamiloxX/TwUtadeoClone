from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile, Post
from .forms import UserForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'twitter/newsfeed.html', context)  
def register_view(request):
    context = {}
    return render(request, 'twitter/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def editar_view(request):
    return render(request, 'twitter/editar.html')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    
    if request.user == post.user:
        post.delete()

    return HttpResponseRedirect(reverse('home')) 
