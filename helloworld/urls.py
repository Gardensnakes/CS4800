from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

request = '<HttpRequest object>'
urlpatterns = [
    path('', views.index, name='index'),
    #path('?search=<str:game_name>', views.search_game, name='search_game'),
    path('pdf/', views.search_game, name ='search_pdf'),
    path('search/', views.search, name='search_game'),
    path('Grand+Theft+Auto+V', views.get_GTAV, name='next-page1'),
    path('The+Witcher+3:+Wild+Hunt', views.get_TW3, name='next-page2'),
    path('Divinity:+Original+Sin+2+-+Definitive+Edition', views.get_DivinityOS2, name='next-page3'),
    path('Red+Dead+Redemption+2', views.get_RedDeadRedemption, name='next-page4'),
    path('Hades', views.get_hades, name='next-page5'),
    path('Dragon+Age:+Origins', views.get_DragonAgeOrin, name='next-page6'),
    path('Disco+Elysium', views.get_DiscoElysium, name='next-page7'),
    path("Baldur's+Gate+3", views.get_BaldursGate3, name='next-page8'),
    path('BioShock+Infinite', views.get_BioshockInfinite, name='next-page9'),
    path('Dishonored', views.get_Dishonored, name='next-page10'),
    path("Sid+Meier's+Civilization+IV", views.get_CivIV, name='next-page11'),
    path('Undertale', views.get_Undertale, name='next-page12'),
    path("The+Sims+4", views.get_Sims4, name='next-page13'),
    path('Grand+Theft+Auto+V-pdf', views.gta_pdf, name='gta-pdf'),
    path('The+Witcher+3:+Wild+Hunt-pdf', views.tw3_pdf, name='tw3-pdf'),
    path('Divinity:+Original+Sin+2+-+Definitive+Edition-pdf', views.dv_pdf, name='dv-pdf'),
    path('Red+Dead+Redemption+2-pdf', views.rdr2_pdf, name='rdr2-pdf'),
    path('Hades-pdf', views.hades_pdf, name='hades-pdf'),
    path('Dragon+Age:+Origins-pdf', views.dao_pdf, name='dao-pdf'),
    path('Disco+Elysium-pdf', views.de_pdf, name='de-pdf'),
    path("Baldur's+Gate+3-pdf", views.bg3_pdf, name='bg3-pdf'),
    path('BioShock+Infinite-pdf', views.bioshi_pdf, name='bioshi-pdf'),
    path('Dishonored-pdf', views.dis_pdf, name='dis-pdf'),
    path("Sid+Meier's+Civilization+IV-pdf", views.sidmyciv4_pdf, name='sidmyciv4-pdf'),
    path('Undertale-pdf', views.undertale_pdf, name='Undertale-pdf'),
    path("The+Sims+4-pdf", views.sim4_pdf, name='sim4-pdf')
]


