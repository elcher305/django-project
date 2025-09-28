
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
     path('catalog/', include('catalog.urls')),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)