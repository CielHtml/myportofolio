import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_LEVELS = [
        ('sd', 'Elementary School'),
        ('smp', 'Junior High School'),
        ('sma', 'Senior High School'),
        ('kuliah', 'College')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution_name = models.CharField(max_length=255)
    description = models.TextField()
    education_levels = models.CharField(max_length=20, choices=EDUCATION_LEVELS)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.CharField(max_length=4)
    ended_at = models.CharField(max_length=20, default="Sekarang")
    def __str__(self):
        return self.institution_name
