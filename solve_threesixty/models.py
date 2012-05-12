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

PRIMARY_FIELD_TYPES = (
    ('blog', 'Blog'),
    ('company', 'Company'),
    ('contact', 'Contact'),
)

INPUT_FIELD_TYPE = (
    ('sectionbreak', 'sectionbreak'),
    ('textarea', 'textarea'),
    ('None', 'None'),
    ('text', 'text'),
    ('html', 'html'),
    ('phonenumber', 'phonenumber'),
    ('date', 'date'),
    ('multiselect', 'multiselect'),
    ('email', 'email'),
    ('select', 'select')
)

class ThreeSixtyField(SolveThreeSixty):
    solve_name = models.CharField(max_length=250,\
                            help_text='Solve360 field name.', null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=30, help_text='Primary type of Field' \
                            +'(' + ' / '.join([f[0] for f in PRIMARY_FIELD_TYPES]) + ')',\
                            choices=PRIMARY_FIELD_TYPES, blank=True, null=True)
    field_type = models.CharField(max_length=30, help_text='Field input type', \
                            choices=INPUT_FIELD_TYPE, blank=True, null=True)

    class Meta:
        unique_together = (('solve_id', 'type'), )
        ordering = ('type', )

    def addField(self, row, field_type='contact'):
        """
        Add's a field to the django model.
        Field's type defauits to contact
        """
        try:
            self = ThreeSixtyField.objects.get(solve_id = row['id'])
        except ThreeSixtyField.DoesNotExist:
            pass
        self.solve_id = row['id']
        self.solve_name = row['name']
        self.name = row['label']
        self.type = field_type
        self.field_type = row['type']
        self.save()

        try:
            for option in row['options']:
                try:
                    ThreeSixtyFieldOptions.objects.get(\
                            name=option, field = self)
                except ThreeSixtyFieldOptions.DoesNotExist:
                    option_obj = ThreeSixtyFieldOptions(
                        name = option,
                        field = self
                    )
                    option_obj.save()
        except KeyError:
            pass
        return self


class ThreeSixtyFieldOptions(models.Model):
    name = models.CharField(max_length=150)
    field = models.ForeignKey(ThreeSixtyField)

    class Meta:
        unique_together = (('name', 'field', ))


class ThreeSixtyUser(SolveThreeSixty):
    name = models.CharField(max_length=150, help_text='Solve360 User Name',
                            blank=True, null=True)
    email = models.CharField(max_length=250,
                            help_text='Solve360 User Email address',
                            blank=True, null=True)
    group = models.BooleanField(help_text='Is this a Solve360 User Group?',
                            default=False)

    def addUser(self, row, group=False):
        self.solve_id = row['id']
        self.email = row['email']
        self.name = row['name']
        self.group = group
        self.save()
        return self