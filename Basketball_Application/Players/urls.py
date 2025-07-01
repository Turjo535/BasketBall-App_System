
from django.urls import path
from .views import Player_Information_View,ReportView,Scouting_Context_Views,PlayerReportPDFView,ReportView,ReportPDFEmailSentView,Report_List_PDF_View

urlpatterns = [
    path('playerinfo/',Player_Information_View.as_view(), name="player_information"),
    path('report/',ReportView.as_view(),name="Report"),
    path('scouting-context/', Scouting_Context_Views.as_view(), name="Scouting-Context"),
    path('report/<int:id>/', ReportView.as_view(), name="Report"),
    path('report/<int:id>/pdf/',PlayerReportPDFView.as_view(),name="Pdf-Report"),
    path('report/<int:id>/pdf/email/',ReportPDFEmailSentView.as_view(),name="Pdf-Report"),
    path('report/lists/pdf/', Report_List_PDF_View.as_view(), name="Report_list"),


]