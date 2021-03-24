from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import(TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy

from . import forms
from django.contrib.auth.models import User
# Create your views here.
from .forms import UserCreateForm, HelperCreateForm,RequestForm
from django.contrib import messages

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        p_reg_form = HelperCreateForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()

            p_reg_form = HelperCreateForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
        p_reg_form = HelperCreateForm()
    context = {
        'form': form,
        'p_reg_form': p_reg_form
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST, instance=request.user)
        profile_form = HelperCreateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('accounts:about')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserCreateForm(instance=request.user)
        profile_form = HelperCreateForm(instance=request.user.profile)
    return render(request, 'accounts/user_changes.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def contactView(request):
    #emails = User.objects.all().select_related('profile').filter(verified = "Yes").values_list('email', flat=True)
    #print(f"Emails: {emails}")
    if request.method == 'GET':
        form = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            city = form.cleaned_data['city']
            try:

                send_mail(subject, message, from_email, [''])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('accounts:success')
    return render(request, "accounts/request.html", {'form': form})

class successView(TemplateView):
    template_name = 'accounts/success.html'