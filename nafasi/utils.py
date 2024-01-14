from rest_framework import status
from rest_framework.response import Response


def set_serializer_author_and_response(cls, request):
    data = request.data
    data["author"] = request.user.id
    serializer = cls.serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def set_serializer_author_response_update(cls, request, instance):
    data = request.data
    data["author"] = request.user.id
    serializer = cls.serializer_class(instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
