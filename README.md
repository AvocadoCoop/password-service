# Password Service

Some passwords and personal and highly secure, this password not for
those ones.

If you need to share low security passwords for account with a supplier
with multiple buyers, use can this simple service.

Identifiers for the account (which should be stored separately) are
hashed with an secret and then base64 encoded to generate the password
which would be used with the service in question.

It is some what brittle since changing the secret changes every password
making it hard to transition over time, and if you slightly mistype the
identifier you will get entirely wrong password, but there is no state
required except the secret.

## Setup

Django 1.7 or higher, should work with Python 2.7 or 3.4 or higher.

Install from github for now

```
pip install git@github.com:AvocadoCoop/password-service.git
```

Configure your urls:

```
# urls.py

urlpatterns = [
  # ...
  url('^admin/password_service/', include('templated_mail.urls')),
]
```

A minimal template is provided, but you may want your own version under
`password_service/service.html`.

Finally you need the secret to hash with your account identifers. You
can change this secret to change all of the passwords, but you will have
to manually update all the services using their password reset
mechanism.

```
PASSWORD_SERVICE_SECRET = 'somesceretwhichishardtoguess'
```

That's it, you're done. You can start setting passwords and updating
your teams documentation.
