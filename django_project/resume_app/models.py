from django.db import models

# Create your models here.

# This is the model for the Contacts


class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    from_email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.contact_name + 'with the email' + self.from_email + 'says\n' + self.message
