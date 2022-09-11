from django.db import models

# Create your models here.


class Location(models.Model):
    loc_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to = 'static/images/')

    def __str__(self):
        return self.name


class Agent(models.Model):
    agent_id = models.AutoField(primary_key = True)
    agent_name = models.CharField(max_length=1000,default="")
    agent_ph = models.CharField(max_length=1000,default="")
    agent_whts = models.CharField(max_length=1000,default="")
    agent_desc = models.CharField(max_length=1000,default="")

    def __str__(self) -> str:
        return self.agent_name


class Property(models.Model):
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    prop_id = models.AutoField(primary_key = True)
    prop_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    latest = models.BooleanField(default=True)
    desc = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    loc_link = models.CharField(max_length=1000,default="")
    prop_type = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    area = models.CharField(max_length=1000)
    mark_price = models.CharField(max_length=1000)
    our_price = models.CharField(max_length=1000)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)

    # upload_to me img wo folder h jahan images upload hongi.
    image = models.FileField(upload_to = 'static/images/')
    

    

    def __str__(self):
        return self.prop_name
    
class Prop_Image(models.Model):
    prop = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'static/images/')
 
    def __str__(self):
        return self.prop.prop_name

    