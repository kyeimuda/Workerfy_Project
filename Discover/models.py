from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .authUserFunction import WorkerfyUserManager
from django.utils import timezone
import uuid

# Create your models here.

# This model creates the Workerfy users table
class WorkerfyUser(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=[('client', 'Client'), ('tradesperson', 'Tradesperson'), ('admin', 'Admin')])
    date_created = models.DateTimeField(auto_now_add=True)
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False)
    verified = models.BooleanField(default=False)

    # Required fields for Django's authentication
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = WorkerfyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # Methods required by Django
    def has_perm(self, perm, obj=None):
        # Admin gets all permissions
        if self.is_admin or self.user_type == 'admin':
            return True
        
        # Non-verified users have limited permissions (read-only)
        if not self.verified:
            return 'view' in perm or 'list' in perm
        
        # Tradesperson permissions
        if self.user_type == 'tradesperson':
            # Allow tradesperson profile, portfolio, and application management
            allowed_perms = [
                'discover.add_tradesperson',
                'discover.change_tradesperson',
                'discover.view_tradesperson',
                'discover.add_pastworkimage',
                'discover.change_pastworkimage',
                'discover.delete_pastworkimage',
                'discover.view_pastworkimage',
                'mainworkerfy.view_jobposting',
                'mainworkerfy.add_jobapplication',
                'mainworkerfy.view_jobapplication',
                'mainworkerfy.add_jobposting',
                'mainworkerfy.change_jobposting',
                'mainworkerfy.delete_jobposting',
                'mainworkerfy.view_jobposting',
                'discover.view_tradesperson',
            ]
            return any(allowed_perm in perm for allowed_perm in allowed_perms)
        
        # Client permissions
        if self.user_type == 'client':
            # Allow client profile and job posting management
            allowed_perms = [
                'discover.add_client',
                'discover.change_client',
                'discover.view_client',
                'mainworkerfy.add_jobposting',
                'mainworkerfy.change_jobposting',
                'mainworkerfy.delete_jobposting',
                'mainworkerfy.view_jobposting',
                'discover.view_tradesperson',
            ]
            return any(allowed_perm in perm for allowed_perm in allowed_perms)
        
        return False

    def has_module_perms(self, app_label):
        # Admin gets all module permissions
        if self.is_admin or self.user_type == 'admin':
            return True
        
        # Non-verified users can only view
        if not self.verified:
            return app_label in ['Discover', 'MainWorkerfy']
        
        # All verified users can access Discover and MainWorkerfy apps
        if app_label in ['Discover', 'MainWorkerfy']:
            return True
        
        return False

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def user_type_verbose(self):
        return dict(self._meta.get_field('user_type').choices).get(self.user_type, 'Unknown')

    class Meta:
        verbose_name = 'Workerfy User'
        verbose_name_plural = 'Workerfy Users'

