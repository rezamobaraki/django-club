from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from accounts import views

app_name = 'accounts'

api_urls = [
    # path('token-auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_urls))
]


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzUwMjcxMCwianRpIjoiYjIyMmY3Y2VlYTU1NGY0MTg3YmI2YjI2YWFjYzJjN2MiLCJ1c2VyX2lkIjoxfQ.lpbuDv7z_vSzACBCQk9iqtJyruD_jY9GevUZG0n_7TU",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzNDE2NjEwLCJqdGkiOiIwYmJiNjM4YzdkYWQ0MTYxYjYyOTVhYjZjYjRlNjMxOCIsInVzZXJfaWQiOjF9.HsmUgkWvgcXWqolWJ1pRukgaKxgeGwjUDIC7k0pMiqo"
# }