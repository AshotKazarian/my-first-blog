from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('sample/', views.sample_view),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns