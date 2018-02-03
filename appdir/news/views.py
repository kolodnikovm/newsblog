from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News
from news.serializers import NewsSerializer


@api_view(['GET'])
def news_detail(request, news_id):
    """ 
        Get news by its id
    """
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
