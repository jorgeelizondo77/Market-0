from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('applications.users.urls','users'), namespace='users')),
    path('',include(('applications.base.urls','base'), namespace='base')),
    path('',include(('applications.dom.urls','dom'), namespace='dom')),
    path('',include(('applications.cli.urls','cli'), namespace='cli')),
    path('',include(('applications.prod.urls','prod'), namespace='prod')),
    path('',include(('applications.prov.urls','prov'), namespace='prov')),
    path('',include(('applications.oc.urls','oc'), namespace='oc')),
] 
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
