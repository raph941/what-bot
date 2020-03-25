from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    request.method ='POST'

    msg = request.POST.get('Body')

    resp = MessagingResponse()

    # Add a text message
    resp.message(msg)

    return HttpResponse(str(resp))
