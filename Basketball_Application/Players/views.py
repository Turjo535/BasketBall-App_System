from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Player
from UserAccount.models import User
from .models import Report_Model
from .pdf import generate_player_report
from UserAccount.utils import Util
from .serializers import Player_Information_Serializers,Report_Serializers, Scouting_Context_Serializers,ReportSerializerID
from UserAccount.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permission import Is_Player, Is_Coach,IsOwner
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile

from django.core.files import File
from datetime import datetime

# Create your views here.

class Player_Information_View(APIView):
    
    permission_classes=[Is_Player,IsOwner, IsAuthenticated]

    def post(self, request):
        
        serializer = Player_Information_Serializers(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Player information saved successfully.", status=201)
        else:
            return Response(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ReportView(APIView):
    permission_classes=[Is_Player,IsOwner, IsAuthenticated]
    # def get(self, request):
    #     # Render empty form
    #     return render(request, 'report_form.html')
    def post(self, request):
        serializer=Report_Serializers(data=request.data)
        #print(serializer)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Player Report saved successfully.", status=201)
            # return render(request, 'report_form.html', {
            #     'message': 'Player Report saved successfully!'
            # })
        else:
            return Response(serializer.errors, status=400 )
        
class Scouting_Context_Views(APIView):
    permission_classes=[Is_Player,IsOwner, IsAuthenticated]
    def post(self, request):
        serializer=Scouting_Context_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Player Scouting Report saved successfully.", status=201)
        else:
            return Response(serializer.errors,status=400)
        
class ReportView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        report=Report_Model.objects.get(id=id, user=request.user)
        serializer=ReportSerializerID(report)
        return Response(serializer.data)





class PlayerReportPDFView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            
            report = Report_Model.objects.get(id=id, user=request.user)
            #print("this is my report", report)
            
           
            
            pdf_buffer = generate_player_report(report)
            pdf_bytes = pdf_buffer.getvalue()  
            pdf_buffer.close()
            filename = f"player_report_{request.user.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
            if not report.pdf:
                report.pdf.save(filename, ContentFile(pdf_bytes))
            response = HttpResponse(pdf_bytes, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="player_report_{id}.pdf"'
            return response
        except Report_Model.DoesNotExist:
            raise NotFound("Report not found or you don't have permission to access it")
        
class ReportPDFEmailSentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        try:
            report=Report_Model.objects.get(user=request.user, id=id)
            Util.send_email({
                    'subject': "Player's Report",
                    'body': f"{report.user.name}'s PDF Report: {report.pdf}",
                    'to_email': report.user.email
                })
            return Response("Email sent successfully.",status=220)
        except Report_Model.unique_error_message:
            return Response(status=400)
        
class Report_List_PDF_View(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        reports = Report_Model.objects.filter(user=request.user)
        print("Reports",reports)
        # Filter reports with non-empty PDF fields
        valid_reports = reports.exclude(pdf__isnull=True).exclude(pdf='')
        print("Non Empty Reports",reports)
        # Get list of PDF file paths
        pdf_paths = valid_reports.values_list('pdf', flat=True)
        #pdf=Report_Model.objects.exclude('').exclude(pdf=None).values_list('pdf', flat=True)
        print("Valid PDF Reports",reports)
        return Response(pdf_paths)
        
        