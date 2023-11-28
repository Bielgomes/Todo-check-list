from rest_framework.serializers import ModelSerializer

from user.models import Profile


class ProfilesSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email')
        read_only_fields = ('is_staff', 'is_superuser')