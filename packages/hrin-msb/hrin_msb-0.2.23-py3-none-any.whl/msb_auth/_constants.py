AUTH_REQUEST_USER_FIELD = "user"
AUTH_REQUEST_PASSWORD_FIELD = "password"

MSB_JWT_TOKEN_VALIDATOR = "msb_auth.validators.JwtTokenValidator"
MSB_INTRA_SERVICE_REQUEST_VALIDATOR = "msb_auth.validators.IntraServiceRequestValidator"

class TokenConst:
	username_field = "username"
	userid_field = "id"
	user_email_field = "email"

	access_token_validity_config_name = 'JWT_ACCESS_TOKEN_VALIDITY'
	refresh_token_validity_config_name = 'JWT_REFRESH_TOKEN_VALIDITY'
	signing_key_config_name = 'JWT_TOKEN_SIGNING_KEY'
	verification_key_config_name = 'JWT_TOKEN_VERIFY_KEY'
	token_audiance_config_name = 'JWT_TOKEN_AUDIENCE'
	token_issuer_config_name = 'JWT_TOKEN_ISSUER'


class DefaultJwtConfig:
	username_field = "username"
	userid_claim = "id"
	userid_field = "userid"
	user_email_field = "email"
	user_class = "msb_auth.TokenUser"
	auth_rule = 'msb_auth.jwt_user_auth_rule'
	algorithm_hs256 = 'HS256'
	auth_header_types = ('Bearer',)
	auth_header_name = 'HTTP_AUTHORIZATION'
	token_type_claim = 'token_type'
	jti_claim = 'jti'
	access_token_lifetime = 30
	refresh_token_lifetime = 1440
	rotate_refresh_tokens = False
	blacklist_after_rotation = False
	audience = None
	issuer = None


class MsAuthConst:
	AUTH_VALIDATION_USER_VALUE = "token"
	AUTH_VALIDATION_AUTH_TYPE = "ms_sso"


class LdapAuthConst:
	AUTH_VALIDATION_AUTH_TYPE = "ldap"
