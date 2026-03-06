from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from .validators import validate_certificate_file, validate_video_size, validate_video_extension
from .paths import portfolio_image_upload_path, portfolio_video_upload_path

# Create your models here.


# Create your models here.
# Main1 : models for the Trades types
User = get_user_model() # This will use the custom user model if one is defined, otherwise it will use the default User model.

# Country model
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    initials = models.CharField(max_length=10, default="N/A")
    code = models.CharField(max_length=10, default="N/A")

    def __str__(self):
        return self.name
    
class Region(models.Model):

    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='regions')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.region.name}, {self.region.country.initials}"


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.city.name}, {self.city.region.name}, {self.city.region.country.initials}"
    
"""
1. TradeCategory
Represents the main trade field (e.g., Carpentry, Plumbing, Electrical).

Used to group related specialties.

Selected as the primary category for a tradesperson.
"""
class TradeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Trade Categories"

    def __str__(self):
        return self.name

"""
2. TradeSpecialty
A subcategory under a trade category (e.g., Roofing under Carpentry).

Tradespeople can select multiple specialties.

Linked to TradeCategory with a ForeignKey.

Enables specific filtering and search (e.g., find a roofer or cabinet maker).
"""
class TradeSpecialty(models.Model):
    category = models.ForeignKey(
        TradeCategory, 
        on_delete=models.CASCADE, 
        related_name="specialties"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('category', 'name')
        verbose_name_plural = "Trade Specialties"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

"""
3. TradeSkillTag
Free-form tags for detailed skill attributes (e.g., Smart Lighting, PVC Pipes, Roof Truss).

Helps with flexible keyword search and extra filtering.

Many-to-many relationship with TradespersonProfile.
"""
class TradeSkillTag(models.Model):
    category = models.ForeignKey(
        TradeCategory,
        on_delete=models.CASCADE,
        related_name="tags"
    )
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('category', 'name')
        verbose_name = "Trade Skill Tag"
        verbose_name_plural = "Trade Skill Tags"

    def __str__(self):
        return f"{self.name}"
    
class Certificate(models.Model):
    tradesperson = models.ForeignKey(
        'TradespersonProfile', 
        on_delete=models.CASCADE, 
        related_name='certificates'
    )
    
    # Core certificate info
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    certificate_file = models.FileField(
        upload_to='certificates/',
        validators=[validate_certificate_file],
        help_text="Upload PDF or image file (max 5MB)"
    )
    
    # Verification fields
    contact_person = models.CharField(max_length=255, blank=True, help_text="Person to contact for verification")
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    verification_notes = models.TextField(blank=True, help_text="Additional instructions or context for verification")
    
    # Optional verification status
    verified = models.BooleanField(default=False)
    verified_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.tradesperson.user.get_full_name()}" 

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='badges/')

    def __str__(self):
        return self.name


class EarnedBadge(models.Model):
    tradesperson = models.ForeignKey('TradespersonProfile', on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_on = models.DateField(auto_now_add=True)
    source = models.CharField(max_length=255, blank=True, help_text="e.g. Admin, Course, Test, etc.")

    class Meta:
        unique_together = ('tradesperson', 'badge')

    def __str__(self):
        return f"{self.tradesperson.user.get_full_name()} - {self.badge.name}"  

class PortfolioItem(models.Model):
    """Images or videos of completed work."""
    tradesperson = models.ForeignKey(
        "TradespersonProfile", 
        on_delete=models.CASCADE, 
        related_name="portfolio"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year_completed = models.PositiveIntegerField(null=True, blank=False)

    image = models.ImageField(
        upload_to=portfolio_image_upload_path, 
        blank=True, 
        null=True,
        validators=[validate_certificate_file]
    )

    video = models.FileField(
        upload_to=portfolio_video_upload_path,
        blank=True,
        null=True,
        validators=[validate_video_size, validate_video_extension]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

"""4. TradespersonProfile
Represents the user’s professional profile on Workerfy.

Linked to:

One main TradeCategory (via ForeignKey)

Many TradeSpecialties (via ManyToManyField)

Many TradeSkillTags (via ManyToManyField)

Stores the core professional identity of the tradesperson.
"""

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    other_names = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=150, blank=True, help_text="Username for login")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, help_text="Phone number for client contact")
    contact_number2 = models.CharField(max_length=15, blank=True, help_text="Secondary phone number (Whatsapp, etc.)")
    gender = models.CharField(max_length=50, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')], 
        blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    data_of_birth = models.DateField(null=True, blank=True)
    base_location = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name="client_base_location")
    sub_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="client_sub_location")
    work_areas = models.ForeignKey(Area,on_delete=models.SET_NULL, related_name="client_areas", null=True, blank=True)

class TradespersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tradesperson_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    other_names = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, help_text="Short bio or introduction")
    tagline = models.CharField(max_length=100, blank=True, help_text="A catchy tagline for your profile")
    contact_number = models.CharField(max_length=15, blank=True, help_text="Phone number for client contact")
    contact_number2 = models.CharField(max_length=15, blank=True, help_text="Secondary phone number (Whatsapp, etc.)")
    gender = models.CharField(max_length=50, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')], 
        blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True, help_text="Social media links (e.g. Facebook, Instagram)")
    website = models.URLField(blank=True, help_text="Personal or business website URL")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, help_text="Is this profile active?")
    is_verified = models.BooleanField(default=False, help_text="Is this tradesperson verified?")
    date_of_birth = models.DateField(null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0, help_text="Years of professional experience")
    
    trade_category = models.ForeignKey(
        TradeCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tradespeople_category"
    )

    # Uncomment the following line if you want to allow multiple trade categories per tradesperson
    #trade_categories = models.ManyToManyField(TradeCategory, related_name="tradespeople", blank=True)

    trade_specialties = models.ManyToManyField(
        TradeSpecialty,
        blank=True,
        related_name="tradespeople_specialty"
    )

    skills = models.ManyToManyField(
        TradeSkillTag, 
        blank=True, 
        related_name="tradespeople_skills"
    )

    base_location = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name="tradespeople_base")
    sub_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="tradespeople_sub")
    work_areas = models.ForeignKey(Area,on_delete=models.SET_NULL, related_name="tradespeople_work_areas", null=True, blank=True)
    working_areas = models.JSONField(default=list, blank=True, help_text="Areas tradespeople can service")
    availability_status = models.CharField(
        max_length=50, 
        choices=[
            ('Available Now', 'Available Now'),
            ('Urgent', 'Urgent'),
            ('Busy', 'Busy'),
            ('On Leave', 'On Leave')
        ], 
        default='Available'
    )

    education_schools = models.JSONField(default=list, blank=True, help_text="List of schools attended")

    other_skills = models.JSONField(default=list, blank=True, help_text="Other skills not covered by tags")
    rate_charged = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Hourly or project rate charged by the tradesperson")

    def __str__(self):
        name = f"{self.first_name} {self.last_name}".strip()
        return name if name else self.username or f"Tradesperson {self.id}"


JOB_TYPE_CHOICES = [
    ("one_time", "One-time"),
    ("recurring", "Recurring"),
    ("contract", "Contract"),
]

WORK_ENV_CHOICES = [
    ("indoor", "Indoor"),
    ("outdoor", "Outdoor"),
    ("residential", "Residential"),
    ("industrial", "Industrial"),
]

URGENCY_CHOICES = [
    ("urgent", "Urgent"),
    ("normal", "Normal"),
]

BUDGET_TYPE_CHOICES = [
    ("fixed", "Fixed Price"),
    ("hourly", "Hourly Rate"),
    ("negotiable", "Negotiable"),
]

MATERIALS_CHOICES = [
    ("yes", "Yes"),
    ("no", "No"),
]

CONTACT_METHOD_CHOICES = [
    ("whatsapp", "Whatsapp"),
    ("email", "Email"),
    ("call", "Call"),
    ("text", "Text"),
]

class JobPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="job_posts")
    title = models.CharField(max_length=255)
    trade_category = models.ForeignKey(TradeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=255, blank=True)

    work_environment = models.CharField(max_length=20, choices=WORK_ENV_CHOICES, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    urgency_level = models.CharField(max_length=10, choices=URGENCY_CHOICES, blank=True)
    budget_type = models.CharField(max_length=20, choices=BUDGET_TYPE_CHOICES, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)

    materials_provided = models.CharField(max_length=3, choices=MATERIALS_CHOICES, default="no")
    required_skills = models.JSONField(default=list, blank=True, help_text="List of required skills for the job")

    contact_method = models.CharField(max_length=20, choices=CONTACT_METHOD_CHOICES, blank=True)
    contact_number = models.CharField(max_length=50, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.trade_category or 'Uncategorized'}"

class JobPostAttachment(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="job_attachments/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.uploaded_at}{self.job_post.pk} - {self.job_post.title}"
