""" from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# Main1 : models for the Trades types
User = get_user_model() # This will use the custom user model if one is defined, otherwise it will use the default User model.


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.region.name}"


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.city.name}"
    
"""
#1. TradeCategory
#Represents the main trade field (e.g., Carpentry, Plumbing, Electrical).

#Used to group related specialties.

#Selected as the primary category for a tradesperson.
"""
class TradeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Trade Categories"

    def __str__(self):
        return self.name

"""
#2. TradeSpecialty
#A subcategory under a trade category (e.g., Roofing under Carpentry).

#Tradespeople can select multiple specialties.

#Linked to TradeCategory with a ForeignKey.

#Enables specific filtering and search (e.g., find a roofer or cabinet maker).
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
#3. TradeSkillTag
#Free-form tags for detailed skill attributes (e.g., Smart Lighting, PVC Pipes, Roof Truss).

#Helps with flexible keyword search and extra filtering.

#Many-to-many relationship with TradespersonProfile.
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
        return f"{self.name} ({self.category.name})"
    

        

"""#4. TradespersonProfile
#Represents the user’s professional profile on Workerfy.

#Linked to:

#One main TradeCategory (via ForeignKey)

#Many TradeSpecialties (via ManyToManyField)

#Many TradeSkillTags (via ManyToManyField)

#Stores the core professional identity of the tradesperson.
"""
class TradespersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trade_category = models.ForeignKey(
        TradeCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tradespeople"
    )
    # Uncomment the following line if you want to allow multiple trade categories per tradesperson
    #trade_categories = models.ManyToManyField(TradeCategory, related_name="tradespeople", blank=True)

    trade_specialties = models.ManyToManyField(
        TradeSpecialty, 
        related_name="tradespeople"
    )

    skills = models.ManyToManyField(
        TradeSkillTag, 
        blank=True, 
        related_name="tradespeople"
    )
    
    work_areas = models.ManyToManyField(Area, related_name="tradespeople")

    def __str__(self):
        return self.user.get_full_name()



 """