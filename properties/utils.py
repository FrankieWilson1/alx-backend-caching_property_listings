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

def get_redis_cache_metrics():
    """
    Retrieves and analyzes Redis cache hit/miss metrics.
    Connects to Redis directly to get INFO, calculates the hit ratio, and logs the metrics.
    """
    try:
        # Get the underlying redis client from django_redis
        redis_client = cache.client.get_client()
        
        # Get cache statistics using the INFO command
        redis_info = redis_client.info('stats')
        
        hits = redis_info.get('keyspace_hits', 0)
        misses = redis_info.get('keyspace_misses', 0)
        
        total_requests = hits + misses
        hit_ratio = (hits / total_requests) * 100 if total_requests > 0 else 0
        
        metrics = {
            'keyspace_hits': hits,
            'keyspace_misses': misses,
            'total_requests': total_requests,
            'hit_ratio': round(hit_ratio, 2)
        }
        
        print("--- Redis Cache Metrics ---")
        print(f"Keyspace Hits: {metrics['keyspace_hits']}")
        print(f"Keyspace Misses: {metrics['keyspace_misses']}")
        print(f"Hit Ratio: {metrics['hit_ratio']}%")
        print("---------------------------")
        
        return metrics

    except Exception as e:
        print(f"Error fetching Redis metrics: {e}")
        return {}
