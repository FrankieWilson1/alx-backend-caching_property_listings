from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetches all properties, first checking the low-level cache.
    Caches the queryset for 1 hour if not found.
    """
    cache_key = 'all_properties'
    
    properties_queryset = cache.get(cache_key)
    
    if not properties_queryset:
        properties_queryset = Property.objects.all().order_by('-created_at')
        
        cache.set(cache_key, properties_queryset, 3600)
        
        print("Fetched properties from the database and cached them.")
    else:
        print("Fetched properties from the cache.")
        
    return properties_queryset
