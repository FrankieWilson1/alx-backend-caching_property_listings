from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .models import Property


@cache_page(60 * 15)  # Cache the entire view for 15 minutes
def property_list(request):
    """
    A view that displays a list of all properties.
    The entire page is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all().order_by('-created_at')
    context = {
        'properties': properties,
    }
    return render(request, 'properties/property_list.html', context)
