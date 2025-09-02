from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from .models import Property

@receiver(post_save, sender=Property)
def clear_properties_cache_on_save(sender, instance, **kwargs):
    """
    Signal handler to clear the 'all_properties' cache on property save (create or update).
    """
    print(f"Clearing 'all_properties' cache due to save operation on Property: {instance.title}")
    cache.delete('all_properties')

@receiver(post_delete, sender=Property)
def clear_properties_cache_on_delete(sender, instance, **kwargs):
    """
    Signal handler to clear the 'all_properties' cache on property deletion.
    """
    print(f"Clearing 'all_properties' cache due to delete operation on Property: {instance.title}")
    cache.delete('all_properties')