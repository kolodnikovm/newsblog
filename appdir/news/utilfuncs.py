from rest_framework import serializers


def main_news_pic(instance, filename):

    return 'news_{0}/main_{1}'.format(instance.id, filename)


def news_pics(instance, filename):

    return 'news_{0}/{1}'.format(instance.id, filename)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
