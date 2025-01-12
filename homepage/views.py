from django.shortcuts import render
from django.views.generic import TemplateView
from partners.forms import VolunteerForm, PartnerForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['volunteer_form'] = VolunteerForm()
        context['partner_form'] = PartnerForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'volunteer_submit' in request.POST:
            volunteer_form = VolunteerForm(request.POST)
            if volunteer_form.is_valid():
                volunteer_form.save()
                return render(request, self.template_name, {
                    'volunteer_form': VolunteerForm(),
                    'partner_form': PartnerForm(),
                    'success_message': 'Thank you for volunteering!',
                })
        elif 'partner_submit' in request.POST:
            partner_form = PartnerForm(request.POST)
            if partner_form.is_valid():
                partner_form.save()
                return render(request, self.template_name, {
                    'volunteer_form': VolunteerForm(),
                    'partner_form': PartnerForm(),
                    'success_message': 'Thank you for partnering with us!',
                })

        # If forms are invalid, return with errors
        return render(request, self.template_name, {
            'volunteer_form': VolunteerForm(request.POST),
            'partner_form': PartnerForm(request.POST),
        })
