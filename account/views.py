from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from account.models import Account
from account.serializers import AccountSerializer
    
class AccountAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )

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