from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import UserModel
from rest_framework import serializers

 
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UserModel.objects.all()
 
    # specify serializer to be used
    serializer_class = UserSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
		'View':'/user/view/pk',
        'Add': '/create',
        'Update': '/user/pk',
        'Delete': '/user/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)
 
    # validating for already existing data
    if UserModel.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esse usuário já existe')
 
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_users(request):
	
	# checking for the parameters from the URL
	if request.query_params:
		users = UserModel.objects.filter(**request.query_params.dict())
	else:
		users = UserModel.objects.all()

	# if there is something in items else raise error
	if users:
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_user(request, pk):
	
    try:
        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
