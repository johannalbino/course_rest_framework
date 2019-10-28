from rest_framework.serializers import ModelSerializer
from type_test.models import TypeTest


class TypeTestSerializer(ModelSerializer):
    class Meta:
        model = TypeTest
        fields = ['id_type_test', 'description', 'type']
