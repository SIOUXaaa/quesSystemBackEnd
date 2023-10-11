from rest_framework import serializers
from web.models import User

#User model对应的serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance