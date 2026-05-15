from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    
                                                                                   
    path('api/user-data/', views.api_data_view, name='api_data'),
    path('api/all-users/', views.all_users_data_view, name='all_users_data'),
    
    path('logout/', views.logout_view, name='logout'),
    path('lesson/', views.sensitive_data_exposure_lesson, name='lesson'),
    
                                          
                                                                                             
                                                              
                                                                              
]

                                                                    
                                                                 
                                                            

                                                                
                          
