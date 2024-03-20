import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogItems, BlogCategory
from .forms import SubscriberForm

# Create your views here.



def index(request):
    blog_items_entertainment = BlogItems.objects.filter(category__name='Entertainment')
    blog_items_business = BlogItems.objects.filter(category__name='Business')
    blog_items_tech = BlogItems.objects.filter(category__name='Technology')
    blog_items_latest = BlogItems.objects.filter().order_by('-published_at')
    blog_items = BlogItems.objects.filter()
    categories = BlogCategory.objects.all()


    context={
        'blog_items_entertainment' : blog_items_entertainment,
        'blog_items_business' : blog_items_business,
        'blog_items_tech' : blog_items_tech,
        'blog_items_latest': blog_items_latest,
        'blog_items': blog_items,
        'categories': categories,
    }
    return render(request, 'index.html', context)



def tech_page(request):
    blog_items_tech = BlogItems.objects.filter(category__name='Technology')


    context={
        'blog_items_tech' : blog_items_tech,
    }
    return render(request, 'tech.html' , context)



def entertainment(request):
    blog_items_entertainment = BlogItems.objects.filter(category__name='Entertainment')


    context={
        'blog_items_entertainment' : blog_items_entertainment,
    }
    return render(request, 'entertainment.html' , context)



def business(request):
    blog_items_business = BlogItems.objects.filter(category__name='Business')


    context={
        'blog_items_business' : blog_items_business,
    }
    return render(request, 'business.html' , context)




def crypto(request):
    blog_items_crypto = BlogItems.objects.filter(category__name='Finance / Crypto')


    context={
        'blog_items_crypto' : blog_items_crypto,
    }
    return render(request, 'crypto.html' , context)



def detail(request, pk):
    item = get_object_or_404(BlogItems, pk=pk)
    releated_items = BlogItems.objects.filter().exclude(pk=pk)[0:4]

    return render(request, 'detailed.html', {
        'item': item,
        'releated_items': releated_items
    })



def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            form.save()
            return redirect('/success_page')
        else:
            # Display form errors if it's not valid
            print(form.errors)
            return render(request, 'error_page.html', {'form' : form})
    else:
        form = SubscriberForm()
    return render(request, 'success_page.html', {'form': form})




def subscriber(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            form.save()
            return redirect('/success_page')
        else:
            # Display form errors if it's not valid
            print(form.errors)
            return render(request, 'error_page.html', {'form' : form})
    else:
        form = SubscriberForm()
    return render(request, 'success_page.html', {'form': form})


