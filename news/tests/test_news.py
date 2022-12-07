from rest_framework import status
from news.tasks import store_news

class TestCreateAuthor:
    def test_if_data_without_attachments_return_201(self):
        data = {
            "id": "1141134320",
            "url": "https://www.npr.org/2022/12/06/1141134320/argentina-cristina-fernandez-de-kirchner-corruption-guilty?utm_medium=JSONFeed&utm_campaign=world",
            "title": "Argentina's vice president is found guilty of corruption",
            "content_html": "<p>A panel sentenced Cristina Fernández de Kirchner to six years in prison and a lifetime ban from holding political office. She will not be jailed while appealing the verdict, which could take years.</p><img src='https://media.npr.org/include/images/tracking/npr-rss-pixel.png?story=1141134320' />",
            "summary": "A panel sentenced Cristina Fernández de Kirchner to six years in prison and a lifetime ban from holding political office. She will not be jailed while appealing the verdict, which could take years.",
            "image": "https://media.npr.org/assets/img/2022/12/06/ap22340686361221-a82250a05a8e129617532fe30aeaae8297f7e62a.jpg",
            "date_published": "2022-12-06T20:01:35-05:00",
            "date_modified": "2022-12-06T20:17:00-05:00",
            "author": {
                "name": "Carrie Kahn",
                "url": "https://www.npr.org/people/2100701/carrie-kahn?utm_medium=JSONFeed&utm_campaign=world",
                "avatar": "https://media.npr.org/assets/img/2022/09/16/carriekahn_vert-4b2724e15f639a4ee755aac154177f2b014b2a68.jpg"
            }
        }
        
        respones = store_news.delay(data)
        
        assert respones.status_code == status.HTTP_201_CREATED
        
    