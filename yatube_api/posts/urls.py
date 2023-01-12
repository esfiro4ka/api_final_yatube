from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include(router.urls)),
]