from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255,null=True,blank=True)
    avatar = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class News(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content_html = models.TextField()
    summary = models.TextField()
    image = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="news")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"
        
 
    
class Attachments(models.Model):
    url = models.CharField(max_length=255)
    attachment = models.FileField(upload_to="attachments",null=True,blank=True)
    mime_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    duration_in_seconds = models.CharField(max_length=255)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="attachments")
    
    def __str__(self):
        return self.title
    
