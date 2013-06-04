
class FacebookBaseException(Exception):
    pass

class FacebookBaseAuthException(FacebookBaseException):
    pass

class FacebookAuthBadCodeException(FacebookBaseAuthException):
    pass