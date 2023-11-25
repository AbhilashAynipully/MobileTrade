from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls'),name='users_urls' ),
    path('mobiles/', include('mobiles.urls')),
]

handler403 = handler403
handler404 = handler404
handler500 = handler500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)