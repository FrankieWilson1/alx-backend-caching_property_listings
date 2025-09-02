from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.forms.models import model_to_dict

from .models import Property
from .utils import get_all_properties


@cache_page(60 * 15)  # Cache the entire view for 15 minutes
def property_list(request):
    """
    An API endpoint that returns a list of all properties in JSON format.
    The entire response is cached in Redis for 15 minutes.
    """
    properties = get_all_properties()

    property_data = [model_to_dict(prop) for prop in properties]

    return JsonResponse({'data': property_data})
