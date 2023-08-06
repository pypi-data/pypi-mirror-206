"""
CORE CONSTANTS

"""
from pathlib import Path


class EnvConst:
	ENV_LOAD_STATUS_KEY = 'ENV_CONFIG_LOADED'
	DOT_ENV_FILE = ".env"
	LOCAL_CONFIG_FILE_PREFIX = "local"
	ENVIRONMENT_VARIABLE_NAME = "ENVIRONMENT"
	DEBUG_VARIABLE_NAME = "DEBUG"


class EnvDefaults:
	# allow admin module
	ALLOW_ADMIN_URL = False

	# Secure csrf cookie
	CSRF_COOKIE_SECURE = True

	# Secure session cookie
	SESSION_COOKIE_SECURE = True

	# make csrf cokkied http only
	CSRF_COOKIE_HTTPONLY = True

	# make csrf cokkie http only
	SESSION_COOKIE_HTTPONLY = True

	# secure the ssl redirect
	SECURE_SSL_REDIRECT = True

	CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "POST", "PUT", ]

	CORS_ALLOW_HEADERS = [
		"accept", "accept-encoding", "authorization", "content-type",
		"dnt", "origin", "user-agent", "x-csrftoken",
		"x-requested-with",
	]

	CORS_PREFLIGHT_MAX_AGE = 86400

	CORS_ALLOW_CREDENTIALS = True


class NameConst:
	"""
	ENV CONSTANT NAMES
	"""
	ENV_LOAD_STATUS_KEY_NAME = 'ENV_CONFIG_LOADED'
	DOT_ENV_FILE_NAME = ".env"
	LOCAL_CONFIG_FILE_PREFIX = "local"
	ENVIRONMENT_VARIABLE_NAME = "ENVIRONMENT"
	DEBUG_VARIABLE_NAME = "DEBUG"

	"""
	CONSTANT DIRECTORY NAMES
	"""
	APP_DIR_NAME = "app"
	RESOURCES_DIR_NAME = "resources"
	WRITABLE_DIR_NAME = "writable"
	FIXTURES_DIR_NAME = "fixtures"

	DEFAULT_FIXTURE_DIR_NAME = "base"
	PROD_FIXTURE_DIR_NAME = "prod"
	TEST_FIXTURE_DIR_NAME = "test"

	RESOURCE_CONFIG_DIR_NAME = "config"
	SETUP_SCRIPTS_DIR_NAME = "setup"
	TEST_DATA_DIR_NAME = "test_data"
	LOGS_DIR_NAME = "fixtures"
	MIGRATIONS_DIR_NAME = "migrations"
	"""
	CONSTANT ENVIRONMENT NAMES
	"""
	PROD_ENV_NAME = "prod"
	STAGE_ENV_NAME = "stage"
	TEST_ENV_NAME = "test"
	DEV_ENV_NAME = "dev"
	LOCAL_ENV_NAME = "local"

	ENV_NAME_LIST = [LOCAL_ENV_NAME, DEV_ENV_NAME, TEST_ENV_NAME, STAGE_ENV_NAME, PROD_ENV_NAME]
	DEV_OR_TEST_ENV_NAMES_LIST = [LOCAL_ENV_NAME, DEV_ENV_NAME, TEST_ENV_NAME]
	"""
	CONSTANT FILE NAMES
	"""
	PROD_ENV_FILE_NAME = ".env"
	DEV_ENV_FILE_NAME = ".env.local"

	"""
	CONSTANT DATABASE NAMES
	"""
	DEFAULT_DATABASE_NAME = "default"
	LOGS_DATABASE_NAME = "logs"

	YAML_FILE_EXTENTION_NAME = "yaml"


class PathConst:
	# path list under root directory
	BASE_DIR_PATH = Path(Path.cwd().__str__().split(NameConst.RESOURCES_DIR_NAME)[0])
	APP_DIR_PATH = BASE_DIR_PATH.joinpath(NameConst.APP_DIR_NAME)
	WRITABLE_DIR_PATH = BASE_DIR_PATH.joinpath(NameConst.WRITABLE_DIR_NAME)
	RESOURCE_DIR_PATH = BASE_DIR_PATH.joinpath(NameConst.RESOURCES_DIR_NAME)

	PROD_ENV_FILE_PATH = BASE_DIR_PATH.joinpath(NameConst.PROD_ENV_FILE_NAME)
	DEV_ENV_FILE_PATH = BASE_DIR_PATH.joinpath(NameConst.DEV_ENV_FILE_NAME)

	# path list under writable directory
	LOGS_DIR_PATH = WRITABLE_DIR_PATH.joinpath(NameConst.LOGS_DIR_NAME)

	# path list under resources directory
	FIXTURES_DIR_PATH = RESOURCE_DIR_PATH.joinpath(NameConst.FIXTURES_DIR_NAME)
	RESOURCE_CONFIG_DIR_PATH = RESOURCE_DIR_PATH.joinpath(NameConst.RESOURCE_CONFIG_DIR_NAME)
	SETUP_SCRIPTS_DIR_PATH = RESOURCE_DIR_PATH.joinpath(NameConst.SETUP_SCRIPTS_DIR_NAME)
	TEST_DATA_DIR_PATH = RESOURCE_DIR_PATH.joinpath(NameConst.TEST_DATA_DIR_NAME)

	# path list under fixtures directory
	BASE_FIXTURES_DIR_PATH = FIXTURES_DIR_PATH.joinpath(NameConst.DEFAULT_FIXTURE_DIR_NAME),
	PROD_FIXTURES_DIR_PATH = FIXTURES_DIR_PATH.joinpath(NameConst.PROD_FIXTURE_DIR_NAME),
	TEST_FIXTURES_DIR_PATH = FIXTURES_DIR_PATH.joinpath(NameConst.TEST_FIXTURE_DIR_NAME),

	# compiled constants
	SYS_PATH_LIST = [
		BASE_DIR_PATH.__str__(), APP_DIR_PATH.__str__(),
		RESOURCE_DIR_PATH.__str__(), WRITABLE_DIR_PATH.__str__()
	]

	FIXTURE_DIRS_LIST = [BASE_FIXTURES_DIR_PATH, PROD_FIXTURES_DIR_PATH, TEST_FIXTURES_DIR_PATH]


__all__ = [
	"NameConst", "PathConst", "EnvDefaults"
]
