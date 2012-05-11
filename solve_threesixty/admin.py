from django.contrib import admin
from solve_threesixty.models import ThreeSixtyContact, ThreeSixtyField, \
    ThreeSixtyTag, ThreeSixtyUser

class ThreeSixtyContactAdmin(admin.Admin):
    actions_on_top = True


class ThreeSixtyFieldAdmin(admin.Admin):
    actions_on_top = True
    list_display = ('solve_id', 'type', )
    list_filter = ('type', )
    radio_fields = ('type')


class ThreeSixtyTagAdmin(admin.Admin):
    actions_on_top = True
    list_display = ('solve_id', 'type', )
    list_filter = ('type', )
    radio_fields = ('type')


class ThreeSixtyUserAdmin(admin.Admin):
    actions_on_top = True


admin.site.register(ThreeSixtyContact, ThreeSixtyContactAdmin)
admin.site.register(ThreeSixtyField, ThreeSixtyFieldAdmin)
admin.site.register(ThreeSixtyTag, ThreeSixtyTagAdmin)
admin.site.register(ThreeSixtyUser, ThreeSixtyUserAdmin)
