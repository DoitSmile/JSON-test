from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


# PostViewSet이 post_list의 2개분기 와 post_detail의 3개분기를 두개의 정보만으로 지원한다.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # 보여줄 범위
    serializer_class = PostSerializer  # 최소 이 두가진 해줘야함

    # 실제 클래스기반뷰, viewset에서 실제요청이 올때마다 호출되는 함수
    def dispatch(self, request, *args, **kwargs):
        print("request.body:", request.body)
        print("request.POST:", request.POST)
        return super().dispatch(request, *args, **kwargs)
