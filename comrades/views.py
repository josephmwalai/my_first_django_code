from rest_framework.response import Response
from rest_framework.views import APIView

from comrades.models import Comrades
from comrades.serializers import ComradesSerializer


# Create your views here.
class ComradesListView(APIView):
    def get(self, request, *args, **kwargs):
        comrades = Comrades.objects.all()
        serializer = ComradesSerializer(comrades, many=True)
        return Response(serializer.data)


class ComradesDetailView(APIView):
    def get(self, request, email, *args, **kwargs):
        comrades = Comrades.objects.filter(email=email).first()
        if comrades:
            serializer = ComradesSerializer(comrades)
            return Response(serializer.data)
        return Response({
            'message': 'Comrade not found'
        }, status=404)


class ComradesCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ComradesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
