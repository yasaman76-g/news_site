from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .tasks import store_news
import urllib.request, json

class NewsApi(APIView):
    def post(self,request):
        url = "https://feeds.npr.org/1004/feed.json"
        response = urllib.request.urlopen(url)
        news = json.loads(response.read())["items"]
        
        sorted_news = sorted(news, key=lambda news: news['date_published'])
        last_five_news = sorted_news[-5:]
        
        #store news in database
        store_news.delay(last_five_news)
        
        
        return Response(data=last_five_news)
