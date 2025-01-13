from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PrimeForm

def is_prime(n):
    primes = [True] * (n + 1)  
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def input_page(request):
    form = PrimeForm()
    return render(request, 'primes/input.html', {'form': form})

def output_page(request):
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            primes = [num for num in range(2, number + 1) if is_prime(num)]
            return render(request, 'primes/output.html', {'primes': primes, 'number': number})
    return redirect(reverse('input_page'))