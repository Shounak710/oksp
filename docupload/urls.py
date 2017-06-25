from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^editor_choice/$', views.editor_choice, name='editor_choice'),
    url(r'^editor_choice/markdown$', views.markdown_editor, name='markdown_editor'),
    url(r'^editor_choice/wysiwyg$', views.wysiwyg_editor, name='wysiwyg_editor'),
    url(r'^(?P<doc_id>\d+)/$', views.display, name='upload'),
    url(r'^original/(?P<doc_id>\d+)/$', views.download_original, name='download_original'),
    url(r'^delete/(?P<doc_id>\d+)/$', views.delete, name='delete'),
]
