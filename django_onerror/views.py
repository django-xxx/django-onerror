import json

from django_response import response

from django_onerror.models import OnerrorReportInfo


def err_report(request):
    payload = json.loads(request.body)

    OnerrorReportInfo.objects.create(
        lineNo=payload.get('lineNo', -1),
        columnNo=payload.get('columnNo', -1),
        scriptURI=payload.get('scriptURI', ''),
        errorMessage=payload.get('errorMessage', ''),
        stack=payload.get('stack', ''),
    )

    return response()
