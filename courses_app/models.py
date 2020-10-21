from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['course_name'])<6:
            errors['course_name'] = "Course Name should be more than 5 characters long."
        if len(postData['description'])<16:
            errors['description'] = "Description should be more than 15 characters long."
        return errors


class Descriptions(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Courses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    description = models.OneToOneField(Descriptions, 
                                    on_delete=models.CASCADE,
                                    primary_key=True)
    
class Comments(models.Model):
    topic = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Courses, related_name="comments", on_delete=models.CASCADE)
    

    



    