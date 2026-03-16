from django.db import models




class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField()
    tech_stack = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name