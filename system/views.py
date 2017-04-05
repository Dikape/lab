import random
import timeit

from django.shortcuts import render, redirect

from .forms import NumberForm


def index(request):
    if request.method == 'GET':
        form = NumberForm
        context = {'form': form}
    if request.method == "POST":
        start = timeit.default_timer()
        form = NumberForm(request.POST)
        number = 0
        matrix_a = []
        matrix_b = []
        matrix_c = []
        if form.is_valid():
            if form.cleaned_data:
                number = form.cleaned_data['number']
                for i in range(number):
                    matrix_a.append([random.randint(0, 10) for j in range(number)])
                    matrix_b.append([random.randint(0, 10) for j in range(number)])
                for i in range(number):
                    row = []
                    for j in range(number):
                        value = 0
                        for k in range(number):
                            value += (matrix_a[i][k]*matrix_b[k][j])
                        row.append(value)
                    matrix_c.append(row)
                    context = {'form': form,
                               'matrix_a': matrix_a,
                               'matrix_b': matrix_b,
                               'matrix_c': matrix_c}

        else:
            context = {'form': form}
        stop = timeit.default_timer()
        context['time'] = stop - start
    return render(request, 'index.html', context)