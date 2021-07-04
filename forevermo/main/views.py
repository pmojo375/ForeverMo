from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import *
from django.core.exceptions import ObjectDoesNotExist
from main.models import *

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

				plusone = form.cleaned_data['plusone']
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				food = form.cleaned_data['foodselection']

				if plusone:
					p1firstname = form.cleaned_data['firstnameplusone']
					p1lastname = form.cleaned_data['lastnameplusone']
					p1food = form.cleaned_data['foodselectionplusone']

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

						p1 = PlusOne(firstname=p1firstname, lastname=p1lastname, foodchoice=p1food, host=guest)

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
						guest = Guest(firstname=firstname, lastname=lastname, foodchoice=food)
						guest.save()

						# create plus one object and save
						# no plus one could previously be tied to this guest since it is a new object
						p1 = PlusOne(firstname=p1firstname, lastname=p1lastname, foodchoice=p1food, host=guest)
						p1.save()
					else:
						# create guest object and save
						guest = Guest(firstname=firstname, lastname=lastname, foodchoice=food)
						guest.save()

				print('Worked')
				# process the data in form.cleaned_data as required
				return HttpResponseRedirect(request.path_info)

			form = GuestForm()

		elif 'message' in request.POST:
			form = MessageForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				message = form.cleaned_data['message']

				newMessage = Message(name=name, message=message)
				newMessage.save()

				# process the data in form.cleaned_data as required
				return HttpResponseRedirect(request.path_info)
		elif 'title' in request.POST:
			form = SongForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				artist = form.cleaned_data['artist']
				title = form.cleaned_data['title']

				newSong = Song(name=name, artist=artist, title=title)
				newSong.save()

				# process the data in form.cleaned_data as required
				return HttpResponseRedirect(request.path_info)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = GuestForm()
		messageForm = MessageForm()
		songForm = SongForm()

	print('NoWorked')
	return render(request, 'main.html', {'form': form, 'messageForm':messageForm, 'messages': messages, 'songForm': songForm})
