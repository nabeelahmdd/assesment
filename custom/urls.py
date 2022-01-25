from rest_framework.routers import DefaultRouter
from django.urls import path, include
from custom.views.user_views import (
    MyTokenObtainPairView, RegisterViewSet,
)
from custom.views.student_views import (
    QuestionListViewSet, QuestionCreateViewSet
)
from custom.views.mentor_views import (
    AnswerListViewSet, AnswerCreateViewSet
)



router = DefaultRouter()
router.register('accounts/register', RegisterViewSet,
                basename='register')

router.register('question/list', QuestionListViewSet,
                basename='question_list')
router.register('question/create', QuestionCreateViewSet,
                basename='question_create')

router.register('answer/list', AnswerListViewSet,
                basename='answer_list')
router.register('answer/create', AnswerCreateViewSet,
                basename='answer_create')

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]

