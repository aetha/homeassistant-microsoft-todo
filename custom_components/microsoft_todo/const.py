DOMAIN = "microsoft_todo"

CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
AUTH_CALLBACK_PATH = "/api/microsoft-todo"
AUTHORIZATION_BASE_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
SCOPE = ["offline_access", "Tasks.ReadWrite"]

MS_TODO_AUTH_FILE = ".ms_todo_auth.json"
ATTR_ACCESS_TOKEN = "access_token"
ATTR_REFRESH_TOKEN = "refresh_token"

SERVICE_NEW_TASK = "ms_todo_new_task"

SUBJECT = "subject"