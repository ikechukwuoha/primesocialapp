from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    educational_stats = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=50, blank=True)
    local_govt = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=55, blank=True)
    gender = models.CharField(max_length=25, blank=True)
    email = models.EmailField(null=True, max_length=100, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True)
    other_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=True)
    profesion = models.CharField(max_length=100, blank=True)



    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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