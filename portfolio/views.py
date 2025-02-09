# portfolio/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Portfolio
import pandas as pd
from collections import defaultdict

@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    grouped_portfolios = defaultdict(list)
    total_amount = 0
    total_amount_aed = 0
    total_amount_inr = 0

    for portfolio in portfolios:
        grouped_portfolios[portfolio.financial_institution].append(portfolio)
        total_amount += portfolio.amount
        total_amount_aed += portfolio.amount_in_aed()
        total_amount_inr += portfolio.amount_in_inr()

    subtotals = {}
    for institution, items in grouped_portfolios.items():
        subtotal_amount = sum(item.amount for item in items)
        subtotal_amount_aed = sum(item.amount_in_aed() for item in items)
        subtotal_amount_inr = sum(item.amount_in_inr() for item in items)
        subtotals[institution] = {
            'amount': subtotal_amount,
            'amount_aed': subtotal_amount_aed,
            'amount_inr': subtotal_amount_inr,
        }

    context = {
        'grouped_portfolios': dict(grouped_portfolios),
        'subtotals': subtotals,
        'total_amount': total_amount,
        'total_amount_aed': total_amount_aed,
        'total_amount_inr': total_amount_inr,
    }

    return render(request, 'portfolio/portfolio_list.html', context)

@login_required
def upload_portfolio(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            Portfolio.objects.create(
                user=request.user,
                financial_institution=row['Financial Institution'],
                currency=row['Currency'],
                asset=row['Asset'],
                title=row['Title'],
                rate=row['Rate'],
                maturity_date=row['Maturity Date'],
                amount=row['Amount']
            )
        return redirect('portfolio_list')
    return render(request, 'portfolio/upload_portfolio.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})