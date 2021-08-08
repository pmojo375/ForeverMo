from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import *
from django.core.exceptions import ObjectDoesNotExist
from main.models import *
from django.conf import settings
import requests

secret_key = settings.RECAPTCHA_PRIVATE_KEY
site_key = settings.RECAPTCHA_PUBLIC_KEY

# Create your views here.

def main(request):
	# if this is a POST request we need to process the form data
	messages = Message.objects.all()

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		print(request.POST)
		if 'firstname' in request.POST:
			form = GuestForm(request.POST)

			if form.is_valid():

				# captcha verification
				data = {
					'response': request.POST.get('g-recaptcha-response'),
					'secret': secret_key
				}
				resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
				result_json = resp.json()

				print(result_json)

				if result_json.get('success') and result_json.get('score') >= 0.9:

					plusone = form.cleaned_data['plusone']
					firstname = form.cleaned_data['firstname']
					lastname = form.cleaned_data['lastname']

					if plusone:
						p1firstname = form.cleaned_data['firstnameplusone']
						p1lastname = form.cleaned_data['lastnameplusone']

					try:

						# check if the guest is already is in the database
						guest = Guest.objects.get(firstname=firstname, lastname=lastname)
						
						if plusone:

							# guest bringing plus one

							# update guest fields
							# create plus one and tie it to the guest

							# this overwrites any previous plus one based on my tests

							# update and save guest data
							guest.foodchoice = food

							guest.save()

							p1 = PlusOne(firstname=p1firstname, lastname=p1lastname, host=guest)

							p1.save()

						else:

							# guest is not bringing plus one

							# update and save guest data
							guest.foodchoice = food
							guest.save()

							if hasattr(guest, 'plusone'):

								# guest previously had plus one

								# get guests previous plus one
								p1 = PlusOne.objects.get(host=guest)

								# delete plus one entry
								p1.delete()

					except ObjectDoesNotExist:

						# guest not in database yet

						if plusone:

							# create guest object and save
							guest = Guest(firstname=firstname, lastname=lastname)
							guest.save()

							# create plus one object and save
							# no plus one could previously be tied to this guest since it is a new object
							p1 = PlusOne(firstname=p1firstname, lastname=p1lastname, host=guest)
							p1.save()
						else:
							# create guest object and save
							guest = Guest(firstname=firstname, lastname=lastname)
							guest.save()

					# process the data in form.cleaned_data as required
					return HttpResponseRedirect(request.path_info)

			messageForm = MessageForm()
			songForm = SongForm()
		elif 'message' in request.POST:
			messageForm = MessageForm(request.POST)
			if messageForm.is_valid():

				# captcha verification
				data = {
					'response': request.POST.get('g-recaptcha-response'),
					'secret': secret_key
				}
				resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
				result_json = resp.json()

				print(result_json)

				if result_json.get('success') and result_json.get('score') >= 0.9:
					name = messageForm.cleaned_data['name']
					message = messageForm.cleaned_data['message']

					newMessage = Message(name=name, message=message)
					newMessage.save()

				# process the data in form.cleaned_data as required
				return HttpResponseRedirect(request.path_info)

			form = GuestForm()
			songForm = SongForm()
		elif 'title' in request.POST:
			songForm = SongForm(request.POST)
			if songForm.is_valid():

				# captcha verification
				data = {
					'response': request.POST.get('g-recaptcha-response'),
					'secret': secret_key
				}
				resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
				result_json = resp.json()

				print(result_json)

				if result_json.get('success') and result_json.get('score') >= 0.9:
					name = songForm.cleaned_data['name']
					artist = songForm.cleaned_data['artist']
					title = songForm.cleaned_data['title']

					newSong = Song(name=name, artist=artist, title=title)
					newSong.save()

				# process the data in form.cleaned_data as required
				return HttpResponseRedirect(request.path_info)

			form = GuestForm()
			messageForm = MessageForm()

	# if a GET (or any other method) we'll create a blank form
	else:
		form = GuestForm()
		messageForm = MessageForm()
		songForm = SongForm()

	return render(request, 'main.html', {'site_key': site_key, 'form': form, 'messageForm':messageForm, 'messages': messages, 'songForm': songForm})
