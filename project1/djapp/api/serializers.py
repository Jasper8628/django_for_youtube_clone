from rest_framework import serializers
from djapp.models import Book

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('selfLink','title','authors','thumbnail','description')