#This model creates the Tradesperson table
class Tradesperson(models.Model):

    REGIONS = [
    ('Greater_Accra', 'Greater Accra'),
    ('Volta', 'Volta Region'),
    ('Ashanti', 'Ashanti Region'),
    ('Western_North', 'Western North Region'),
    ('Western', 'Western Region'),
    ('Central', 'Central Region'),
    ('Upper_East', 'Upper East Region'),
    ('Savannah', 'Savannah Region'),
    ('North_East', 'North East Region'),
    ('Bono', 'Bono Region'),
    ('Ahafo', 'Ahafo Region'),
    ('Bono_East', 'Bono East Region'),
    ('Upper_West', 'Upper West Region'),
    ('Nortern', 'Nortern Region'),
    ('Oti', 'Oti Region'),
    ('Eastern', 'Eastern Region'),
]


    JOB_TYPES = [
    ('Carpenter', 'Carpenter'),
    ('Electrician', 'Electrician'),
    ('Plumber', 'Plumber'),
    ('Roofer', 'Roofer'),
    ('Painter', 'Painter'),
    ('Drywall', 'Drywall'),
    ('Glazier', 'Glazier'),
    ('Tiler', 'Tiler'),
    ('Ironworker', 'Iron worker or Steel Worker'),
    ('Welder', 'Welder'),
    ('HVAC_Technician', 'HVAC Technician'),
    ('Concrete_Worker', 'Concrete Worker'),
    ('Refrigeration_Technician', 'Refrigeration Technician'),
    ('Landscaper/Gardener', 'Landscaper/Gardener'),
    ('Locksmith', 'Locksmith'),
    ('Pest_Control_Technician', 'Pest Control Technician'),
    ('Cleaning_Technician', 'Cleaning Technician'),
    ('Gas_Fitter', 'Gas Fitter'),
    ('Septic_Tank_Installer/Repairer', 'Septic Tank Installer/Repairer'),
    ('Appliance_Repair_Technician', 'Appliance Repair Technician'),
    ('Solar_Panel_Installer', 'Solar Panel Installer'),
    ('Green_Energy_Technician', 'Green Energy Technician'),
    ('Smart_Home_Technician', 'Smart Home Technician'),
    ('Waterproofing_Specialist', 'Waterproofing Specialist'),
    ('General_Contractor', 'General Contractor'),
    ('Handyman', 'Handyman'),
    ('Scaffolder', 'Scaffolder'),
    ('Labourer', 'Labourer'),
    ('Elevator_Installer_Repairer', 'Elevator Installer/Repairer'),
    ('Auto_Mechanic', 'Auto Mechanic'),
    ('Heavy_Equipment_Operator', 'Heavy Equipment Operator'),
    ('Sheet_Metal_Worker', 'Sheet Metal Worker'),
    ('Industrial_Electrician', 'Industrial Electrician'),
    ('Pipefitter', 'Pipefitter/Steamfitter'),
]


    JOB_TYPE = [
        ('FULL_TIME','Full time'),
        ('PART_TIME', 'Part time'),
        ('FREELANCE_CONTRACTS','Freelance contracts'),
    ]

    AVAILABILITY_STATUS = [
        ('URGENT', 'Urgent'),
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    VERIFICATION_STATUS = [
        ('VERIFIED', 'Verified'),
        ('NOT VERIFIED', 'Not verified'),
    ]

    SERVICE_RANGE = [
        ('INSIDE', 'Inside'),
        ('OUTSIDE', 'Outside'),
        
    ]


    tradesperson_id = models.AutoField(primary_key=True)  # Unique identifier for each tradesperson
    user = models.OneToOneField('WorkerfyUser', on_delete=models.CASCADE)  # References WorkerfyUser
    first_name = models.CharField(max_length=255) 
    middle_name = models.CharField(max_length=255, null=True, blank=True) # Optional middle name 
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField( default='default.jpg', upload_to='profile_pics/', null=True, blank=True)  # Optional profile picture
    phone = models.CharField(max_length=15)  # Primary phone number
    phone2 = models.CharField(max_length=15, null=True, blank=True)  # Optional secondary phone number
    location = models.CharField(max_length=255, choices=REGIONS)  # Detailed address
    address = models.CharField(max_length=255)
    trades_type = models.CharField(max_length=50, choices=JOB_TYPES)  # Specific trade specialization
    specialization = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()  # Number of years in the trade
    extra_skills = models.CharField(max_length=50, choices=JOB_TYPES)  # Additional skills (optional)
    certification = models.TextField(null=True, blank=True)  # Certifications (optional)
    work_hours = models.CharField(max_length=255)  # Availability hours (e.g., "9 AM - 5 PM")
    job_type = models.CharField(max_length=255, choices=JOB_TYPE, default='Full time')  # Job type (e.g., "full-time", "part-time", etc.)
    service_range = models.CharField(max_length=255, choices=SERVICE_RANGE)  # Geographic area or range where services are provided
    rate_charged = models.DecimalField(max_digits=10, decimal_places=2)  # Rate per job/hour
    bio = models.TextField(null=True, blank=True)  # Brief bio about the tradesperson
    languages = models.CharField(max_length=255)  # Languages spoken
    availability_status = models.CharField(max_length=255, choices=AVAILABILITY_STATUS, default='Active')  # Whether they are currently available for jobs
    verification_status = models.CharField(max_length=255, choices=VERIFICATION_STATUS, default='Not verified')  # Whether they are verified on the platform
    created_date = models.DateTimeField(default=timezone.now)  # Date profile was created

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Tradesperson'
        verbose_name_plural = 'Tradespeople'

# This model handles images for past jobs.
class PastWorkImage(models.Model):
    user = models.ForeignKey('WorkerfyUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='past_jobs/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"
    
    class Meta:
         verbose_name = 'Past Work Image'
         verbose_name_plural = 'Past Work Images'



#This model creates the client table
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)  # Unique identifier for each client
    user = models.OneToOneField('WorkerfyUser', on_delete=models.CASCADE)  # References WorkerfyUser
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)  # Optional middle name
    last_name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)  # Brief bio for the client
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)  # Optional profile picture
    location = models.CharField(max_length=255)  # General location (e.g., city or region)
    address = models.CharField(max_length=500)  # Detailed address
    phone = models.CharField(max_length=15)  # Primary phone number
    phone2 = models.CharField(max_length=15, null=True, blank=True)  # Optional secondary phone number
    created_date = models.DateTimeField(default=timezone.now)  # Date profile was created

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


