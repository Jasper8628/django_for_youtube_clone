from rest_framework.generics import ListAPIView,RetrieveAPIView, CreateAPIView
from djapp.models import Book
from .serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class=ArticleSerializer
    
class ArticleDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class=ArticleSerializer
    
class ArticleCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class=ArticleSerializer
