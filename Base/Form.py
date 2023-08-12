from django.forms import *
from .models import Details

class detailsform(ModelForm):
    class Meta:
        model= Details
        fields = '__all__'