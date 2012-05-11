from django.db import models


class SolveThreeSixty(models.Model):
    solve_id = models.CharField(max_length=250, \
                        help_text='Solve 360 api key.', null=True)

    class Meta:
        abstract = True


class ThreeSixtyContact(SolveThreeSixty):
    pass

TAG_TYPES = (
    ('blog', 'Blog'),
    ('company', 'Company'),
    ('contact', 'Contact'),
)


class ThreeSixtyTag(SolveThreeSixty):
    type = models.CharField(max_length=30, help_text='Type of Tag', \
                            choices=TAG_TYPES, blank=True, null=True)

    class Meta:
        unique_together = (('solve_id', 'type'), )
        ordering = ('type', )

FIELD_TYPES = (
    ('blog', 'Blog'),
    ('company', 'Company'),
    ('contact', 'Contact'),
)


class ThreeSixtyField(SolveThreeSixty):
    type = models.CharField(max_length=30, help_text='Type of Field', \
                            choices=FIELD_TYPES, blank=True, null=True)

    class Meta:
        unique_together = (('solve_id', 'type'), )
        ordering = ('type', )


class ThreeSixtyUser(SolveThreeSixty):
    pass
