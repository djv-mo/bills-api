from rest_framework import serializers
from .models import Bills, BillsItems


class BillsSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    total = serializers.FloatField(read_only=True)

    class Meta:
        model = Bills
        fields = '__all__'
        read_only_fields = ('active',)

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d %Y')

class BillsItemsSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    negative = serializers.BooleanField(read_only=True)

    class Meta:
        model = BillsItems
        exclude = ('bill', 'user',)

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d %Y')
