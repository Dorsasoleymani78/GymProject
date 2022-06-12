from .models import Period,Coach
from django import forms
class PeriodForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PeriodForm ,self).__init__(*args, **kwargs)
        self.fields['coach'].queryset = Coach.objects.filter(
            majorName__majorName=self.instance.major)