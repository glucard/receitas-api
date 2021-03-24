from rest_framework.routers import DefaultRouter
from .views import ReceitasViewSet, ReceitasChefViewSet, SearchReceitasViewSet

router = DefaultRouter()
router.register(r'receitas', ReceitasViewSet, basename='receitas')
router.register(r'chef-receitas/(?P<chef_id>\d+)', ReceitasChefViewSet, basename='receitas_chef')
router.register(r'search-receitas/(?P<search_name>[\w\-]+)', SearchReceitasViewSet, basename='search_receitas')

receitas_urls = router.urls