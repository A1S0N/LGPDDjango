from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from .serializers import *
from django.core.mail import send_mail
from .decorators import check_recaptcha
################################################################################
#                 P    R    I    V    A    C    Y    R    S
################################################################################
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def rules(request):
    rules_ = PrivacyRule.objects.all()
    serializer = PrivacyRuleSerializer(rules_, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def newRule(request):
	if request.method == 'POST' and request.token_is_valid:
		serializer = PrivacyRuleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def editRule(request):
	if request.method == 'POST' and request.token_is_valid:
		try:
			PrivacyRule.objects.get(id=request.data['id']).update(title=request.data['title'], severity=request.data['severity'])
			return Response(status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def deleteRule(request):
	if request.method == 'POST' and request.token_is_valid:
		try:
			PrivacyRule.objects.get(id=request.data['id']).delete()
			return Response(status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)
################################################################################
################################################################################
#                 P    R    I    V    R    Q    S    T    S
################################################################################
@check_recaptcha
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def contact(request):
    serializer = LGPDRequestSerializer(data=request.data)
    if serializer.is_valid():
        try:
            send_mail(
                'Nova solicitação LGPD',
                'Acesse a platafoma para verificar',
                '#',
                ['#'],
                fail_silently=False,
            )
        except:
            pass
        serializer.save()
        return Response('{}', status=status.HTTP_200_OK)
    else:
        return Response('{}', status=status.HTTP_400_BAD_REQUEST)