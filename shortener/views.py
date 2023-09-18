from django.http import (
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.decorators import api_view

from shortener.models import Shortener


@api_view(['POST'])
def create_short_url(request):
    url = request.data.get('url')
    shortener, _ = Shortener.objects.get_or_create(url=url)
    full_url = request.build_absolute_uri(reverse('get_short_url', kwargs={'id': shortener.id}))
    return JsonResponse({'url': full_url})


@api_view(['GET'])
def get_short_url(request, id):
    url_id = id.split('/')[-1]
    shortener = get_object_or_404(Shortener, id=url_id)
    return JsonResponse({'url': shortener.url})
