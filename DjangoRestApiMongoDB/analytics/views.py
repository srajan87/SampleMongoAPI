from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from analytics.models import Accounts
from analytics.serializers import AccountsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def accounts_list(request):
    # GET list of accounts, POST a new account, DELETE all accounts
    if request.method == 'GET':
        accounts = Accounts.objects.all()
        
        account_id = request.GET.get('account_id', None)
        if account_id is not None:
            accounts = accounts.filter(account_id__icontains=account_id)
        
        accounts_serializer = AccountsSerializer(accounts, many=True)
        return JsonResponse(accounts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        accounts_data = JSONParser().parse(request)
        accounts_serializer = AccountsSerializer(data=accounts_data)
        if accounts_serializer.is_valid():
            accounts_serializer.save()
            return JsonResponse(accounts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Accounts.objects.all().delete()
        return JsonResponse({'message': '{} Accounts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def accounts_detail(request, pk):
    # find account by pk (id)
    try: 
        account = Accounts.objects.get(pk=pk) 
    except Accounts.DoesNotExist: 
        return JsonResponse({'message': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        accounts_serializer = AccountsSerializer(account) 
        return JsonResponse(accounts_serializer.data)
    elif request.method == 'PUT': 
        account_data = JSONParser().parse(request) 
        accounts_serializer = AccountsSerializer(account, data=account_data) 
        if accounts_serializer.is_valid(): 
            accounts_serializer.save() 
            return JsonResponse(accounts_serializer.data) 
        return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        account.delete() 
        return JsonResponse({'message': 'Account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def accounts_list_registered(request):
    # GET all published tutorials
    accounts = Accounts.objects.all()
    print(accounts)
    if request.method == 'GET': 
        accounts_serializer = AccountsSerializer(accounts, many=True)
        #print(account_serializer.data)
        return JsonResponse(accounts_serializer.data, safe=False)


