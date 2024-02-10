

from django.urls import path
from . import views

urlpatterns = [
    # path('details/<int:id>', views.details,name="post_details"),
    path('details/<int:id>', views.PostDetailsView.as_view(),name="post_details"),
    path('buy_now/<int:id>', views.buy_now,name="buy_now"),
    path('order_history/', views.order_history,name="order_history"),


    
    

    # path('experiment_pass/', views.experiment_pass,name="experiment_pass"),
]
