from django import forms


# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True,widget=forms.TextInput(
    	attrs={
    	'class':'form-control',
    	'placeholder':'Name',
    	}))
    Email = forms.EmailField(required=True,widget=forms.TextInput(
    	attrs={
    	'class':'form-control',
    	'placeholder':'Email Address',
    	}))
    Mobile_No=forms.IntegerField(required=True,error_messages={'required': 'Enter a valid mobile number'},widget=forms.TextInput(
    	attrs={
    	'class':'form-control',
    	'placeholder':'Phone Number',
    	}))
    Message = forms.CharField(required=True,widget=forms.Textarea(
		attrs={
    	'class':'form-control',
    	'placeholder':'Message',
        'rows':5,
    	}))