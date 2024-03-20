from django.db import models

import cloudinary.models


# Create your models here.


class BlogItems(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='item_images', blank=True, null=True)
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, blank=True, null=True)
    back_category = models.ForeignKey('BackCategory', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)


    class Meta():
        verbose_name_plural = "Blog Posts"
    
    def __str__(self):
        return self.title
    

        


class BlogCategory(models.Model):
    YELLOW = 'bg-yellow-500'
    PINK = 'bg-pink-500'
    ORANGE = 'bg-orange-500'
    BLUE = 'bg-blue-500'
    GREEN = 'bg-green-500'
    RED = 'bg-red-500'
    PURPLE = 'bg-purple-500'
    CATEGORY_COLOR = [
        (YELLOW, 'bg-yellow-500'),
        (PINK, 'bg-pink-500'),
        (ORANGE, 'bg-orange-500'),
        (BLUE, 'bg-blue-500'),
        (GREEN, 'bg-green-500'),
        (RED, 'bg-red-500'),
        (PURPLE, 'bg-purple-500'),
    ]


    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default=YELLOW, choices=CATEGORY_COLOR) # hexadecimal color code
    slug = models.SlugField()


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    



class BackCategory(models.Model):

        name = models.CharField(max_length=50)
        slug = models.SlugField()


        class Meta:
            verbose_name_plural = "BackCategory"


        def __str__(self):
            return self.name
        



class Subscriber(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta():
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.full_name
        





