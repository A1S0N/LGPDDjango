from rest_framework import serializers
from .models import *

class PrivacyRuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = PrivacyRule
		fields = '__all__'

class LGPDRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = LGPDRequest
		fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'