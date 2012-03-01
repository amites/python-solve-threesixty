from django.db import models

class SolveThreeSixty(models.Model):
    solve_id = models.CharField(max_length=250, help_text='Solve 360 key for a contact.', null=True)
