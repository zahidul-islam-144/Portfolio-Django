from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('App_Core.urls')),
    path('edu/', include('App_Edu.urls')),

] 
    # path('edu/', include('App_Edu.urls')),
    # path('service/', include('App_Service.urls')),

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  