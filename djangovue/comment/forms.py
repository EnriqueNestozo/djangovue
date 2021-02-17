from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text' : Textarea(attrs = {'class': 'form-input'})
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].widget.attrs.update({'class': 'form-input'})

    #podemos sobreescribir el metodo save si queremos agregar algo antes de guardar en la bd.
    def save(self, commit=True, text=""):
        instance = super(CommentForm, self).save(commit=commit)

        if(text == ""):
            instance.text = text

        if(commit):
            instance.save()

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', initial='pepe', required=True, disabled=False, help_text='Aquí va el nombre', max_length=10, min_length=2)