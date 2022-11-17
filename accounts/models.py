from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin,BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
        	raise ValueError('Must include username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
        	username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """

        user = self.create_user(
			username=username,
			email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
	username = models.CharField(
	    max_length=255,
	    unique=True,
	)
	email = models.EmailField(
	    verbose_name='email address',
	    max_length=255,
	    unique=True,
	)
	first_name = models.CharField(
			max_length=120,
			null=True,
			blank=True,
			)
	last_name = models.CharField(
			max_length=120,
			null=True,
			blank=True,
			)
	phone_number = models.CharField(
			max_length=13,
			null=True,
			blank=True,
			unique=True,
			)
	is_partner=models.BooleanField(default=False)
	is_corner=models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	stat_member=models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	is_tap=models.BooleanField(default=False)
	loyalty_point= models.IntegerField(default=0)
	# last_online = models.DateTimeField(default=datetime.now, blank=True)
	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	@property
	def get_full_name(self):
	    # The user is identified by their email address
	    return "%s %s" %(self.first_name, self.last_name)

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.first_name

	def __unicode__(self):
	    return self.username

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin
	

	@property
	def is_superuser(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_superuser
	@property
	def is_stats(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.stat_member



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True,default=timezone.now)
    if settings.DEBUG:
    	photo = models.ImageField(upload_to=settings.PROFILE_URL, blank=True)
    else:
        photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=MyUser)