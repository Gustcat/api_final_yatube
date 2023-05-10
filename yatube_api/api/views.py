from rest_framework import viewsets, mixins, permissions, serializers
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from posts.models import Post, Comment, Follow
from .serializers import PostSerializer, CommentSerializer, FollowSerializer

class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = FollowSerializer#data=request.data, context={'request': request})
    pagination_class = None
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        # print('PERFORM_CREATE')
        # print(serializer.data['following'])
        # if self.request.user.id == serializer.data['following']:
        #     raise serializers.ValidationError
        serializer.save(user=self.request.user)
