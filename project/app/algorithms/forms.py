from django.forms.models import ModelForm
from app.algorithms.models import Algorithm

class AlgorithmRunningTimeForm (ModelForm):
    class Meta:
        model = Algorithm
        fields = ('time_best_case', 'time_worst_case')