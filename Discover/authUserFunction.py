from django.contrib.auth.models import BaseUserManager


class WorkerfyUserManager(BaseUserManager):
    def create_user(self, email, user_type, password=None):
        if not email:
            raise ValueError("The Email field is required")
        """ if not username:
            raise ValueError("The Username field is required") """
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_type='admin', password=None):
        user = self.create_user(email=email, user_type=user_type, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


