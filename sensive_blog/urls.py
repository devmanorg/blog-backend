from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
