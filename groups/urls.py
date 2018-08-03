from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name="groups"

urlpatterns = [
    path('', views.Index, name='Index'),
    path('detail/<int:id>', views.detail, name='GroupDetail'),
    path('create_elem/<int:group_id>', views.create_elem, name='ElemCreate'),
    # path('memo_del/', views.memo_del, name='memo_del'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)