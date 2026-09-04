from django.http import HttpResponse
from django.shortcuts import render

# Health check endpoint for probes
def healthz(request):
    return HttpResponse("OK", status=200)

# Home view serving HTML
def home(request):
    return render(request, 'index.html')