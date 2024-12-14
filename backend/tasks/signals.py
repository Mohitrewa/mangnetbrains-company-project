from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Task
from django.contrib.auth.models import User

@receiver(post_save, sender=Task)
def task_saved_handler(sender, instance, created, **kwargs):
    """
    Signal to handle actions when a Task is created or updated.
    """
    if created:
        print(f"Task '{instance.title}' was created and assigned to {instance.assigned_user}.")
    else:
        print(f"Task '{instance.title}' was updated.")

@receiver(pre_delete, sender=Task)
def task_deleted_handler(sender, instance, **kwargs):
    """
    Signal to handle actions when a Task is deleted.
    """
    print(f"Task '{instance.title}' assigned to {instance.assigned_user} is being deleted.")

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    """
    Signal to perform an action when a User is created.
    """
    if created:
        print(f"User '{instance.username}' has been created.")
