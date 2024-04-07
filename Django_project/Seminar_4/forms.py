import datetime

from django import forms


class GameForm(forms.Form):
    game_type = forms.ChoiceField(choices=(('coin', 'монетка'), ('cube', 'кубик'), ('number', 'число')))
    num_tries = forms.IntegerField(min_value=1, max_value=64)

    # Выбор из базы данных
    # author = forms.ModelChoiceField(label='Author', queryset=Author.objects.all())


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Биография автора'}
        ),
    )
    birthday = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
    )
