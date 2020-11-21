from django.shortcuts import render
from django.http import HttpResponse
from Select import *
from indit_db import *
from extract_db.py import *

sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
conn = create_connection(sql_path)

def index(request):
    return HttpResponse("Hello, world.")

def seller(request, name):
	return HttpResponse(get_game_seller(conn, name))




# def getname(request):
# 	return 
