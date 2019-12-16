from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View

from .models import Student
from .forms import StudentFrom

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentFrom()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

        context = self.get_context()
        context.update({
            'form': form
        })

        return render(request, self.template_name, context=context)


# def index(request):
#     students = Student.objects.all()
#     return render(request, 'index.html', context={'students': students})

# def index(request):
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentFrom()
#
#     context = {
#         'students': students,
#         'form': form,
#     }
#
#     return render(request, 'index.html', context=context)

