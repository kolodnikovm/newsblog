from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from news.models import Author, Category, News, Tag
from news.utils.serializers import RecursiveField
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


class NewsSerializer(serializers.ModelSerializer):
    category = RecursiveCategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = News
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'avatar', 'first_name', 'last_name')
