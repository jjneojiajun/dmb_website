from .forms import ContactForm
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import send_mail
from django.contrib import messages



def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

        send_mail(
            'Thank you for contact us',
            'Dear %s Please allow us 3 days to contact you!' % (contact_name),
            'messanger@localhost.com',
            [contact_email],
            fail_silently=False,
        )

        send_mail(
            'Customer %s Message' %(contact_name),
            form_content,
            'messanger@localhost.com',
            ['rockjj93@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us')

    return render(request, 'contact_us.html', {'form': form_class})