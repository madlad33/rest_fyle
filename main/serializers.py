from rest_framework import serializers
from .models import Banks,Branches

class BankSerialzier(serializers.ModelSerializer):
    """Serializer for Bank objects"""
    class Meta:
        model = Banks
        fields = ['name','id']
        read_only_fields = ['id']


class BranchSerializer(serializers.ModelSerializer):
    """Serializer for branch objects"""
    class Meta:
        model = Branches
        fields = ['ifsc','bank_id','branch','address','city','district','state']
        read_only_fields = fields

