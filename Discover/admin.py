from django.contrib import admin
from .models import WorkerfyUser, Tradesperson, Client, TradeType, TradespersonCategory,\
      Feature, JobPosting, Application, Booking, Service, Payment, Dispute, Review, Notification, AuditLog,\
      PastWorkImage

# Register your models here.
admin.site.register(PastWorkImage)

# Register your models here.
@admin.register(WorkerfyUser)
class WorkerfyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type')
    search_fields = ('email', 'user_type')

@admin.register(Tradesperson)
class TradespersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'location', 'years_of_experience', 'availability_status')
    search_fields = ('first_name', 'last_name', 'middle_name', 'location', 'specialization')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'location', 'created_date')
    search_fields = ('first_name', 'last_name', 'middle_name', 'location')

@admin.register(TradeType)
class TradeTypeAdmin(admin.ModelAdmin):
    list_display = ('trades_name',)
    search_fields = ('trades_name',)

@admin.register(TradespersonCategory)
class TradespersonCategoryAdmin(admin.ModelAdmin):
    list_display = ('tradesperson',)
    filter_horizontal = ('trade_types',)  # For easy many-to-many selection

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_name',)
    search_fields = ('feature_name',)

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'client', 'location', 'job_start', 'job_end', 'budget', 'payment_type', 'application_deadline', 'created_at')
    list_filter = ('payment_type', 'location', 'job_start', 'job_end', 'created_at')
    search_fields = ('job_title', 'client__first_name', 'location', 'skills_required')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'job_posting', 'tradesperson', 'application_date', 'status')
    list_filter = ('status', 'application_date')
    search_fields = ('job_posting__job_title', 'tradesperson__first_name', 'status')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'client', 'tradesperson', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('client__first_name', 'tradesperson__first_name', 'status')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'booking', 'service_start', 'service_status', 'flag')
    list_filter = ('service_status', 'service_start', 'flag')
    search_fields = ('booking__client__first_name', 'booking__tradesperson__first_name', 'service_status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'service', 'client', 'amount', 'payment_method', 'payment_status', 'upfront_payment', 'timestamp')
    list_filter = ('payment_status', 'payment_method', 'upfront_payment')
    search_fields = ('client__first_name', 'transaction_id')

@admin.register(Dispute)
class DisputeAdmin(admin.ModelAdmin):
    list_display = ('dispute_id', 'service', 'client', 'tradesperson', 'dispute_status', 'initiator', 'created_date', 'resolved_date')
    list_filter = ('dispute_status', 'initiator')
    search_fields = ('service__service_id', 'client__first_name', 'tradesperson__first_name')

admin.site.register(Review)

admin.site.register(Notification)

admin.site.register(AuditLog)