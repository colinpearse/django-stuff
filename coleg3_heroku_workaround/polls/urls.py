from django.conf.urls import url

from . import views

# Description of url() lines:
# ex: /polls/
# ex: /polls/5/  NOTE: the 'name' value as called by the {% url %} template tag
# ex: /polls/5/results/
# ex: /polls/5/vote/
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