#This model creates the Trades type tables
class TradeType(models.Model):
    trades_id = models.AutoField(primary_key=True)  # Unique identifier for each trade type
    trades_name = models.CharField(max_length=255, unique=True)  # Name of the trade (e.g., Electrician, Plumber)

    def __str__(self):
        return self.trades_name

    class Meta:
        verbose_name = 'Trade Type'
        verbose_name_plural = 'Trade Types'
        ordering = ['trades_name']

#This is model creates the Tradesperson category table
class TradespersonCategory(models.Model):
    id = models.AutoField(primary_key=True)  # Unique identifier for each tradesperson's category entry
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)  # FK to Tradesperson
    trade_types = models.ManyToManyField('TradeType', blank=False)  # Many-to-many relationship with TradeType, max 5

    def __str__(self):
        return f"{self.tradesperson.full_name} - Trades: {[trade.trades_name for trade in self.trade_types.all()]}"

    class Meta:
        verbose_name = 'Tradesperson Category'
        verbose_name_plural = 'Tradesperson Categories'

# This model creates the featues table
class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)  # Unique identifier for each feature
    feature_name = models.CharField(max_length=255, unique=True)  # Name of the feature (e.g., Job Posting, Booking, Messaging)

    def __str__(self):
        return self.feature_name

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
        ordering = ['feature_name']

# This model creates the Job Posting table
class JobPosting(models.Model):
    job_id = models.AutoField(primary_key=True)  # Unique identifier for each job posting
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # FK to Client who posts the job
    job_title = models.CharField(max_length=255)  # Title of the job
    job_description = models.TextField()  # Detailed description of the job
    location = models.CharField(max_length=255)  # Location of the job
    job_start = models.DateField()  # Start date of the job
    job_end = models.DateField()  # End date of the job
    budget = models.DecimalField(max_digits=10, decimal_places=2)  # Budget for the job
    payment_type = models.CharField(max_length=50, choices=[('hourly', 'Hourly'), ('fixed', 'Fixed')])  # Payment type (hourly/fixed)
    application_deadline = models.DateField()  # Deadline for tradespeople to apply for the job
    skills_required = models.CharField(max_length=255)  # Skills required for the job
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-populates when the job is created

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Job Posting'
        verbose_name_plural = 'Job Postings'
        ordering = ['-created_at']

# This model creates the applications table
class Application(models.Model):
    application_id = models.AutoField(primary_key=True)  # Unique identifier for each application
    job_posting = models.ForeignKey('JobPosting', on_delete=models.CASCADE)  # FK to the job being applied to
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)  # FK to the tradesperson applying
    cover_letter = models.TextField(null=True, blank=True)  # Optional cover letter from the tradesperson
    portfolio_link = models.URLField(max_length=500, null=True, blank=True)  # Link to the tradesperson's portfolio, if any
    application_date = models.DateTimeField(auto_now_add=True)  # Date when the application was made
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')  # Application status
    response = models.TextField(null=True, blank=True)  # Optional response or feedback from the client/employer

    def __str__(self):
        return f"Application {self.application_id} for {self.job_posting.job_title}"

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['-application_date']

# This model creates the Booking table
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)  # Unique identifier for each booking
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # FK to the Client making the booking
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)  # FK to the Tradesperson being booked
    job_posting = models.ForeignKey('JobPosting', on_delete=models.SET_NULL, null=True, blank=True)  # Optional FK to the Job Posting if the booking is made through an application acceptance
    features = models.ManyToManyField('Feature')  # M2M relationship with Features
    booking_date = models.DateTimeField(auto_now_add=True)  # Date when the booking was made
    booking_start = models.DateTimeField(null=True, blank=True)  # Proposed start date of the booking
    booking_end = models.DateTimeField(null=True, blank=True)  # Proposed end date of the booking
    booking_description = models.TextField() # this field give more details about the job
    booking_title = models.CharField(max_length=255)# Title of the booking
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], default='pending')  # Status of the booking
    client_message = models.TextField(null=True, blank=True)  # Optional message from the client about the booking
    tradesperson_response = models.TextField(null=True, blank=True)  # Optional response from the tradesperson
    rate_charged = models.DecimalField(max_digits=10, decimal_places=2)  # Rate agreed for the booking
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the booking record was created

    def __str__(self):
        return f"Booking {self.booking_id} by {self.client.full_name}"

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['-booking_date']

