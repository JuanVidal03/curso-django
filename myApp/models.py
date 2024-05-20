from django.db import models


# modelo proyectos
class Project(models.Model):
    name = models.CharField(max_length=200)
    

# modelo de tareas
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)