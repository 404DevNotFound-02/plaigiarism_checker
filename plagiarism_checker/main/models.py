from django.db import models

from django.contrib.auth.models import User
from django.db import models

class PlagiarismHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField()
    plagiarism_percentage = models.FloatField()
    checked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plagiarism_percentage}%"

