from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from GithubApi.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
