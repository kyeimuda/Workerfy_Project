from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import WorkerfyUser  # Import your custom user model

class WorkerfyUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Attempt to get a WorkerfyUser by email and password
            workerfy_user = WorkerfyUser.objects.get(email=email)
        except WorkerfyUser.DoesNotExist:
            return None
        
        # Check if the password matches
        if workerfy_user and check_password(password, workerfy_user.password):
            return workerfy_user  # Return the authenticated user
        return None

    def get_user(self, user_id):
        try:
            return WorkerfyUser.objects.get(pk=user_id)
        except WorkerfyUser.DoesNotExist:
            return None
