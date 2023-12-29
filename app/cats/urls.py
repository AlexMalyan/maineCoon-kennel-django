from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [

    path("", views.index),
    # path("search/", views.PostSearchView.as_view(), name="post_search"),
    # path("<slug:post>/", views.post_single, name="post_single"),
    # path("tag/<slug:tag>/", views.TagListView.as_view(), name="tag_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
