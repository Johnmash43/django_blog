from django.urls import path
from .views import *

urlpatterns = [

    path("dashboard", dashboard, name="dashboard"),
    path("categories", categories, name="categories"),
    # path("articles", articles, name="articles"),
    path("articles",ArticleListView.as_view(),name="articles"),##Class Based View
    path("create/article",ArticleCreateView.as_view(),name="article.create"),##Create View
    path("update/article/<pk>",ArticleUpdateView.as_view(),name="update.article"),
    path("delete/article/<id>", deleteArticle, name="delete.article"),
    path("feedback", feedback, name="feedback"),
    path("feedback/reply/<id>", replyFeedback, name="feedback.reply"),
    path("create/category/", createCategory, name="create.category"),
    path("delete/category/<id>", deleteCategory, name="delete.category")
]