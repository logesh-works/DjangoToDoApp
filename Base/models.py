from django.db import models

class Details(models.Model):
    Task_name = models.CharField("Task Name",max_length=250)
    Task_status = models.BooleanField("Task Status",default=False)

    def __str__(self) -> str:
        return self.Task_name

