from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    reg_date = models.DateTimeField('Date published')
    content = models.TextField()
    # TextField: 긴 문자열

    def __str__(self):
        return self.title