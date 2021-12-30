from core.security import create_access_token
data = {"email" : "test@email.com"}
create_access_token(data)