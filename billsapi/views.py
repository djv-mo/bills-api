from django.db.models import Sum
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .serializers import BillsSerializer, BillsItemsSerializer
from .models import Bills, BillsItems
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


class BillsItemsListCreateApiView(generics.ListCreateAPIView):
    serializer_class = BillsItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        id = self.kwargs.get('pk')
        return BillsItems.objects.filter(bill__id=id, bill__user=user).order_by('-created_at')

    def perform_create(self, serializer):
        user = self.request.user
        id = self.kwargs.get('pk')
        bill = get_object_or_404(Bills, id=id)
        # get serializer data to validate price
        serializer.is_valid()
        validatedData = serializer.validated_data
        price = validatedData.get('price')
        # check if the price is positive or negative
        if price < 0:
            serializer.save(negative=True)
        # checking if the user is the owner of the bill
        if bill.user == user:
            serializer.save(bill=bill, user=user)
        else:
            raise NotFound('Not found.')


class BillsItemRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillsItems.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = BillsItemsSerializer

    def perform_update(self, serializer):
        serializer.is_valid()
        validatedData = serializer.validated_data
        price = validatedData.get('price')
        # check if the price is positive or negative
        if price < 0:
            serializer.save(negative=True)
        else:
            serializer.save(negative=False)
