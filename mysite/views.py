# core/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    # Equivalente a <Home /> en App.tsx.
    # gallery_images reemplaza el array hardcodeado que tenías dentro de Gallery.tsx.
    # El día que tengas un modelo Django para esto, cambias esta lista por una query
    # (ej. Image.objects.all()) y el template de gallery.html no cambia.
    gallery_images = [
        {"url": "/static/img/banner.jpg", "title": "Vintage Horror"},
        {"url": "/static/img/nail1.jpg", "title": "Gothic Claws"},
        {"url": "/static/img/nail2.jpg", "title": "Witch Aesthetics"},
        {"url": "/static/img/nail3.jpg", "title": "Slasher Style"},
        {"url": "/static/img/nail4.jpg", "title": "Vampiric French"},
        {"url": "/static/img/nail5.jpg", "title": "Blood Drip"},
        {"url": "/static/img/nail6.jpg", "title": "Dark Magic"},
        {"url": "/static/img/nail7.jpg", "title": "Occult Symbols"},
    ]
    return render(request, "home.html", {"gallery_images": gallery_images})


def products(request):
    # Equivalente a <Products /> montado en /store
    return render(request, "products.html")


def healthz(request):
    return JsonResponse({"status": "ok"})


@csrf_exempt  # si usas fetch() con CSRF token del template, quita csrf_exempt y usa {% csrf_token %}
def booking_submit(request):
    """
    Endpoint opcional: si más adelante quieres guardar la cita en PostgreSQL
    ANTES de redirigir a WhatsApp. Por ahora el formulario funciona sin este
    endpoint (abre WhatsApp directo con JS), así que esto es solo un punto
    de partida si decides agregar el modelo Booking después.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        # Aquí iría: Booking.objects.create(**data)
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False}, status=405)
