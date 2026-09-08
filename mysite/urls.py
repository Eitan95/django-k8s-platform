# mysite/urls.py
# Equivalente a tu App.tsx: App.tsx usaba wouter con <Route path="/" /> y <Route path="/store" />.
# En Django no hay un "Router" en el cliente: cada URL mapea directo a una vista que renderiza un template.

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite import views  # ajusta "core" al nombre real de tu app Django

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("store/", views.products, name="products"),  # antes: /store con <Products />
    path("booking/", views.booking_submit, name="booking_submit"),  # ver views.py
    path("healthz", views.healthz, name="healthz"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# El NotFound de tu App.tsx (el 404 con "The void consumes this page.") se maneja distinto en Django:
# 1. Crea templates/404.html con ese mismo contenido (ver nota abajo).
# 2. En settings.py asegúrate de tener DEBUG = False en producción para que Django lo use.
