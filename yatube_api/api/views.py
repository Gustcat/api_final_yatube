from rest_framework import viewsets, mixins, permissions, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from posts.models import Post, Comment, Follow, Group
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer

class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('$following',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
