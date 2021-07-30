from rest_framework import serializers
from .models import Bills, BillsItems


class BillsSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Bills
        fields = '__all__'
        read_only_fields = ('active',)

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d %Y')
