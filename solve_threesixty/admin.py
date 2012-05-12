from django.contrib import admin
from solve_threesixty.models import ThreeSixtyContact, ThreeSixtyTag, \
                                    ThreeSixtyField, ThreeSixtyUser


class ThreeSixtyContactAdmin(admin.ModelAdmin):
    actions_on_top = True


class ThreeSixtyFieldAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ('solve_id', 'type', )
    list_filter = ('type', )
    radio_fields = {'type' : admin.VERTICAL}


class ThreeSixtyTagAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ('solve_id', 'type', )
    list_filter = ('type', )
    radio_fields = {'type' : admin.VERTICAL}


class ThreeSixtyUserAdmin(admin.ModelAdmin):
    actions_on_top = True


admin.site.register(ThreeSixtyContact, ThreeSixtyContactAdmin)
admin.site.register(ThreeSixtyTag, ThreeSixtyTagAdmin)
admin.site.register(ThreeSixtyField, ThreeSixtyFieldAdmin)
admin.site.register(ThreeSixtyUser, ThreeSixtyUserAdmin)
