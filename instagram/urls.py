from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()  # router 인스턴스만들고 아래에서 프로젝트주소와 view를 지정해주면 이시점에서 2개의 url이 만들어진다.
router.register('post', views.PostViewSet)  # 2개의 URL을 만들어준다.
# router.urls > url pattern list

urlpatterns = [
    path('', include(router.urls)),
]
