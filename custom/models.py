from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.

GENDER_CHOICES = (
    ('f', 'female'),
    ('m', 'male'),
    ('r', 'rather not say ')
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

	
	
    email = models.EmailField(
        verbose_name='email address',max_length=255,unique=True
    )
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(
        upload_to="customer_images", null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, 
        null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser
    username = None
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

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
        return self.staff

    @property
    def is_mentor(self):
        "Is the user a is_superuser member?"
        return self.is_superuser


class Question(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    text = models.TextField()
    attachment = models.FileField(upload_to="attachments", null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    cr_date = models.DateField(auto_now=True)
    up_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def answer(self):
        return self.answer_set.all().values('ans', 'mentor', 'cr_date', 'up_date')
        


class Answer(models.Model):
    ans = models.TextField(null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.SET(value='Deleted'))
    cr_date = models.DateField(auto_now=True)
    up_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.ans

    @property
    def student(self):
        return self.question.student.email