# This model creates the services table
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)  # Unique identifier for the service
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)  # One-to-One relationship with Booking (when booking is accepted)
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)  # FK to the tradesperson performing the service
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # FK to the client receiving the service
    service_start = models.DateTimeField()  # Date when the service/job starts
    service_end = models.DateTimeField(null=True, blank=True)  # Optional date when the service/job is completed
    flag = models.CharField(max_length=50, choices= [
        ('Green', 'GREEN'),
        ('Red', 'RED')
    ], default='Green')
    service_status = models.CharField(max_length=50, choices=[
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], default='in_progress')  # Status of the service
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the service was created

    def __str__(self):
        return f"Service {self.service_id} for Booking {self.booking.booking_id}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-service_start']

# This model creates the payment table 
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)  # Unique identifier for each payment
    service = models.ForeignKey('Service', on_delete=models.CASCADE)  # FK to the related service
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # FK to the client making the payment
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the payment
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_payment', 'Mobile Payment')
    ])  # The payment method used
    payment_status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')
    ], default='pending')  # Status of the payment
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # External transaction ID (from payment gateway)
    upfront_payment = models.BooleanField(default=False)  # Indicates whether this is an upfront payment
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time the payment record was created
    last_updated = models.DateTimeField(auto_now=True)  # Timestamp for the last time the payment record was updated

    def __str__(self):
        return f"Payment {self.payment_id} for Service {self.service.service_id} - Status: {self.payment_status}"

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-timestamp']

# This model creates the flaged dispute tables
class Dispute(models.Model):
    DISPUTE_STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    dispute_id = models.AutoField(primary_key=True)  # Unique identifier for each dispute
    service = models.ForeignKey('Service', on_delete=models.CASCADE)  # FK to the service where the dispute arose
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # FK to the client involved
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)  # FK to the tradesperson involved
    dispute_reason = models.TextField()  # Detailed reason for the dispute
    dispute_status = models.CharField(max_length=20, choices=DISPUTE_STATUS_CHOICES, default='open')  # Status of the dispute
    initiator = models.CharField(max_length=50, choices=[
        ('client', 'Client'),
        ('tradesperson', 'Tradesperson')
    ])  # Who initiated the dispute
    created_date = models.DateTimeField(auto_now_add=True)  # Date the dispute was created
    resolved_date = models.DateTimeField(null=True, blank=True)  # Date the dispute was resolved, if applicable
    resolution_notes = models.TextField(null=True, blank=True)  # Additional notes on how the dispute was resolved
    evidence_files = models.FileField(upload_to='disputes/evidence/', null=True, blank=True)  # Uploads of files or images as evidence

    def __str__(self):
        return f"Dispute {self.dispute_id} for Service {self.service.service_id} - Status: {self.dispute_status}"

    class Meta:
        verbose_name = 'Dispute'
        verbose_name_plural = 'Disputes'
        ordering = ['-created_date']

# This table create the Review and Ratings table
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    tradesperson = models.ForeignKey('Tradesperson', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # E.g., 4.50
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.review_id} - Rating: {self.rating} by {self.client} for {self.tradesperson}"
    
    class Meta:
        ordering = ['-created_at']

# This model creates the Notification table 
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('WorkerfyUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Notification {self.notification_id} for {self.user}"

    class Meta:
        ordering = ['-created_at']

# This model creates the Audit log table
class AuditLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('WorkerfyUser', on_delete=models.SET_NULL, null=True)
    action_type = models.CharField(max_length=50)  # e.g., 'created', 'updated', 'deleted'
    object_type = models.CharField(max_length=100)  # e.g., 'Booking', 'Service'
    object_id = models.PositiveIntegerField()  # ID of the affected object
    message = models.TextField(null=True, blank=True)  # Optional details about the action
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AuditLog {self.log_id} - {self.action_type} {self.object_type} {self.object_id}"

    class Meta:
        ordering = ['-timestamp']





