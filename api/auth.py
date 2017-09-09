from functools import wraps

from flask import g, request, jsonify
from jose import jwt, JWTError, ExpiredSignatureError

from .models import User


# define a user class
class CurrentUser(object):
    def __init__(self, user_id, name, email, roles, image_url):
        self.uuid = user_id
        self.roles = roles
        self.email = email
        self.name = name
        self.photo = image_url

    def __repr__(self):
        return ("<CurrentUser \n"
                "uuid - {} \n"
                "name - {} \n"
                "email - {} \n"
                "role - {} >").format(self.uuid, self.name,
                                      self.email, self.roles)


# authorization decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check that the Authorization header is set
        authorization_token = request.headers.get('Authorization')
        if not authorization_token:
            response = jsonify({
                "message": "Bad request. Header does not contain authorization"
                           " token"
            })
            response.status_code = 400
            return response

        unauthorized_response = jsonify({
            "message": "Unauthorized. The authorization token supplied is"
                       " invalid"
        })
        unauthorized_response.status_code = 401
        expired_response = jsonify({
            "message": "The authorization token supplied is expired"
        })
        expired_response.status_code = 401

        try:
            # decode token
            payload = jwt.decode(authorization_token, 'secret',
                                 options={"verify_signature": False})
        except ExpiredSignatureError:
            return expired_response
        except JWTError:
            return unauthorized_response

        expected_user_info_format = {
            "id": "user_id",
            "email": "gmail",
            "first_name": "test",
            "last_name": "user",
            "name": "test user",
            "picture": "link",
            "roles": {
                "Andelan": "unique_id",
                "Fellow": "unique_id"
            }
        }

        # confirm that payload and UserInfo has required keys
        if ("UserInfo" and "exp") not in payload.keys() and payload[
                "UserInfo"].keys() != expected_user_info_format.keys():
            return unauthorized_response
        else:
            uuid = payload["UserInfo"]["id"],
            name = payload["UserInfo"]["name"],
            email = payload["UserInfo"]["email"],
            photo = payload["UserInfo"]["picture"]
            roles = payload["UserInfo"]["roles"]

            # save user to db if they haven't been saved yet
            if not User.query.get(payload["UserInfo"]["id"]):
                user = User(
                    uuid=uuid, name=name, email=email, photo=photo
                )
                user.save()

            # instantiate current user object
            current_user = CurrentUser(
                uuid, name, email, roles, photo
            )

            # set current user in flask global variable, g
            g.current_user = current_user

            # now return wrapped function
            return f(*args, **kwargs)
    return decorated
