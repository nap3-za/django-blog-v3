from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm, UpdatePostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeView(request, *args, **kwargs):

    posts = Post.objects.all().filter(status='published', visibility='public')
    context = {'post': posts.order_by("-pub_date")}
    return render(request, "nodisc/home.html", context)

@login_required
def BlogView(request, *args, **kwargs):

    posts = Post.objects.all().filter(status='published').order_by("-pub_date")
    context = {'post': posts}
    return render(request, "blog/blog.html", context)

@login_required
def PostView(request, pk, *args, **kwargs):

    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, "blog/post.html", context)

@login_required
def AddPostView(request, *args, **kwargs):
    form = AddPostForm(request.POST or None)
    if form.is_valid() and form != None:
        title = form.cleaned_data.get("title")
        page_title = form.cleaned_data.get("page_title")
        content = form.cleaned_data.get("content")
        status = form.cleaned_data.get("status")
        visibility = form.cleaned_data.get("visibility")
        category = form.cleaned_data.get("category")
        l1 = form.cleaned_data.get("l1")
        l2 = form.cleaned_data.get("l2")
        l3 = form.cleaned_data.get("l3")
        l4 = form.cleaned_data.get("l4")
        l5 = form.cleaned_data.get("l5")
        ext_link1 = form.cleaned_data.get("ext_link1")
        ext_link2 = form.cleaned_data.get("ext_link2")
        ext_link3 = form.cleaned_data.get("ext_link3")
        ext_link4 = form.cleaned_data.get("ext_link4")
        ext_link5 = form.cleaned_data.get("ext_link5")

        post = Post.objects.create(
            title = title,
            page_title = page_title,
            content = content,
            status = status,
            visibility = visibility,
            category = category,
            author = request.user,
            ext_link1 = ext_link1,
            ext_link2 = ext_link2,
            ext_link3 = ext_link3,
            ext_link4 = ext_link4,
            ext_link5 = ext_link5,

            l1 = l1,
            l2 = l2,
            l3 = l3,
            l4 = l4,
            l5 = l5,
        )
        post.save()
        print("new post created successsfully")
        return redirect("http://127.0.0.1:8000/blog/posts/my-posts/")
    else:
        print("the form is none")
    context = {'form': AddPostForm}
    return render(request, "blog/add-post.html", context)

@login_required
def DeleteView(request,pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect("http://127.0.0.1:8000/blog/")

@login_required
def UpdatePostView(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    form = UpdatePostForm(request.POST or None)
    if form.is_valid() and form != None:
        title = form.cleaned_data.get("title")
        page_title = form.cleaned_data.get("page_title")
        content = form.cleaned_data.get("content")
        status = form.cleaned_data.get("status")
        visibility = form.cleaned_data.get("visibility")
        category = form.cleaned_data.get("category")
        l1 = form.cleaned_data.get("l1")
        l2 = form.cleaned_data.get("l2")
        l3 = form.cleaned_data.get("l3")
        l4 = form.cleaned_data.get("l4")
        l5 = form.cleaned_data.get("l5")

        ext_link1 = form.cleaned_data.get("ext_link1")
        ext_link2 = form.cleaned_data.get("ext_link2")
        ext_link3 = form.cleaned_data.get("ext_link3")
        ext_link4 = form.cleaned_data.get("ext_link4")
        ext_link5 = form.cleaned_data.get("ext_link5")

        if post.author == request.user:
            post.title = title
            post.page_title = page_title
            post.content = content
            post.status = status
            post.visibility = visibility
            post.category = category

            post.ext_link1 = ext_link1
            post.ext_link2 = ext_link2
            post.ext_link3 = ext_link3
            post.ext_link4 = ext_link4
            post.ext_link5 = ext_link5

            post.l1 = l1
            post.l2 = l2
            post.l3 = l3
            post.l4 = l4
            post.l5 = l5
            post.save()
            print("post updated successsfully") 
            return redirect("http://127.0.0.1:8000/blog/posts/my-posts/")   
    else:
        print("the form is none")

    context = {'post': post}
    return render(request, "blog/edit.html", context)

@login_required
def MyPostsView(request, *args, **kwargs):

    posts = Post.objects.all().filter(author=request.user)
    context = {'post': posts.order_by("-pub_date")}
    return render(request, "blog/my-posts.html", context)

def CategoryView(request, *args, **kwargs):
    posts = Post.objects.all().filter(status='published').order_by("-pub_date")
    context = {
        'tech': posts.filter(category="technology"),
        'computers': posts.filter(category="computers"),
        'general': posts.filter(category="general"),
        }
    return render(request, "blog/category.html", context)
