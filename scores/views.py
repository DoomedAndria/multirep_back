from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from scores.serializer import ScoreSerializer


class ManageScoreView(APIView):
    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)