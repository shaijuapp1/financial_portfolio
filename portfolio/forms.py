from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['financial_institution', 'currency', 'asset', 'title', 'rate', 'maturity_date', 'amount']