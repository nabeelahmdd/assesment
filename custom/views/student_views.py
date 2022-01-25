from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import *
from custom.models import Question
from rest_framework.permissions import IsAuthenticated
from custom.serializers.student_serializer import QuestionSerializer


class QuestionListViewSet(
	ListModelMixin,
	GenericViewSet
):
	permission_classes = [IsAuthenticated]
	serializer_class = QuestionSerializer

	def get_queryset(self):
		return Question.objects.filter(student=self.request.user)


class QuestionCreateViewSet(
	CreateModelMixin,
	GenericViewSet
):
	permission_classes = [IsAuthenticated]
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	def perform_create(self, serializer):
		serializer.save(student=self.request.user)