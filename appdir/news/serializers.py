from rest_framework import serializers
from users.models import User
from news.models import News, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name')


class NewsSerializer(serializers.ModelSerializer):


    class Meta:
        model = News
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture', 'additional_pictures')


class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_joined', 'author')
