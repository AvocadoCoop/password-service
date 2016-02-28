import hashlib
import base64

from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def password_service(request, template="password_service/service.html"):
    identifier = request.GET.get('id')
    password = None

    if identifier is not None and identifier != '':
        password_hex = hashlib.sha256("{} {}".format(identifier, settings.PASSWORD_SERVICE_SECRET)).hexdigest()[:12]
        password = base64.b64encode(password_hex)

    return render(
        request,
        template,
        dict(
            identifier = identifier,
            password = password,
        ),
    )
