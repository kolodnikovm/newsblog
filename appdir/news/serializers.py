from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from news.models import Author, Category, DraftNews, Tag, PublishedNews
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


class DraftNewsSerializer(serializers.ModelSerializer):
    category = RecursiveCategorySerializer()

    class Meta:
        model = DraftNews
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
