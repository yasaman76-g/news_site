from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from celery import shared_task
from tags.models import Tag, TaggedItem
from .models import News, Author, Attachments
import os
import urllib.request


@shared_task
def store_news(news_data):
    with transaction.atomic():
        
        for item in news_data:
            author = Author.objects.create(
                name=item["author"].get("name",""),
                url=item["author"].get("url",""),
                avatar=item["author"].get("avatar",""),
            )
            
            news = News.objects.create(
                url=item["url"],
                title=item["title"],
                content_html=item["content_html"],
                summary=item["summary"],
                image=item["image"],
                date_published=item["date_published"],
                author=author
            )
            
            if "attachments" in item:
                for attachment in item["attachments"]:
                    attachments = Attachments.objects.create(
                        mime_type=attachment["mime_type"],
                        title=attachment["title"],
                        duration_in_seconds=attachment["duration_in_seconds"],
                        news=news,
                    ) 
                    
                    
                    
                    attached_file = urllib.request.urlretrieve(attachment["url"])
                    fname = os.path.basename(attachment["url"])

                    with open(attached_file[0],'rb') as fp:
                        attachments.attachment.save(fname, File(fp))
                        attachments.save()
                            
            if "tags" in item:  
                contenttype = ContentType.objects.get_for_model(News)
                for label in item["tags"]:
                    tag = Tag.objects.create(label=label)
                    TaggedItem.objects.create(
                        tag=tag,
                        content_type=contenttype,
                        object_id=news.id,
                        content_object=news
                    )
                
                

