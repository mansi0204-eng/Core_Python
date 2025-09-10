class LoginException(Exception):

    def __init__(self,msg):
        super().__init__(msg)

loginId="admin"
password=123

try:
    if loginId=="admin" and password=="admin":
        print("valid user")
    else:
        raise LoginException("Invalid User")
except LoginException as e:
    print("exception:",e)