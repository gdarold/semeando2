from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from cart.forms import CartAddDoacaoForm
from .models import TipoDoacao, Doacao


class DoacaoCreate(CreateView):
    model = Doacao
    fields = ['tipo_doacao', 'tipo_planta','titulo','descricao', 'imagem', 'peso',
              'quantidade']

    def form_valid(self, form):
        doacao = form.save(commit=False)
        doacao.doador = self.request.user

        doacao.save()

        return super(DoacaoCreate, self).form_valid(form)


class DoacaoDetailView(DetailView):
    queryset = Doacao.available.all()
    extra_context = {"form": CartAddDoacaoForm()}


class DoacaoListView(ListView):
    tipo_doacao = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Doacao.available.all()

        tipo_doacao_slug = self.kwargs.get("slug")
        if tipo_doacao_slug:
            self.tipo_doacao = get_object_or_404(TipoDoacao, slug=tipo_doacao_slug)
            queryset = queryset.filter(tipo_doacao=self.tipo_doacao)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_doacao"] = self.tipo_doacao
        context["tipos_doacoes"] = TipoDoacao.objects.all()
        return context


class DoacaoUser(ListView):
    model = Doacao

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        usuario = self.request.user.username
        return Doacao.objects.filter(doador=usuario)


class DoacaoEdit(UpdateView):
    model = Doacao
    fields = ['tipo_doacao', 'tipo_planta', 'titulo', 'descricao', 'imagem', 'peso',
              'quantidade', 'is_available']

