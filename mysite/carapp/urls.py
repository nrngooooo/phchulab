from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CarListView, CarUpDel, CarMarkListView, CarMarkUpDel

urlpatterns = [
    path('cars/', CarListView.as_view(), name='carlist'),
    path('cars/<int:pk>/', CarUpDel.as_view(), name='carupdel'),
    path('carmarks/', CarMarkListView.as_view(), name='carmarklist'),
    path('carmarks/<int:pk>/', CarMarkUpDel.as_view(), name='carmarkupdel'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)