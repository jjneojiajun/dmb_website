from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    contact_email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    contact_no = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

