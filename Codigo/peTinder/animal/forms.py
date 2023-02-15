from animal.models import Animal
from django import forms

SEXO_ESCOLHAS = {
        ("M", "Masculino"),
        ("F", "Feminino")
    }

class RegistroAnimalForm( forms.ModelForm ):
    sexo = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect(attrs={'class':'notapply'}),
        choices=SEXO_ESCOLHAS,
    )
    class Meta:
        model = Animal
        exclude = ['dono']
