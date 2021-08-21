from blog.forms import ContactForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Post


def index(request):
    contact_form = ContactForm()
    posts = Post.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            record = form.save()
            record.user = request.user
            record.save()
            messages.info(request, 'Your submission was successful!')
            return redirect('blog')

    context = {
        "posts" : posts,
        "contact_form": contact_form,
    }

    return render(request, "blog/index.html", context)