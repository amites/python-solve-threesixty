# Pluggable set of Django models for Solve360

from django.conf import settings
from django.db import models


TAG_TYPES = (
    ('blog', 'Blog'),
    ('company', 'Company'),
    ('contact', 'Contact'),
)


FIELD_TYPES = (
    ('blog', 'Blog'),
    ('company', 'Company'),
    ('contact', 'Contact'),
)


class SolveThreeSixty(models.Model):
    class Meta:
        abstract = True


class ThreeSixtyContact(SolveThreeSixty):
    pass


class ThreeSixtyTag(SolveThreeSixty):
    type = models.CharField(max_length=30, help_text='Type of Tag',
                            choices=TAG_TYPES, blank=True, null=True)

    class Meta:
        unique_together = (('solve_id', 'type'), )
        ordering = ('type', )


class ThreeSixtyField(SolveThreeSixty):
    type = models.CharField(max_length=30, help_text='Type of Field',
                            choices=FIELD_TYPES, blank=True, null=True)

    class Meta:
        unique_together = (('solve_id', 'type'), )
        ordering = ('type', )


class ThreeSixtyUser(SolveThreeSixty):
    pass
