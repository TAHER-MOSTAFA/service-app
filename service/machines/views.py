from django.views.generic import TemplateView, RedirectView
from service.machines.models import Company, Machine, WishList, Category, Conatact
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from service.machines.forms import ContactForm


class HomeView(TemplateView):
    template_name = "machines/home.html"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['machines1'] = Machine.objects.all().order_by('-rate')[:3]
        context['machines2'] = Machine.objects.all().order_by('-rate')[3:6]
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        form = ContactForm(self.request.POST)
        
        if form.is_valid():
            Conatact.objects.create(**form.cleaned_data)
            context['message'] = "تم تسجيل رسالتك !"
        else:
            print(form.errors.items())
            context['errors'] = form.errors
        return self.render_to_response(context)

class CompanyView(TemplateView):
    template_name = "machines/company.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, id=self.kwargs['id'])
        context['machines'] = list(context['company'].machine_set.select_related('category').order_by('category'))
        return context
    
class MachineView(TemplateView):
    template_name = "machines/machine.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machine'] = get_object_or_404(Machine, id=self.kwargs['id'])
        context['related_machines'] = Machine.objects.filter(
            category=context['machine'].category
            ).exclude(id=context['machine'].id)[:3]
        
        if self.request.GET.get("msg", False):
            context['message'] = "تم اضافة الماكينة الى المفضلة الخاصة بك"
        return context
    
    

class AddToWishListView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'machine'

    def get_redirect_url(self, *args, **kwargs):
        wishlist, _ = WishList.objects.get_or_create(user=self.request.user)
        machine = get_object_or_404(Machine, id=kwargs['id'])
        wishlist.machines.add(machine)
        self.request.META['QUERY_STRING'] = "msg=True"
        return super().get_redirect_url(*args, **kwargs)


class WishListView(LoginRequiredMixin, TemplateView):
    template_name = "machines/favs.html"
    
    def post(self, request, *args, **kwargs):
        pass
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = WishList.objects.get_or_create(user=self.request.user)[0].machines.all()
        return context


class SearchView(TemplateView):
    template_name = "machines/search.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET["q"]
        context['machines'] = Machine.objects.filter(name__icontains=self.request.GET["q"])
        return context

    
    
class ContactUs(TemplateView):
    template_name = "machines/contact.html"
  
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ContactForm(self.request.POST)
        if form.is_valid():
            Conatact.objects.create(**form.cleaned_data)
            context['message'] = "تم تسجيل رسالتك !"
        else:
            context['errors'] = form.errors
        return self.render_to_response(context)
    
    
class CategoryView(TemplateView):
    template_name = "machines/category.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['id'])
        context['machines'] = Machine.objects.filter(category_id=self.kwargs['id'])
        return context
