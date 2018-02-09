from rest_framework import serializers
from users.models import User
from news.models import News, Author, Category, Tag
from rest_framework_recursive.fields import RecursiveField


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


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

    class Meta:
        model = News
        fields = ('heading', 'creation_date', 'author', 'category',
                  'tags', 'text_content', 'main_picture', 'extra_pics')


class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_joined', 'author')
