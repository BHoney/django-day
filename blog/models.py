from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    '''This will be the general layout for all blog posts
        AUTHOR: The Author of the Posts
        TITLE:  The Title of the Post
        TEXT:   The Post Body
        Created_Date:   Self Explaintory
        Published_Date: Ditto. Note that it might not be the Created_Date
        '''
    author = models.ForeignKey('auth.User') #Grabs the author's ID
    title = models.CharField(max_length=200) #Limits characters to under 200
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title