
from rest_framework.response import Response
from rest_framework import status
from base.models import Patient
from patient_info_API.serializers import PatientSerializer
from django.shortcuts import render
from rest_framework.views import APIView

class PatientListAPIView(APIView):
#    def get(self, request):
#        patients = Patient.objects.all()
#        serializer = PatientSerializer(patients, many=True)
#        return Response(serializer.data)

    def get(self, request):
        patients = Patient.objects.all()
        context = {'patient_list': patients}
        return render(request, 'base/patient_list.html', context)
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)