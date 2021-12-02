from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from webportal.management.sqlite.conSqlite3 import getFields, getModels, validateData
from .models import *
from .serializers import *
#from django.core.mail import send_mail
from .decorators import check_recaptcha

################################################################################
#                 D    A    T    A    L    E    A    K    S
################################################################################
@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
def models_(request):
	mds = getFields(getModels())
	return Response(mds, status=status.HTTP_200_OK)

@api_view(['GET'])
def people_(request):
	people = Person.objects.all()
	serializer = PersonSerializer(people, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK )
################################################################################
#                 P    R    I    V    A    C    Y    R    S
################################################################################
@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
def lgpdreqs(request):
    rqs = LGPDRequest.objects.all()
    serializer = LGPDRequestSerializer(rqs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def newLGPDReq(request):
	if request.method == 'POST':
		serializer = LGPDRequestSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
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
   #         send_mail(
   #            'Nova solicitação LGPD',
   #             'Acesse a platafoma para verificar',
   #             '#',
   #             ['#'],
   #             fail_silently=False,
   #         )
            pass
        except:
            pass
        serializer.save()
        return Response('{}', status=status.HTTP_200_OK)
    else:
        return Response('{}', status=status.HTTP_400_BAD_REQUEST)