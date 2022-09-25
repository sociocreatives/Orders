from django.urls import path
from . import views

urlpatterns = [
    path('orders/',views.OrderView.as_view(),name='orders'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('faq/',views.FaqView.as_view(),name='faq'),
    path('terms/',views.TermsView.as_view(),name='terms'),
    path('partners/',views.PartnersView.as_view(),name='partners'),
    path('order/<int:order_id>/',views.OrderIdView.as_view(),name='order'),
    path('update-status/<int:order_id>/',views.UpdateOrderStatusView.as_view(),name='update_order_status'),
    path('user/<int:user_id>/orders',views.UserOrdersView.as_view(),name='users_orders'),
    path('user/<int:user_id>/order/<int:order_id>/',views.UserOrderDetailView.as_view(),name='user_order_detail'),
]
