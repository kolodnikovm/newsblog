from rest_framework import serializers

from news.models import Author, Category, News, Tag, PublishedNews
from news.utilfuncs import RecursiveField
from users.models import User


class RecursiveCategorySerializer(serializers.ModelSerializer):
    subcategories = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('name', 'parent_id', 'subcategories')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PublishedNewsSerializer(serializers.ModelSerializer):
    category = RecursiveCategorySerializer()

    class Meta:
        model = PublishedNews
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture')


class NewsSerializer(serializers.ModelSerializer):
    category = RecursiveCategorySerializer()

    class Meta:
        model = News
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture')


class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_joined', 'author')
