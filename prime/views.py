from django.shortcuts import render, redirect
from .forms import PrimeForm
from .models import Prime, Profile



# Create your views here.
def dashboard(request):
    form = PrimeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prime = form.save(commit=False)
            prime.user = request.user
            prime.save()
            return redirect("prime:dashboard")
    followed_primes = Prime.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(
        request,
        "prime/dashboard.html",
        {"form": form, "primes": followed_primes},
    )

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "prime/profile_list.html", {"profiles": profiles})


def profile(request, pk):

    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "prime/profile.html", {"profile": profile})

def notification(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "prime/notification.html", {"profiles": profiles})
