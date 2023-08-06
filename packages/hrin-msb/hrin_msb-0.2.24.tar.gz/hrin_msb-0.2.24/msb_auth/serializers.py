from django.utils.translation import gettext_lazy as _
from rest_framework.fields import CharField
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenVerifySerializer)

from .constants import  (TokenFieldNames as _tfn, AUTH_REQUEST_TYPE_FIELD_NAME, AUTH_REQUEST_USER_FIELD_NAME)
from .users import TokenUser


class JwtTokenObtainSerializer(TokenObtainPairSerializer):
	"""Customizes JWT default Serializer to add more information about user"""
	username_field = AUTH_REQUEST_USER_FIELD_NAME
	default_error_messages = {
		'no_active_account': _('User Authentication Failed.')
	}

	def __init__(self, *args, **kwargs):
		super(JwtTokenObtainSerializer, self).__init__(*args, **kwargs)
		self.fields[AUTH_REQUEST_TYPE_FIELD_NAME] = CharField(required=True)
		self.fields[AUTH_REQUEST_USER_FIELD_NAME] = CharField(required=True)

	@classmethod
	def final_token_data(cls, token: TokenUser = None):
		return token

	@classmethod
	def get_token(cls, user: TokenUser = None):
		try:
			usertoken: TokenUser = super().get_token(user)
			usertoken[_tfn.ID] = user.token.get(_tfn.ID)
			usertoken[_tfn.AUTH_ID] = user.token.get(_tfn.AUTH_ID)
			usertoken[_tfn.USERNAME] = user.token.get(_tfn.USERNAME)
			usertoken[_tfn.IS_VALID] = user.token.get(_tfn.IS_VALID)
			usertoken[_tfn.SESSION] = user.token.get(_tfn.SESSION).to_json()
			usertoken[_tfn.IP] = user.token.get(_tfn.IP)
			return cls.final_token_data(usertoken)
		except Exception as e:
			return None


class JwtTokenVerifySerializer(TokenVerifySerializer):
	pass
