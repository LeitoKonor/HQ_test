from rest_framework import viewsets
from .models import Product, Lesson, LessonView
from .serializer import ProductSerializer, LessonSerializer, LessonViewSerializer

class LessonListView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(viewsets.ModelViewSet):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer

class ProductStatisticsView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer