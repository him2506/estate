from django.contrib import admin
from . models import Property,Prop_Image,Location,Agent

# Register your models here.



class LocationAdmin(admin.ModelAdmin):
    list_display = ('loc_id','name')
admin.site.register(Location,LocationAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id','agent_name','agent_ph')
admin.site.register(Agent,AgentAdmin)


class Prop_ImageAdmin(admin.StackedInline):
    model = Prop_Image


 
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [Prop_ImageAdmin]
 
    class Meta:
       model = Property
 
@admin.register(Prop_Image)
class Prop_ImageAdmin(admin.ModelAdmin):
    pass

