from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *


#First loading page
def home(request):
	return render(request, 'home.html')


#Signup html page
def signup(request):
	return render(request, 'signup.html')


#login html page
def loginpage(request):
	return render(request, 'login.html')


#first page after login
@login_required(login_url='loginpage')
def welcome(request):
    return render(request, 'welcome.html')


@login_required(login_url='loginpage')
def index(request):
    return render(request, 'index.html')


#profile page
@login_required(login_url='loginpage')
def profile(request):
    print(request.session['hello'])
    return render(request, 'profile.html')


#first password reset page
@login_required(login_url='loginpage')
def resetpassword(request):
	return render(request, 'resetpassword.html')


#User signup/registration function view
def usercreate(request):
	if request.method == 'POST':
		firstname = request.POST['first_name']
		lastname = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword:
			if User.objects.filter(username=username):
				messages.info(request, 'This username already exists. Sign up again')
			else:
				user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,username=username, password=password)
				user.save()
				return redirect('loginpage')
		else:
			messages.info(request, 'Password doesnt match. Signup Again')
			return redirect('signup')
	else:
		messages.info(request, 'Oops....Something went wrong.')
		return redirect('welcome')


#User signup/registration update view
def userupdate(request, id):
	if request.method == 'POST':
		user = request.user
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('profile')
	else:
		return redirect('welcome')


#User signup/registration password update view
def passupdate(request, id):
	if request.method == 'POST':
		user = request.user
		user.username = request.POST['username']
		password = request.POST.get('password')
		cpassword = request.POST.get('cpassword')
		try:
			if password is not None:
				if password == cpassword:
					user.set_password(password)
					user.save()
		except:
			pass
		return redirect('profile')
	else:
		return redirect('welcome')


#User login functionality view
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			request.session['hello'] = username
			messages.info(request, f'Welcome {username}.')
			return redirect('welcome')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')


#User logout functionality view
def logout(request):
	auth.logout(request)
	return redirect('home')


@login_required(login_url='loginpage')
def create(request):
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		age = request.POST['age']
		email = request.POST['email']
		phone = request.POST['phone']
		desname = request.POST['name']
		try:
			image = request.FILES['image']
		except:
			image = f'media/default.jpg'
		persons = person(firstname=fname, lastname=lname, age=age, email=email, image=image)
		persons.save()
  
		details = personalDetails(phone=phone, personid=persons)
		details.save()
  
		position = designation(name=desname, personid=persons)
		position.save()
		return redirect('show')
	else:
		return redirect('index')


@login_required(login_url='loginpage')
def show(request):
	persons = person.objects.all()
	return render(request, 'show.html', {'per': persons})


@login_required(login_url='loginpage')
def delete(request, personid):
	persons = person.objects.get(personid=personid)
	persons.delete()
	return redirect('show')


@login_required(login_url='loginpage')
def edit(request, personid):
	persons = person.objects.get(personid=personid)
	return render(request, 'edit.html', {'per': persons})


@login_required(login_url='loginpage')
def update(request, personid):
	if request.method == 'POST':
		persons = person.objects.get(personid=personid)
		persons.firstname = request.POST.get('firstname')
		persons.lastname = request.POST.get('lastname')
		persons.age = request.POST.get('age')
		persons.email = request.POST.get('email')
		try:
			persons.image = request.FILES['image']
		except:
			pass
		persons.save()
		return redirect('show')
	else:
		return redirect('show')



# def hello(request):
#     form = UserRegisterationForm()
#     return render(request, 'hello.html', {'form': form})