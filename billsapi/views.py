from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BillsSerializer
from .models import Bills
from .permissions import IsOwner

class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Bills.objects.filter(user=user, active=True).order_by('-created_at').annotate(total=Sum('bills__price'))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
