from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework import serializers
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self,data):
        newuser = User.objects.create_user(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password'],
            image = data['image']  
        )      
        return newuser
    
class Signup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer
    
class updateinfo(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer
    permission_classes = [IsAuthenticated]
    
class fetchuser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userserializer
    
    def get(self, request):
        
        print(request.user.id)
        
        user = User.objects.get(id = request.user.id)
        serializers = self.serializer_class(user)
        return Response(data = serializers.data, status=200)