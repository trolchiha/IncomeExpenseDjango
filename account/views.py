from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from account.models import Account
from account.serializers import AccountSerializer

class CreateAccountAPIView(CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AccountListAPIView(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Account.objects.all()

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
    