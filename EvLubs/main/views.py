from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from queryset_sequence import QuerySetSequence


class Index(ListView):
	model = PersonEvent
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['TeamEvents'] = TeamEvent.objects.filter(city = self.request.user.profile.city)
		context['profile'] = self.request.user.profile
		context['Categorys'] = Category.objects.all()
		context['PersonEvents'] = PersonEvent.objects.filter(city=self.request.user.profile.city)
		personEvents = PersonEvent.objects.filter(city=self.request.user.profile.city)
		teamEvents = TeamEvent.objects.filter(city=self.request.user.profile.city)
		context['Events'] = QuerySetSequence(personEvents, teamEvents)
		context['cats'] = Category.objects.all()
		return context

	# def post(self, request, **kwargs):
	# 	city = request.POST.get('city')
	# 	context = self.get_context_data(**kwargs)
	# 	context['PersonEvents'] = PersonEvent.objects.filter(city=city)



class CategoryEvents(ListView):
	model = PersonEvent
	context_object_name = 'PersonEvent'
	template_name = 'main/CategoryEvents.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = self.request.POST.get('elastics')
		category = Category.objects.get(title=category)
		personEvents = PersonEvent.objects.filter(cat=category)
		teamEvents = TeamEvent.objects.filter(cat=category)
		context['Events'] = QuerySetSequence(personEvents, teamEvents)
		return context

def cats(request):
	if request.method == "POST":
		category = Category.objects.get(title=request.POST.get('elastics'))
		personEvents = PersonEvent.objects.filter(cat=category)
		teamEvents = TeamEvent.objects.filter(cat=category)
		context = {
			'profile': request.user.profile
		}
		context['Events'] = QuerySetSequence(personEvents, teamEvents)
		return render(request, 'main/CategoryEvents.html', context)
	return render(request, 'main/index.html')



def cityEvents(request):
	city = request.POST.get('city')
	city = city[:-1]

	context = {
		'PersonEvents': PersonEvent.objects.filter(city=city),
		'TeamEvents': TeamEvent.objects.filter(city=city),
		'city': city,
		'profile': request.user.profile,
	}

	return render (request, 'main/CityEvents.html', context)

# 												Register/Login/LogOut


class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = 'main/register.html'

	def form_valid(self, form):
		user = form.save()
		profile = Profile(user=user)
		profile.save()
		login(self.request, user)
		return redirect('home')


class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'main/login.html'

	def get_success_url(self):
		return reverse_lazy('home')


def logoutuser(request):
	logout(request)
	return redirect('login')


# 												PersonEvent


class CreatePersonEvent(CreateView):
	form_class = PersonEventForm
	template_name = 'main/CreatePersonEvent.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['cats'] = Category.objects.all()
		return context

	def get_initial(self, **kwargs):
		initial = super(CreatePersonEvent, self).get_initial(**kwargs)
		a = 'sport'
		initial.update({
			'creater': self.request.user.profile,
			'cat': Category.objects.get(title=a)
		})
		return initial


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.creater_id = self.request.user.profile.id
		self.object.save
		return super(CreatePersonEvent, self).form_valid(form)


	def get_success_url(self):
		return reverse_lazy('home')


class PersonEventDetail(DetailView):
	model = PersonEvent
	template_name = 'main/PersonEventDetail.html'
	context_object_name = 'Event'


def personEvents(request):
	events = PersonEvent.objects.filter(city=request.user.profile.city)
	context = {
		'events': events,
		'profile': request.user.profile
	}
	return render(request, 'main/events.html', context)


def savePersonEvent(request):
	if request.method == "POST":
		title = request.POST.get('title')
		description = request.POST.get('description')
		date = request.POST.get('date')
		city = request.POST.get('city')
		address = request.POST.get('address')
		cat = Category.objects.get(title=request.POST.get('elastics'))

		PersonEvent(title=title, description=description, date=date, city=city, address=address, cat=cat, creater=request.user.profile).save()
		return redirect('home')

# 												TeamEvent


class CreateTeamEvent(CreateView):
	form_class = TeamEventForm
	template_name = 'main/CreateTeamEvent.html'

	def get_initial(self):
		initial = super(CreateTeamEvent, self).get_initial()
		team = Team.objects.get(admin=self.request.user.profile)
		initial.update({
			'creater': team.pk
		})
		return initial



def saveTeamEvent(request):
	if request.method == "POST":
		title = request.POST.get('title')
		description = request.POST.get('description')
		date = request.POST.get('date')
		city = request.POST.get('city')
		address = request.POST.get('address')
		cat = Category.objects.get(title=request.POST.get('elastics'))
		creater = Team.objects.get(admin=request.user.profile)

		TeamEvent(title=title, description=description, date=date, city=city, address=address, cat=cat, creater=creater).save()
		return redirect('home')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.creater_id = Team.objects.get(admin=self.request.user.profile).id
		self.object.save
		return super(CreateTeamEvent, self).form_valid(form)


	def get_success_url(self):
		return reverse_lazy('home')


class TeamEventDetail(DetailView):
	model = TeamEvent
	template_name = 'main/TeamEventDetail.html'
	context_object_name = 'Event'


def teamEvents(request):
	events = TeamEvent.objects.filter(city=request.user.profile.city)
	context = {
		'events': events,
		'profile': request.user.profile
	}
	return render(request, 'main/events.html', context)

# 												Team 


class TeamCreate(CreateView):
	model = Team
	form_class = TeamForm
	template_name = 'main/CreateTeam.html'
	context_object_name = Team

	def get_initial(self):
		initial = super(TeamCreate, self).get_initial()
		initial.update({
			'admin': self.request.user.profile
		})
		return initial


	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.admin_id = self.request.user.profile.id
		self.object.save
		return super(TeamCreate, self).form_valid(form)


	def get_success_url(self):
		return reverse_lazy('home')

class TeamDetail(DetailView):
	model = Team
	context_object_name = 'Team'
	template_name = 'main/TeamDetail.html'


#												 Club


class ClubDetail(DetailView):
	model = Club
	context_object_name = 'Club'
	template_name = 'main/ClubDetail.html'


#									 	Add users/teams in Event


def addPersonEventUser(request):
	pk = request.POST.get('pk')
	event = PersonEvent.objects.get(pk=pk)
	event.users.add(request.user.profile)

def addTeamEventTeam(request):
	pk = request.POST.get('pk')
	event = TeamEvent.objects.get(pk=pk)
	team = Team.objects.get(admin=request.user.profile)
	event.teams.add(team)


class ProfileDetail(DetailView):
	model = Profile
	context_object_name = 'profile'
	template_name = 'main/Profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		return context


def profileEdit(request):
	form = profileEditForm()

	context = {
		'profile': request.user.profile,
		'form': form
	}

	if request.method == "POST":
		form = profileEditForm(request.POST)

		if form.is_valid():
			user = request.user
			user.username = request.POST.get('username')
			user.profile.status = request.POST.get('status')
			user.profile.city = request.POST.get('city')[:-1]
			user.profile.save()
			user.save()
			return redirect('home')

	return render(request, 'main/ProfileEdit.html', context)



