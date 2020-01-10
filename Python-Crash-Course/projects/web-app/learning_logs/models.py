from django.db import models

# Create your models here.
# This covers the topic that someone is writing about
class Topic(models.Model):
    """
    A topic that the user is learning about.
    """
    text = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.text

# This covers what a user has written about a Topic
class Entry(models.Model):
    """
    An entry that a user has written about a topic.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """
        Return a string representation of the model.
        In this case, the first 50 characters of the entry.
        """
        if len(str(self.text)) <= 50:
            return f"{self.text[:50]}"
        else:
            return f"{self.text[:50]}..."
