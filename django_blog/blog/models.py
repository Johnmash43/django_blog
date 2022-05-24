from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reader(User):
    '''
    Inheriting formuser gives us access to username, email, password and 
    other Auth-Related attributes
    This way the only need to add phone number
    '''
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email


class Article(models.Model):
    DRAFT = 0
    LIVE = 1
    IN_REVIEW = 2
    INACTIVE = 3

    ARTICLE_STATUS = (
        (DRAFT, "Draft"),
        (LIVE, "Live"),
        (IN_REVIEW,"In Review"),
        (INACTIVE, "Inactive")
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models. TextField()
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    '''
    Status will be used to check whether an article is publicly visible,
    still a draft, scheduled, etc
    We will use the choices Field Options for this
    '''
    Status = models.IntegerField(choices=ARTICLE_STATUS, default=DRAFT)
    ''' 
    To show relationsships with the writer and Category with fields we
    a foreignkey field type.This will show that the field points to 
    another model's Primary key
    syntax:models.ForeignKey(RelatedModelName, on-delete=Value)
    '''
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.image.url


class Reaction(models.Model):
    comment = models.TextField(null=True, blank=True)
    like = models.BooleanField(null=True, blank=True)
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT,null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reaction by: "+ self.reader.email


class Feedback(models.Model):
    message = models.TextField()
    name = models.CharField(null=True, blank=False, max_length=100)
    email = models.EmailField(null=True, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





