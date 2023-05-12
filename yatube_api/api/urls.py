from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
