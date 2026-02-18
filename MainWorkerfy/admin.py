from django.contrib import admin

# Register your models here.
from .models import TradeCategory, TradeSpecialty, TradeSkillTag, TradespersonProfile, Area,\
      City, Region, EarnedBadge, Certificate, Badge, PortfolioItem, Country, JobPost, JobPostAttachment, ClientProfile

admin.site.register(TradeCategory)
admin.site.register(TradeSpecialty)
admin.site.register(TradeSkillTag)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(PortfolioItem)
admin.site.register(Country)
admin.site.register(JobPost)
admin.site.register(JobPostAttachment)
admin.site.register(ClientProfile)


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['tradesperson', 'title', 'issue_date']
    search_fields = ['tradesperson__user__username', 'name']
    list_filter = ['issue_date']

@admin.register(EarnedBadge)
class EarnedBadgeAdmin(admin.ModelAdmin):
    list_display = ['tradesperson', 'badge', 'awarded_on']
    search_fields = ['tradesperson__user__username', 'badge__name']
    list_filter = ['awarded_on']


@admin.register(TradespersonProfile)
class TradespersonProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    filter_horizontal = ['trade_specialties', 'skills']