from django.shortcuts import redirect
from .models import Entry
from .forms import EntryForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView,ListView,DetailView,CreateView

class DashboardListview(ListView):
    model = Entry
    template_name = "Dashboard.html"
    context_object_name = "activites"

    #Par défaut Django recupere tout les activites. Mais avec get_queryset(), tu peux personnaliser ça.
    #Tu redéfinis la méthode utilisée par Django pour récupérer les données.
    def get_queryset(self):
        return Entry.objects.order_by('-created_at')[:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Activités du user connecté
        context['mes_activites'] = Entry.objects.filter(
            author=self.request.user
        ).order_by('-created_at')[:6]

        #STATISTIQUES GLOBALES
        context['total_activites'] = Entry.objects.count()

        context['bugs'] = Entry.objects.filter(
            category__name__iexact="bug"
        ).count()

        context['sprints'] = Entry.objects.filter(
            category__name__iexact="sprint"
        ).count()

        context['veilles'] = Entry.objects.filter(
            category__name__iexact="veille"
        ).count()

        return context

class ActiviteListview(ListView):
    model=Entry
    template_name="liste_activites.html"
    context_object_name="activites"
    paginate_by = 6

    def get_queryset(self):

        #On recupere la valeur de category dans l’URL (ex request=/activites/?category=bug)
        category = self.request.GET.get('category')

        if category:
            return Entry.objects.filter(
                category__name__iexact=category
            )

        return Entry.objects.all()

class AjouterActiviteView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'ajouter_activite.html'
    success_url = reverse_lazy('liste_activite')

    #Cette méthode est appelée quand le formulaire est valide.
    def form_valid(self, form):
        activite = form.save(commit=False)
        activite.author = self.request.user

        activite.save()

        #Django termine le traitement et fait la redirection.
        return super().form_valid(form)
    
class ActiviteUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    #Je veux modifier un objet de type Commentaire donc django sait quoi récupérer (get_object())
    model = Entry
    form_class = EntryForm
    template_name = 'activite_edit.html'
    success_url = reverse_lazy('liste_activite')

    def test_func(self):
        activite = self.get_object()
        return self.request.user == activite.author
    
class ActiviteDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Entry

    def post(self, request,*args, **kwargs):
        activite = self.get_object()
        activite.delete()
        return redirect('liste_activite')

    def test_func(self):
        activite = self.get_object()
        return self.request.user == activite.author

class DetailActiviteView(DetailView):
    model = Entry
    template_name = 'detail_activite.html'
    context_object_name = 'activite'