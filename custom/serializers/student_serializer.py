from rest_framework import serializers
from custom.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'title', 'text', 'attachment', 'answer',
            'cr_date', 'up_date'
        ]
