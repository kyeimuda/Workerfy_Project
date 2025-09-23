from django.urls import path
from . import views

urlpatterns = [
        path('', views.Intro_home, name='Intro_home'),
        path('onboardings', views.onBoardings, name='Onboardings'),
        path('Sign_up', views.sign_up, name='Signup'),
        path('login', views.login_view, name='Login'),
        path('get_started', views.get_started, name='Get_started'),
        
        path('TradespeopleRegistration', views.tradesPeopleRegistration, name='Tradesperson-Registration'),
        path('emailNotice', views.email_notice, name='Email-notice'),
        path('congratulations', views.contratsPage, name='Congratulations'),

        path('learn-featues', views.features_learn, name='learn-featues'),
        path('learn-forC', views.clients_learn, name='learn-forC'),
        path('learn-forT', views.tradespeople_learn, name='learn-forT'),
        path('learn-aboutUs', views.aboutUs_learn, name='learn-aboutUs'),
        path('learn-contact', views.contactUS_learn, name='learn-contact'),
        path('Profile_page', views.Profile_page_view, name='profile-page'),
        path('Notifications', views.notifications_view, name='notifications'),
    
        path('Home_learn', views.home_learn_view, name='home-learn'),
        path('Signup_Learn', views.home_learn_login, name='Signup_Learn'),
        path('Create_As_C', views.create_as_c, name='Create_As_C'),
        path('Create_As_T', views.create_as_t, name='Create_As_T'),
        path('Verification_By_Email/', views.verify_email, name='Verification_By_Email'),
        path('Verification_By_Email_resend/', views.resend_email, name='Verification_By_Email_resend')

    ]
