from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimestampedModel

User = get_user_model()

class Profile(TimestampedModel):
    class Gender(models.TextChoices):
        MALE = ("M", _("Male"),)
        FEMALE = ("F", _("Female"),)
        OTHER = ("O", _("Other"),)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(verbose_name=_("PhoneNumber"), max_length=30, blank=True, null=True)
    about_me = models.TextField(verbose_name=_("AboutMe"), default="Say something about yourself")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="KE", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"),max_length=20, default="Chittagong", blank=False, null=False)
    profile_photo= models.ImageField(verbose_name=_("ProfilePhoto"), default="/profile_default.png")
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    
    def follow(self,profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()