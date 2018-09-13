# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django_onerror.models import OnerrorReportInfo
from django_response import response


def err_report(request):
    if not hasattr(settings, 'DJANGO_ONERROR_ACCEPT_REPORT') or settings.DJANGO_ONERROR_ACCEPT_REPORT:
        payload = json.loads(request.body)

        OnerrorReportInfo.objects.create(
            lineNo=payload.get('lineNo', -1),
            columnNo=payload.get('columnNo', -1),
            scriptURI=payload.get('scriptURI', ''),
            errorMessage=payload.get('errorMessage', ''),
            stack=payload.get('stack', ''),
        )

    return response()
