from rest_framework.views import APIView

from core.models import Question
from core.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status


class QuestionListView(APIView):
    """
        Retrieve, Create, Update, Delete questions instances
    """

    def get(self, request, ):
        questions = Question.objects.all()
        serialize_data = QuestionSerializer(instance=questions, many=True).data
        return Response(serialize_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        serialize_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_200_OK)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
