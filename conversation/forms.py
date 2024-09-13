from django import forms

from .models import ConvesationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConvesationMessage
        fields = ("content",  )
        widget = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }