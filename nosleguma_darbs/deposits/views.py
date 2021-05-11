from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)

from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
)

from django.urls import reverse_lazy

from deposits.models import Deposit
from deposits.forms import DepositForm


class DepositListView(ListView):
    model = Deposit
    template_name = 'index.html'
    context_object_name = 'deposits'

    def get_queryset(self):
        return Deposit.objects.all()


class AddDepositFormView(FormView):
    form_class = DepositForm
    template_name_get = 'form.html'
    template_name_post = 'index.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
        }

        return render(
            request=request,
            template_name=self.template_name_get,
            context=context,
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            deposit = Deposit(
                deposit=request.POST['deposit'],
                term=request.POST['term'],
                rate=request.POST['rate'],
            )

            deposit.save()

            context = {
                'deposits': Deposit.objects.all(),
            }

            return render(
                template_name=self.template_name_post,
                request=request,
                context=context,
            )


class ShowDepositView(DetailView):
    model = Deposit
    template_name = 'show.html'
    context_object_name = 'deposit'