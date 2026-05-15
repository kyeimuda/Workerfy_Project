import os
from django.core.exceptions import ValidationError

def validate_certificate_file(value):
    # 1. File size (5MB max)
    max_size_mb = 5
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size should not exceed {max_size_mb}MB.")

    # 2. File extension
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file format. Allowed: PDF, JPG, PNG.')

def validate_video_size(file):
    """Ensure video is not larger than 10 MB."""
    max_size_mb = 10
    if file.size > max_size_mb * 1024 * 1024:  # bytes
        raise ValidationError(f"Video file size must not exceed {max_size_mb} MB.")

def validate_video_extension(file):
    """Ensure uploaded file has an allowed video extension."""
    valid_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    ext = os.path.splitext(file.name)[1].lower()  # get file extension
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported file type. Allowed types: {', '.join(valid_extensions)}")

#This vailidator checks is the user is a has a Trades, client or admin acount
def validate_user_role(user):
    """Ensure the user has a valid role: Trades, Client, or Admin."""
    if not user.is_authenticated:
        raise ValidationError("User must be authenticated.")
    
    if hasattr(user, 'tradesperson_profile'):
        return 'Tradesperson'
    if hasattr(user, 'client'):
        return 'Client'
    if user.is_staff:
        return 'Admin'
        
    raise ValidationError("User does not have a valid role. Must be Tradesperson, Client, or Admin")
               
