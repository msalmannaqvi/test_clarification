from django import forms
from .models import ClarificationType, ClarificationCategory, ClarificationFiles, General, Assign_To, Rfx


class ClarificationTypeForm(forms.ModelForm):
    class Meta:
        model = ClarificationType
        fields = '__all__'


class ClarificationForm(forms.ModelForm):
    class Meta:
        model = ClarificationCategory
        fields = '__all__'


class ClarificationFileform(forms.ModelForm):
    class Meta:
        model = ClarificationFiles
        fields = ['files']


class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign_To
        fields = '__all__'


class RfxForm(forms.ModelForm):
    class Meta:
        model = Rfx
        fields = '__all__'


class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = '__all__'
