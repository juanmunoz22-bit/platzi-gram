# Django
from django.shortcuts import redirect
from django.urls import reverse

# Models
    # Profile
from users.models import Profile

class ProfileCompletionMiddleware:
    """Middleware for the update info of a user
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile: Profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update'), reverse('logout')]:
                        return(redirect('update'))

        response = self.get_response(request)
        return response