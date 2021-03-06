from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from books.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
