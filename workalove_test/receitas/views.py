from .models import Receita
from .serializers import ReceitaSerializer, ReadOnlyReceitaSerializer
from rest_framework import viewsets

class ReceitasViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Retorna a dada receita. 

    list:
    Retorna uma lista com todas as receitas.
    """
    queryset = Receita.objects.all().select_related('chef')
    serializer_class = ReadOnlyReceitaSerializer

class ReceitasChefViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Retorna uma dada receita do chefe_id.

    list:
    Retorna uma lista com todos as receitas do chefe_id.

    Create:
    Cria uma nova receita.
    """
    serializer_class = ReceitaSerializer
    
    def get_queryset(self):
        """
        Retorna um uma lita com todas as receitas que estão relacionados
        ao chefe_id, dado na url.
        """
        chef_id = self.kwargs['chef_id']
        return Receita.objects.filter(chef=chef_id)

class SearchReceitasViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrive:
    não usado.

    list:
    Retorna uma lista com os resultados da busca.
    """
    serializer_class = ReadOnlyReceitaSerializer
    
    def get_queryset(self):
        """
        Retorna uma lista com todas as receitas que possuem o valor
        de search_name. O search_name é especificado na url. 
        """
        search_name = self.kwargs['search_name']
        receitas = Receita.objects.all()
        queryset = [receita for receita in receitas if search_name.lower() in receita.nome.lower()]
        return queryset
