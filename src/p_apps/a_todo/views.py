from .models import ToDos
from .serializers import ToDoSerializer
from rest_framework import permissions, viewsets, filters


# Create your views here.
class ToDoViewSets(viewsets.ModelViewSet):
    """
    API endpoint that allows authenticated users to view a list of Todos.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDos.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'description', 'priority']
    ordering = ['priority']