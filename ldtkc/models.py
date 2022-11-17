from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.text import slugify
from cloudinary_storage.storage import RawMediaCloudinaryStorage

from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

# from tinymce.models import HTMLField

    
#from phonenumber_field.modelfields import PhoneNumberField


COURSE_CHOICES = (
        ('Pick a Course','Pick a Course'),
        ('MS Excel [Basic & Intermediate]', 'MS Excel [Basic & Intermediate]'),
        ('MS Excel [Advanced Masterclass]', 'MS Excel [Advanced Masterclass]'),
        ('MS PowerPoint [Advanced Masterclass]', 'MS PowerPoint [Advanced Masterclass]'),
        (' Essential MS Excel for HR Professionals ', ' Essential MS Excel for HR Professionals '),
        (' Excel Dashboard for Business Intelligence ', ' Excel Dashboard for Business Intelligence '),
        ('Financial Modelling', 'Financial Modelling'),
        ('Web Design for Beginners', 'Web Design for Beginners'),
        (' Programming(Python)', ' Programming(Python)'),
        ('Web Design for Advance Learners', 'Web Design for Advance Learners'),
    )



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
        default=""
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        default="youremailisrequired",
        unique=True,
    )

    ip_address=models.CharField(max_length=120, default='ABC')
    mobile=models.CharField(max_length=13,null=True,blank=True,unique=True)
    sex=models.CharField(max_length=15,default='')
    company=models.CharField(max_length=550,default='')
    occupation=models.CharField(max_length=550, default='')
    pick_your_course=models.CharField(max_length=100,default='Pick a Course')
        
    start_course=models.DateTimeField(default=datetime.now()-timedelta(days=5))



    full_name=models.CharField(max_length=150,default='')


    is_member = models.BooleanField(default=False,
                    verbose_name='Is Paid Member')
    is_active = models.BooleanField(default=True)
    is_test_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_head = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return "%s" %(self.full_name)

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.first_name

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



class Registeration(models.Model):
    name = models.CharField(
	    max_length=255,
	    default=""
	)
    email = models.EmailField(
	    verbose_name='email address',
	    max_length=255,
	    default="",
	    unique=True, 
	)

    ip_address=models.CharField(max_length=120, default='ABC')
    sex=models.CharField(max_length=11,null=True,blank=True)
    mobile=models.CharField(max_length=11,null=True,blank=True)
    company=models.CharField(max_length=11,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    occupation=models.CharField(max_length=120,blank=True,null=True)
    pick_your_course=models.CharField(max_length=100,default='Pick a Course')
    is_test_user = models.BooleanField(default=False)
    def __str__(self):
        return 'Registeration Status for  {}'.format(self.name)


class PaymentStatus(models.Model):
    user = models.OneToOneField(MyUser,related_name="paypal_user",on_delete=models.CASCADE)
    pay33 = models.BooleanField(default=False)
    pay67= models.BooleanField(default=False)
    pay200 = models.BooleanField(default=False)
    #pay182=models.BooleanField(default=False)

    def __str__(self):
        return 'Payment Status for  {}'.format(self.user.username)

class Calendar(models.Model):
    user = models.ForeignKey(MyUser,related_name="calendar_user",on_delete=models.CASCADE)
    month = models.CharField(max_length=200,default=False)
    center = models.CharField(max_length=200,default=False)
    location = models.CharField(max_length=200,default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    content6 = models.TextField(blank=True)
    content7 = models.TextField(blank=True)

    def __str__(self):
        return 'Calendar for  {}'.format(self.user.username)


class Courses(models.Model):
    user = models.ForeignKey(MyUser,related_name="ldtkc_user",on_delete=models.CASCADE)
    heading = models.CharField(max_length=200,default=False)
    # benefit = models.CharField(max_length=1000,default=False)
    # target = models.CharField(max_length=500,default=False)
    write_up = models.TextField(default="")
    outline = models.FileField(upload_to='course_file/',max_length=10000,null=True,blank=True,storage=RawMediaCloudinaryStorage())
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='course_image/',blank=True,max_length=1000)

    def __str__(self):
        return '{} Courses for  {}'.format(self.heading,self.user.username)

class AddCourses(models.Model):
    user = models.ForeignKey(MyUser,related_name="addcourse_user",on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default=False)
    created_at=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return '{}'.format(self.title)

class Gallery(models.Model):
    user = models.ForeignKey(MyUser,related_name="ldtkc_gallery",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="gallery_image/",blank=True)

    def __str__(self):
        return 'Galllery Images for  {}'.format(self.user.username)



class Testimonial(models.Model):
    user = models.ForeignKey(MyUser,related_name="ldtkc_testimonial",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,default=False)
    testimonial = models.TextField(default=False)

    def __str__(self):
        return 'Testimonial for  {}'.format(self.name)



class Resources(models.Model):
    user = models.ForeignKey(MyUser,related_name="ldtkc_resource",on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default=False)
    content = models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='resource/',blank=True,max_length=1000,storage=RawMediaCloudinaryStorage())
    

    def __str__(self):
        return 'Resource for  {}'.format(self.user.username)



class SatisfiedClient(models.Model):
    user = models.ForeignKey(MyUser,related_name="ldtkc_satisfied",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='satisfied_client/',blank=True,)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return 'Resource for  {}'.format(self.user.username)



def create_paymentstatus(sender, **kwargs):
    if kwargs['created']:
        user_paystatus = PaymentStatus.objects.create(user=kwargs['instance'])

post_save.connect(create_paymentstatus, sender=MyUser)


class Profile(models.Model):
    user = models.OneToOneField(MyUser,related_name="profile_user",on_delete=models.CASCADE)
    hobby = models.CharField(max_length=100, default='')
    home_address = models.CharField(max_length=100, default='')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=MyUser)





class OnlineVideo(models.Model):
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to='online_video/',blank=True,max_length=1000,storage=VideoMediaCloudinaryStorage(),
                              validators=[validate_video])
    description = models.TextField()

    def __str__(self):
        return "%s online video"%self.title

class OnlineClass(models.Model):
    user = models.ForeignKey(MyUser, related_name="online_user",on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1500,default='')
    online_video = models.ForeignKey(OnlineVideo, default='',related_name="online_video",on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    def __str__(self):
        return "%s online video"%self.user

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(OnlineClass, self).save(*args, **kwargs)


# Test Class
class TestQuestion(models.Model):
    poster = models.ForeignKey(MyUser,default="", on_delete=models.CASCADE,related_name="user_test")
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.content)


class TestAnswer(models.Model):
    questions = models.ForeignKey(TestQuestion, on_delete=models.CASCADE,related_name="user_answer")
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
            
    def __str__(self):
        return "{}".format(self.correct_answer)

class PlayerStatistic(models.Model):
    player = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="user_stats")
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=500,default="")
    company=models.CharField(max_length=500,default="")
    mobile=models.CharField(max_length=15,default='',null=True,blank=True)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return "{} Candidate".format(self.name)