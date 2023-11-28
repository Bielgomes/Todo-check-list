from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.api.serializers import ProfilesSerializers
from user.models import Profile


class ProfilesViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializers

    def create(self, request, *args, **kwargs):
        profile = self.queryset.get(email=request.data['email'])
        if profile:
            return Response({'detail': 'This email already exists.'}, status=status.HTTP_409_CONFLICT)

        new_profile = Profile.objects.create_user(**request.data)
        serializer = ProfilesSerializers(new_profile)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        profile = self.queryset.get(pk=request.user.id)

        serializer = ProfilesSerializers(profile)
        return Response(serializer.data)

    @action(methods=['PATCH'], detail=False)
    def password(self, request):
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        profile = self.queryset.get(pk=request.user.id)
        profile.set_password(request.data['password'])
        profile.save()

        return Response()

    @action(methods=['PATCH'], detail=False)
    def email(self, request):
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        profile = self.queryset.get(pk=request.user.id)

        try:
            profile_with_same_email = self.queryset.get(email=request.data['email'])
            return Response({'detail': 'This email already exists'}, status=status.HTTP_409_CONFLICT)
        except:
            pass

        profile.email = request.data['email']
        profile.save()

        return Response()
