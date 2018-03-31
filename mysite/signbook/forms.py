from django import forms



class CommentForm(forms.Form):
	name = forms.CharField(max_length=20, widget=forms.TextInput())
	comment = forms.CharField(widget=forms.Textarea())

