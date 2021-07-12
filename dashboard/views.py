from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import EmployeeSerilizer,EmployeeUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
User = get_user_model()
class CreateEmployee(generics.GenericAPIView):
    serializer_class = EmployeeSerilizer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({
            'user':data,
            "message":"Account Created Successfully Please login",
        })
        '''except Exception as e:
            return Response({'Error':'Some fields are missing'})'''


class EmployeeDetails(APIView):

    def get_employee(self,data):
        try:
            if ('Name' in data) and ('MobileNo' in data):
                return User.objects.filter(FirstName = data['Name'],MobileNo = data['MobileNo'])
            elif 'Name' in data:
                return User.objects.filter(FirstName = data['Name'])
            elif data['MobileNo']:
                return User.objects.filter(MobileNo = data['MobileNo'])
        except User.DoesNotExist:
            raise Http404


    def get(self,format=None):
        users = User.objects.all()
        serializer = EmployeeSerilizer(users, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        user = self.get_employee(request.data)
        serializer = EmployeeSerilizer(user,many=True)
        return Response(serializer.data)

class UpdateEmployee(APIView):
    def put(self, request):
        try:
            user = User.objects.get(EmailId = request.data['EmailId'])
        except Exception as e:
            return Response({'message':'Email is not registered Please provide a valid one....!'})
        serializer = EmployeeUpdateSerializer(user, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def delete(self, request, format=None):
        try:
            user = User.objects.get(EmailId = request.data['EmailId'])
        except Exception as e:
            return Response({'message':'Email is not registered Please provide a valid one....!'})
        user_name = user.FirstName
        print(user_name)
        user.delete()
        return Response({'message':f'{user_name} is deleted'})