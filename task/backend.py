from django.contrib.auth.backends import ModelBackend
from .models import User
from django.contrib.auth import get_user_model



class EmailAuthBackend(object):
	
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			except User.DoesNotExist:
				return None
 
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
	except User.DoesNotExist:
		return None
