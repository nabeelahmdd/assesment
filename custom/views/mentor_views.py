
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import *
from custom.models import Answer
from rest_framework.permissions import IsAdminUser
from custom.serializers.mentor_serializer import AnswerSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class AnswerListViewSet(
	ListModelMixin,
	GenericViewSet
):
	authentication_classes = [BasicAuthentication, SessionAuthentication]
	permission_classes = [IsSuperUser]
	serializer_class = AnswerSerializer

	def get_queryset(self):
		return Answer.objects.filter(mentor=self.request.user)


class AnswerCreateViewSet(
	CreateModelMixin,
	GenericViewSet
):
	authentication_classes = [BasicAuthentication, SessionAuthentication]
	permission_classes = [IsSuperUser]
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

	def perform_create(self, serializer):
		serializer.save(mentor=self.request.user)