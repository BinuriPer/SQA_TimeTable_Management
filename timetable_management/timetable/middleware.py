from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

User = get_user_model()

class LoginAttemptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and request.path == "/login/":
            username = request.POST.get("username")
            user = User.objects.get(username=username)
            if user and user.last_login_attempt and user.login_attempts >= 3:
                if timezone.now() - user.last_login_attempt < timezone.timedelta(minutes=15):
                    return HttpResponse("Account locked due to too many failed login attempts.")
        
        response = self.get_response(request)

        return response