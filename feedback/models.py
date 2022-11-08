from django.db import models


class Feedbacks(models.Model):
    author = models.CharField(max_length=65)  # charfild = varchar
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.author
