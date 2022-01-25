from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import *
from custom.models import Question
from rest_framework.permissions import IsAuthenticated
from custom.serializers.student_serializer import QuestionSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class QuestionListViewSet(
	ListModelMixin,
	GenericViewSet
):
	authentication_classes = [BasicAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = QuestionSerializer

	def get_queryset(self):
		return Question.objects.filter(student=self.request.user)


class QuestionCreateViewSet(
	CreateModelMixin,
	GenericViewSet
):
	authentication_classes = [BasicAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	def perform_create(self, serializer):
		serializer.save(student=self.request.user)