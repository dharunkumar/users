from users.models import Users
from users.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

import traceback
import logging
# Logging
logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_users(request):
    if request.method == "GET":
        response_message = {}
        response_message['ok'] = False
        response_message['members'] = []
        try:
            data = Users.objects.all()
            serializer = UserSerializer(data=data, many=True)
            if(serializer.is_valid()):
                response_message['reason'] = 'Unable to get Users Data'
            else:
                response_message['ok'] = True
                response_message['members'] = serializer.data
        except Exception as e:
            logger.error('Exception at get_users :{}'.format(str(e)))
            logger.error(traceback.format_exc())
            response_message['reason'] = 'Exception while getting Users Data'
        return Response(response_message)
