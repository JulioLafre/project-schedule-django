from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms


class ContactForm(forms.ModelForm):
    first_name  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Veio do Init'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuário'
    )

    qualquer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Veio do Init'
            }
        ),
        help_text='Texto de ajuda para o usuário'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Veio do Init'
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
                     
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()

