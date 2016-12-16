from django import forms
from django.core.validators import URLValidator



def validate_url(value):
	url_validator = URLValidator()
	try:
		url_validator(value)
	except:
		raise ValidationError("Invalid URL for this field")
	return value


class SubmitUrlForm(forms.Form):
	url = forms.CharField(label="Submit Form", validators=[validate_url])

	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean()
	# 	url = cleaned_data.get('url')
	# 			url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Url invalida para este campo")		
	# 	return url

	# def clean_url(self):
	# 	url =self.cleaned_data['url']
	# 	print(url)
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Url invalida para este campo")		
	# 	return url