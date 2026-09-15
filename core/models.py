from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    phone=models.CharField(max_length=15,blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class employer(models.Model):
    company_name=models.CharField(max_length=100)
    company_description=models.TextField()
    company_location=models.CharField(max_length=100)
    company_website=models.URLField(max_length=200, blank=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    

class candidate(models.Model):
    phone=models.CharField(max_length=15,blank=True)
    resume=models.FileField(upload_to='resumes/', blank=True)
    cover_letter=models.TextField(blank=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    
    
class job(models.Model):
    title=models.CharField(max_length=100)
    job_description=models.TextField()
    job_type=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateField(auto_now_add=True)
    employer=models.ForeignKey(employer,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title   
    
class application(models.Model):
    status=models.CharField(max_length=100,default='pending')
    created_at=models.DateField(auto_now_add=True)
    candidate=models.ForeignKey(candidate,on_delete=models.CASCADE,related_name='candidate_applications')
    job=models.ForeignKey(job,on_delete=models.CASCADE,related_name='job_applications')
    
    def __str__(self):
        return f"{self.candidate.first_name} {self.candidate.last_name} applied for {self.job.title}"