from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Prime(models.Model):
    user = models.ForeignKey(User, 
                            related_name="primes", 
                            on_delete=models.DO_NOTHING)

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:100]}..."
        )