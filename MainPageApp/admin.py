from django.contrib import admin

# Register your models here.
""" from .models import TradeCategory, TradeSpecialty, TradeSkillTag, TradespersonProfile, Area, City, Region
 """
""" admin.site.register(TradeCategory)
admin.site.register(TradeSpecialty)
admin.site.register(TradeSkillTag)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Area)

@admin.register(TradespersonProfile)
class TradespersonProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    filter_horizontal = ['trade_specialties', 'skills'] """