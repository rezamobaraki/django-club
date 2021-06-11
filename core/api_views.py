from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.models import Question, Answer
from core.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status

from permission_access.permissions import IsOwnerOrReadOnly


class QuestionListView(APIView):
    """
        Retrieve, Create, Update, Delete questions instances
    """

    def get(self, request, ):
        questions = Question.objects.all()
        serialize_data = QuestionSerializer(instance=questions, many=True).data
        return Response(serialize_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        serialize_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_200_OK)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = AnswerSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class AnswerUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def put(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        self.check_object_permissions(request, answer)
        serialize_data = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_200_OK)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        self.check_object_permissions(request, answer)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
