from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', Index.as_view(), name='home'),
	path('category', CategoryEvents.as_view(), name='CatEvents'),
	path('cats', cats, name='cats'),
	path('cityEvent', cityEvents, name='CityEvents'),

	path('register', RegisterUser.as_view(), name='Register'),
	path('login', LoginUser.as_view(), name='Login'),

	path('createPersonEvent', CreatePersonEvent.as_view(), name='CreatePersonEvent'),
	path('createTeamEvent', CreateTeamEvent.as_view(), name='CreateTeamEvent'),
	path('createTeam', TeamCreate.as_view(), name='CreateTeam'),

	path('personEventDetail/<int:pk>/', PersonEventDetail.as_view(), name='PersonEventDetail'),
	path('teamEventDetail/<int:pk>/', TeamEventDetail.as_view(), name='TeamEventDetail'),
	path('teamDetail/<int:pk>/', TeamDetail.as_view(), name='TeamDetail'),
	path('clubDetail/<int:pk>/', ClubDetail.as_view(), name='ClubDetail'),
	path('profile/<int:pk>/', ProfileDetail.as_view(), name='Profile'),

	path('addPersonEventUser', addPersonEventUser, name='addPersonEvetUser'),
	path('addTeamEventTeam', addTeamEventTeam, name='addTeamEventAjax'),
	path('savePersonEvent', savePersonEvent, name='savePersonEvent'),
	path('saveTeamEvent', saveTeamEvent, name='saveTeamEvent'),

	path('profileEdit', profileEdit, name='profileEdit'),

	path('personEvents', personEvents, name='personEvents'),
	path('teamEvents', teamEvents, name='teamEvents'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)