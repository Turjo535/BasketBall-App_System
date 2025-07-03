from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Player
from UserAccount.models import User
from .models import Report_Model
from .pdf import generate_player_report
from UserAccount.utils import Util
from .serializers import Player_Information_Serializers,Player_list_serializer,Report_Serializers, Scouting_Context_Serializers,ReportSerializerID
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
from django.shortcuts import get_object_or_404

from django.core.files import File
from datetime import datetime
from django.utils import timezone

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
        
class Player_list_view(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        players=User.objects.filter(role='player')
        serializer=Player_list_serializer(players,many=True)
        return Response(serializer.data)

#@method_decorator(csrf_exempt, name='dispatch')
class ReportView(APIView):
    permission_classes=[Is_Player,IsOwner, IsAuthenticated]
    # def get(self, request):
    #     # Render empty form
    #     return render(request, 'report_form.html')
    def post(self, request):
        
        serializer=Report_Serializers(data=request.data)
   
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Player Report saved successfully.", status=201)
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

class ReportDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        report=Report_Model.objects.get(id=id, user=request.user)
        serializer=ReportSerializerID(report)
        return Response(serializer.data)





class PlayerReportPDFView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # fetch and 404 if not found / not owned
        report = get_object_or_404(Report_Model, id=id, user=request.user)

        # generate PDF
        pdf_buffer = generate_player_report(report)
        pdf_bytes = pdf_buffer.getvalue()
        pdf_buffer.close()

        # save to model if not yet saved, or overwrite
        filename = f"player_report_{request.user.id}_{timezone.now().strftime('%Y%m%d%H%M%S')}.pdf"
        content = ContentFile(pdf_bytes, name=filename)
        report.pdf.save(filename, content, save=True)

        # stream as download
        resp = HttpResponse(pdf_bytes, content_type='application/pdf')
        resp['Content-Disposition'] = f'attachment; filename="player_report_{report.id}.pdf"'
        return resp
        
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
        
        