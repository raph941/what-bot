from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    if request.method == 'POST':

        msg = request.POST['Body']

        resp = MessagingResponse()

        # Add a text message
        resp.message(msg)

        return HttpResponse(str(resp))
    else:
        pass