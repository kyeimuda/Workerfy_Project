def portfolio_image_upload_path(instance, filename):
    return f"portfolio/images/user_{instance.tradesperson.user.id}/{filename}"

def portfolio_video_upload_path(instance, filename):
    return f"portfolio/videos/user_{instance.tradesperson.user.id}/{filename}"