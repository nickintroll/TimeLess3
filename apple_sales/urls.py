from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # my_apps
    path('', include('core.urls', namespace='core')),
    path('shop/', include('shop.urls', namespace='shop')),
	path('cart/', include('cart.urls', namespace='cart')),

]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)