from django.shortcuts import redirect

from social.pipeline.partial import partial

from .models import UserProfile


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if kwargs.get('ajax') or user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
        else:
            return redirect('require_email')


def get_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):
	img_url = None
	if backend.name == 'google-plus':
		img_url = response['image']['url']
	else:
		img_url = 'http://local.offsetnull.com/static/nulluser.jpg'

	profile = UserProfile.objects.get_or_create(user = user)[0]
	profile.photo = img_url
	profile.save()
