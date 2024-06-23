from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from account.models import Account
from account.serializers import AccountSerializer
    
class AccountAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ('id', 'name', 'balance', 'currency')
    search_fields = ('name', 'balance', 'currency')
    ordering_fields = ('id', 'name', 'balance', 'currency')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
    

class AccountDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)