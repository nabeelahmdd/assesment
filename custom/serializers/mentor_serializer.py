from rest_framework import serializers
from custom.models import Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['question', 'student', 'ans', 'cr_date', 'up_date']