from django.db import models
from solve_threesixty.api import Solve360


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
    name = models.CharField(max_length=150, help_text='Solve360 User Name',
                            blank=True, null=True)
    email = models.CharField(max_length=250,
                            help_text='Solve360 User Email address',
                            blank=True, null=True)
    group = models.BooleanField(help_text='Is this a Solve360 User Group?',
                            default=False)
#
#    def addUser(self, row, group=False):
##        try:
##            self =
#        self.solve_id = row['id']
#        self.email = row['email']
#        self.name = row['name']
#        self.group = group
#        self.save()
#        return self