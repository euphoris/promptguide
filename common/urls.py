from django_distill import distill_path
from django.urls import path
from . import views

app_name = 'common'


def guide_ids():
     for guide in views.guides.values():
        yield {'guide_id': guide['id']}


urlpatterns = [
    distill_path('', views.home, name='home'),
    path('prompt/', views.list_prompts, name='list_prompts'),
    path('prompt/<str:prompt_id>', views.view_prompt, name='view_prompt'),
    distill_path('guide/', views.list_guides, name='list_guides'),
    distill_path('guide/<str:guide_id>/', views.view_guide, name='view_guide', distill_func=guide_ids),
]
