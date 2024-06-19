from rest_framework import response, status
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer

class RegisterApiView(GenericAPIView):

    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    