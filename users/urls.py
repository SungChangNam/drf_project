from pydoc import visiblename
from users import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_vlew"),
    path("mock/", views.mockView.as_view(), name="mockView"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name="Follow_view."),
    path('<int:user_id>/', views.ProfileView.as_view(), name="profile_view."),
    
    
]