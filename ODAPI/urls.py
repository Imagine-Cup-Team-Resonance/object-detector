from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('ODAPI', views.ImageView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.detect),
    path('', views.uploadImages, name='uploadImages')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()