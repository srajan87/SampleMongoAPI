from rest_framework_mongoengine import serializers 
from analytics.models import Accounts
 
 
class AccountsSerializer(serializers.DocumentSerializer):
 
    class Meta:
        model = Accounts
        fields = (
                  'account_id',
                  'limit',
                  'products')