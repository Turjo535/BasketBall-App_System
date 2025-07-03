
from django.urls import path
from .views import Player_Information_View,Player_list_view,ReportView,Scouting_Context_Views,PlayerReportPDFView,ReportView,ReportPDFEmailSentView,Report_List_PDF_View,ReportDetailView

urlpatterns = [
    path('playerinfo/',Player_Information_View.as_view(), name="player_information"),
    path('player-list/',Player_list_view.as_view(),name="Player_Lists"),
    path('report/',ReportView.as_view(),name="Report_create"),
    path('scouting-context/', Scouting_Context_Views.as_view(), name="Scouting-Context"),
    path('report/<int:id>/', ReportDetailView.as_view(), name="Report"),
    path('report/<int:id>/pdf/',PlayerReportPDFView.as_view(),name="Pdf-Report"),
    path('report/<int:id>/pdf/email/',ReportPDFEmailSentView.as_view(),name="Pdf-Report"),
    path('report/lists/pdf/', Report_List_PDF_View.as_view(), name="Report_list"),


]