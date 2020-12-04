from django.shortcuts import render
from django.http import HttpResponse
# from .Select import *
from .init_db import *
from .extract_db import *
from .report import create_report
from  .descriptions import *
import os


sql_path = r"C:\\Users\\Administrator\\Desktop\\testsite\\helloworld\\Games.db"
conn = sqlite3.connect(sql_path, check_same_thread=False)

pic_name = ""

def index(request):
    return render(request, 'index.html')

def img_path(pic_name):
    img = pic_name.replace(":","")
    # img = pic_name.replace("II","2")
    # img = pic_name.replace("III","3")
    #return "{% static 'img/" + img + ".png' %}"
    #return "img/" + img + ".png"
    return 'img/' + img + '.png'
           #{% static 'img/GameSeachIcon.png' %}

def search_game(request):
    game_name = request.GET['search']
    release = get_game_release(conn, game_name)
    lowest_seller = get_lowest_seller(conn,game_name)
    lowest_price = get_lowest_price(conn,game_name)
    dev = get_game_developer(conn,game_name)
    pub = get_game_publisher(conn,game_name)
    launcher =  get_game_launcher(conn,game_name)
    platform = get_game_platform(conn,game_name)
    return create_report(game_name, game_name, pub, release, platform, lowest_seller, lowest_price)

def search(request):
    game_name = request.GET['search']
    img = img_path(game_name)
    release = get_game_release(conn, game_name)
    lowest_seller = get_lowest_seller(conn,game_name)
    lowest_price = get_lowest_price(conn,game_name)
    dev = get_game_developer(conn,game_name)
    pub = get_game_publisher(conn,game_name)
    launcher =  get_game_launcher(conn,game_name)
    platform = get_game_platform(conn,game_name)
    seller = get_game_1seller(conn,game_name)
    original = get_game_original_price(conn, game_name, seller)
    current = get_game_current_price(conn, game_name, seller)
    lowest = get_game_lowest(conn, game_name, seller)
    seller2 = get_game_2seller(conn,game_name)
    original2 = get_game_original_price(conn, game_name, seller2)
    current2 = get_game_current_price(conn, game_name, seller2)
    lowest2 = get_game_lowest(conn, game_name, seller2)
    seller3 = get_game_3seller(conn,game_name)
    original3 = get_game_original_price(conn, game_name, seller3)
    current3 = get_game_current_price(conn, game_name, seller3)
    lowest3 = get_game_lowest(conn, game_name, seller3)
    seller4 = get_game_4seller(conn,game_name)
    original4 = get_game_original_price(conn, game_name, seller4)
    current4 = get_game_current_price(conn, game_name, seller4)
    lowest4 = get_game_lowest(conn, game_name, seller4)
    seller5 = get_game_5seller(conn,game_name)
    original5 = get_game_original_price(conn, game_name, seller5)
    current5 = get_game_current_price(conn, game_name, seller5)
    lowest5 = get_game_lowest(conn, game_name, seller5)
    description = get_desc(conn, game_name)
    info = {"DESC": description,'Name':game_name,'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    
    return render(request, 'More.html', info)

# def search(request):
#     # if request.POST["search"] in util.list_entries():
#     #     return HttpResponseRedirect(reverse("search_game", args=(request.POST["search"],)))
#     # else:
#     #     return render(request, "index.html")
#     srh = request.GET['search']

def gta_pdf(request):
    release = get_game_release(conn, 'Grand Theft Auto V')
    lowest_seller = get_lowest_seller(conn,'Grand Theft Auto V')
    lowest_price = get_lowest_price(conn,'Grand Theft Auto V')
    dev = get_game_developer(conn,'Grand Theft Auto V')
    pub = get_game_publisher(conn,'Grand Theft Auto V')
    launcher =  get_game_launcher(conn,'Grand Theft Auto V')
    platform = get_game_platform(conn,'Grand Theft Auto V')
    return create_report("Grand Theft Auto V", "Grand Theft Auto V", pub, release, platform, lowest_seller, lowest_price)

def tw3_pdf(request):
    
    release = get_game_release(conn, 'The Witcher 3: Wild Hunt')
    lowest_seller = get_lowest_seller(conn,'The Witcher 3: Wild Hunt')
    lowest_price = get_lowest_price(conn,'The Witcher 3: Wild Hunt')
    dev = get_game_developer(conn,'The Witcher 3: Wild Hunt')
    pub = get_game_publisher(conn,'The Witcher 3: Wild Hunt')
    launcher =  get_game_launcher(conn,'The Witcher 3: Wild Hunt')
    platform = get_game_platform(conn,'The Witcher 3: Wild Hunt')
    return create_report("The Witcher 3: Wild Hunt", "The Witcher 3: Wild Hunt", pub, release, platform, lowest_seller, lowest_price)

def dv_pdf(request):
    
    release = get_game_release(conn, 'Divinity: Original Sin 2 - Definitive Edition')
    lowest_seller = get_lowest_seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    lowest_price = get_lowest_price(conn,'Divinity: Original Sin 2 - Definitive Edition')
    dev = get_game_developer(conn,'Divinity: Original Sin 2 - Definitive Edition')
    pub = get_game_publisher(conn,'Divinity: Original Sin 2 - Definitive Edition')
    launcher =  get_game_launcher(conn,'Divinity: Original Sin 2 - Definitive Edition')
    platform = get_game_platform(conn,'Divinity: Original Sin 2 - Definitive Edition')
    return create_report("Divinity: Original Sin 2 - Definitive Edition", "Divinity: Original Sin II", pub, release, platform, lowest_seller, lowest_price)

def rdr2_pdf(request):

    release = get_game_release(conn, 'Red Dead Redemption 2')
    lowest_seller = get_lowest_seller(conn,'Red Dead Redemption 2')
    lowest_price = get_lowest_price(conn,'Red Dead Redemption 2')
    dev = get_game_developer(conn,'Red Dead Redemption 2')
    pub = get_game_publisher(conn,'Red Dead Redemption 2')
    launcher =  get_game_launcher(conn,'Red Dead Redemption 2')
    platform = get_game_platform(conn,'Red Dead Redemption 2')
    return create_report("Red Dead Redemption 2", "Red Dead Redemption 2", pub, release, platform, lowest_seller, lowest_price)

def hades_pdf(request):
    
    release = get_game_release(conn, 'Hades')
    lowest_seller = get_lowest_seller(conn,'Hades')
    lowest_price = get_lowest_price(conn,'Hades')
    dev = get_game_developer(conn,'Hades')
    pub = get_game_publisher(conn,'Hades')
    launcher =  get_game_launcher(conn,'Hades')
    platform = get_game_platform(conn,'Hades')
    return create_report("Hades", "Hades", pub, release, platform, lowest_seller, lowest_price)

def dao_pdf(request):
    release = get_game_release(conn, 'Dragon Age: Origins')
    lowest_seller = get_lowest_seller(conn,'Dragon Age: Origins')
    lowest_price = get_lowest_price(conn,'Dragon Age: Origins')
    dev = get_game_developer(conn,'Dragon Age: Origins')
    pub = get_game_publisher(conn,'Dragon Age: Origins')
    launcher =  get_game_launcher(conn,'Dragon Age: Origins')
    platform = get_game_platform(conn,'Dragon Age: Origins')
    return create_report("Dragon Age: Origins", "Dragon Age: Origins", pub, release, platform, lowest_seller, lowest_price)

def de_pdf(request):
    release = get_game_release(conn, 'Disco Elysium')
    lowest_seller = get_lowest_seller(conn,'Disco Elysium')
    lowest_price = get_lowest_price(conn,'Disco Elysium')
    dev = get_game_developer(conn,'Disco Elysium')
    pub = get_game_publisher(conn,'Disco Elysium')
    launcher =  get_game_launcher(conn,'Disco Elysium')
    platform = get_game_platform(conn,'Disco Elysium')
    return create_report("Disco Elysium", "Disco Elysium", pub, release, platform, lowest_seller, lowest_price)

def bg3_pdf(request):
    release = get_game_release(conn, "Baldur's Gate 3")
    lowest_seller = get_lowest_seller(conn,"Baldur's Gate 3")
    lowest_price = get_lowest_price(conn,"Baldur's Gate 3")
    dev = get_game_developer(conn,"Baldur's Gate 3")
    pub = get_game_publisher(conn,"Baldur's Gate 3")
    launcher =  get_game_launcher(conn,"Baldur's Gate 3")
    platform = get_game_platform(conn,"Baldur's Gate 3")
    return create_report("Baldur's Gate 3", "Baldur's Gate III", pub, release, platform, lowest_seller, lowest_price)

def bioshi_pdf(request):
    release = get_game_release(conn, 'BioShock Infinite')
    lowest_seller = get_lowest_seller(conn,'BioShock Infinite')
    lowest_price = get_lowest_price(conn,'BioShock Infinite')
    dev = get_game_developer(conn,'BioShock Infinite')
    pub = get_game_publisher(conn,'BioShock Infinite')
    launcher =  get_game_launcher(conn,'BioShock Infinite')
    platform = get_game_platform(conn,'BioShock Infinite')
    return create_report("BioShock Infinite", "BioShock Infinite", pub, release, platform, lowest_seller, lowest_price)

def dis_pdf(request):
    release = get_game_release(conn, 'Dishonored')
    lowest_seller = get_lowest_seller(conn,'Dishonored')
    lowest_price = get_lowest_price(conn,'Dishonored')
    dev = get_game_developer(conn,'Dishonored')
    pub = get_game_publisher(conn,'Dishonored')
    launcher =  get_game_launcher(conn,'Dishonored')
    platform = get_game_platform(conn,'Dishonored')
    return create_report("Dishonored", "Dishonored", pub, release, platform, lowest_seller, lowest_price)

def sidmyciv4_pdf(request):
    release = get_game_release(conn, "Sid Meier's Civilization IV")
    lowest_seller = get_lowest_seller(conn,"Sid Meier's Civilization IV")
    lowest_price = get_lowest_price(conn,"Sid Meier's Civilization IV")
    dev = get_game_developer(conn,"Sid Meier's Civilization IV")
    pub = get_game_publisher(conn,"Sid Meier's Civilization IV")
    launcher =  get_game_launcher(conn,"Sid Meier's Civilization IV")
    platform = get_game_platform(conn,"Sid Meier's Civilization IV")
    return create_report("Sid Meier's Civilization IV", "Sid Meier's Civilization IV", pub, release, platform, lowest_seller, lowest_price)

def undertale_pdf(request):
    release = get_game_release(conn, 'Undertale')
    lowest_seller = get_lowest_seller(conn,'Undertale')
    lowest_price = get_lowest_price(conn,'Undertale')
    dev = get_game_developer(conn,'Undertale')
    pub = get_game_publisher(conn,'Undertale')
    launcher =  get_game_launcher(conn,'Undertale')
    platform = get_game_platform(conn,'Undertale')
    return create_report("Undertale", "Undertale", pub, release, platform, lowest_seller, lowest_price)

def sim4_pdf(request):
    release = get_game_release(conn, 'The Sims 4')
    lowest_seller = get_lowest_seller(conn,'The Sims 4')
    lowest_price = get_lowest_price(conn,'The Sims 4')
    dev = get_game_developer(conn,'The Sims 4')
    pub = get_game_publisher(conn,'The Sims 4')
    launcher =  get_game_launcher(conn,'The Sims 4')
    platform = get_game_platform(conn,'The Sims 4')
    return create_report("The Sims 4", "The Sims 4", pub, release, platform, lowest_seller, lowest_price)

def seller(request, name):
    #return HttpResponse(get_game_seller(conn,conn, name))
    return HttpResponse(name)

def prediction(request, name):
    #return HttpResponse(return_prediction(conn, name))
    print(return_prediction(conn, name))

def next(request,game_name):
    seller = seller(game_name)
    return render(request, 'More.html', seller)

def get_hades(request):
    img = img_path('Hades')
    release = get_game_release(conn, 'Hades')
    dev = get_game_developer(conn,'Hades')
    pub = get_game_publisher(conn,'Hades')
    launcher =  get_game_launcher(conn,'Hades')
    platform = get_game_platform(conn,'Hades')
    seller = get_game_1seller(conn,'Hades')
    original = get_game_original_price(conn, 'Hades', seller)
    current = get_game_current_price(conn, 'Hades', seller)
    lowest = get_game_lowest(conn, 'Hades', seller)
    seller2 = get_game_2seller(conn,'Hades')
    original2 = get_game_original_price(conn, 'Hades', seller2)
    current2 = get_game_current_price(conn, 'Hades', seller2)
    lowest2 = get_game_lowest(conn, 'Hades', seller2)
    seller3 = get_game_3seller(conn,'Hades')
    original3 = get_game_original_price(conn, 'Hades', seller3)
    current3 = get_game_current_price(conn, 'Hades', seller3)
    lowest3 = get_game_lowest(conn, 'Hades', seller3)
    seller4 = get_game_4seller(conn,'Hades')
    original4 = get_game_original_price(conn, 'Hades', seller4)
    current4 = get_game_current_price(conn, 'Hades', seller4)
    lowest4 = get_game_lowest(conn, 'Hades', seller4)
    seller5 = get_game_5seller(conn,'Hades')
    original5 = get_game_original_price(conn, 'Hades', seller5)
    current5 = get_game_current_price(conn, 'Hades', seller5)
    lowest5 = get_game_lowest(conn, 'Hades', seller5)
    info = {"DESC": desc5,'Name':'Hades','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info)

def get_TW3(request):
    img = img_path('The Witcher 3: Wild Hunt')
    release = get_game_release(conn, 'The Witcher 3: Wild Hunt')
    dev = get_game_developer(conn,'The Witcher 3: Wild Hunt')
    pub = get_game_publisher(conn,'The Witcher 3: Wild Hunt')
    launcher =  get_game_launcher(conn,'The Witcher 3: Wild Hunt')
    platform = get_game_platform(conn,'The Witcher 3: Wild Hunt')
    seller = get_game_1seller(conn,'The Witcher 3: Wild Hunt')
    original = get_game_original_price(conn, 'The Witcher 3: Wild Hunt', seller)
    current = get_game_current_price(conn, 'The Witcher 3: Wild Hunt', seller)
    lowest = get_game_lowest(conn, 'The Witcher 3: Wild Hunt', seller)
    seller2 = get_game_2seller(conn,'The Witcher 3: Wild Hunt')
    original2 = get_game_original_price(conn, 'The Witcher 3: Wild Hunt', seller2)
    current2 = get_game_current_price(conn, 'The Witcher 3: Wild Hunt', seller2)
    lowest2 = get_game_lowest(conn, 'The Witcher 3: Wild Hunt', seller2)
    seller3 = get_game_3seller(conn,'The Witcher 3: Wild Hunt')
    original3 = get_game_original_price(conn, 'The Witcher 3: Wild Hunt', seller3)
    current3 = get_game_current_price(conn, 'The Witcher 3: Wild Hunt', seller3)
    lowest3 = get_game_lowest(conn, 'The Witcher 3: Wild Hunt', seller3)
    seller4 = get_game_4seller(conn,'The Witcher 3: Wild Hunt')
    original4 = get_game_original_price(conn, 'The Witcher 3: Wild Hunt', seller4)
    current4 = get_game_current_price(conn, 'The Witcher 3: Wild Hunt', seller4)
    lowest4 = get_game_lowest(conn, 'The Witcher 3: Wild Hunt', seller4)
    seller5 = get_game_5seller(conn,'The Witcher 3: Wild Hunt')
    original5 = get_game_original_price(conn, 'The Witcher 3: Wild Hunt', seller5)
    current5 = get_game_current_price(conn, 'The Witcher 3: Wild Hunt', seller5)
    lowest5 = get_game_lowest(conn, 'The Witcher 3: Wild Hunt', seller5)
    info = {"DESC": desc2,'Name':'The Witcher 3: Wild Hunt','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )

def get_GTAV(request):
    img = img_path('Grand Theft Auto V')
    release = get_game_release(conn, 'Grand Theft Auto V')
    dev = get_game_developer(conn,'Grand Theft Auto V')
    pub = get_game_publisher(conn,'Grand Theft Auto V')
    launcher =  get_game_launcher(conn,'Grand Theft Auto V')
    platform = get_game_platform(conn,'Grand Theft Auto V')
    seller = get_game_1seller(conn,'Grand Theft Auto V')
    dev = get_game_developer(conn,'Grand Theft Auto V')
    pub = get_game_publisher(conn,'Grand Theft Auto V')
    launcher =  get_game_launcher(conn,'Grand Theft Auto V')
    platform = get_game_platform(conn,'Grand Theft Auto V')
    original = get_game_original_price(conn, 'Grand Theft Auto V', seller)
    current = get_game_current_price(conn, 'Grand Theft Auto V', seller)
    lowest = get_game_lowest(conn, 'Grand Theft Auto V', seller)
    seller2 = get_game_2seller(conn,'Grand Theft Auto V')
    original2 = get_game_original_price(conn, 'Grand Theft Auto V', seller2)
    current2 = get_game_current_price(conn, 'Grand Theft Auto V', seller2)
    lowest2 = get_game_lowest(conn, 'Grand Theft Auto V', seller2)
    seller3 = get_game_3seller(conn,'Grand Theft Auto V')
    original3 = get_game_original_price(conn, 'Grand Theft Auto V', seller3)
    current3 = get_game_current_price(conn, 'Grand Theft Auto V', seller3)
    lowest3 = get_game_lowest(conn, 'Grand Theft Auto V', seller3)
    seller4 = get_game_4seller(conn,'Grand Theft Auto V')
    original4 = get_game_original_price(conn, 'Grand Theft Auto V', seller4)
    current4 = get_game_current_price(conn, 'Grand Theft Auto V', seller4)
    lowest4 = get_game_lowest(conn, 'Grand Theft Auto V', seller4)
    seller5 = get_game_5seller(conn,'Grand Theft Auto V')
    original5 = get_game_original_price(conn, 'Grand Theft Auto V', seller5)
    current5 = get_game_current_price(conn, 'Grand Theft Auto V', seller5)
    lowest5 = get_game_lowest(conn, 'Grand Theft Auto V', seller5)
    info = {"DESC": desc1, 'Name':'Grand Theft Auto V','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )


def get_DivinityOS2(request):
    img = img_path('Divinity: Original Sin II')
    release = get_game_release(conn, 'Divinity: Original Sin 2 - Definitive Edition')
    dev = get_game_developer(conn,'Divinity: Original Sin 2 - Definitive Edition')
    pub = get_game_publisher(conn,'Divinity: Original Sin 2 - Definitive Edition')
    launcher =  get_game_launcher(conn,'Divinity: Original Sin 2 - Definitive Edition')
    platform = get_game_platform(conn,'Divinity: Original Sin 2 - Definitive Edition')
    seller = get_game_1seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    original = get_game_original_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller)
    current = get_game_current_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller)
    lowest = get_game_lowest(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller)
    seller2 = get_game_2seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    original2 = get_game_original_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller2)
    current2 = get_game_current_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller2)
    lowest2 = get_game_lowest(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller2)
    seller3 = get_game_3seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    original3 = get_game_original_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller3)
    current3 = get_game_current_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller3)
    lowest3 = get_game_lowest(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller3)
    seller4 = get_game_4seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    original4 = get_game_original_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller4)
    current4 = get_game_current_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller4)
    lowest4 = get_game_lowest(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller4)
    seller5 = get_game_5seller(conn,'Divinity: Original Sin 2 - Definitive Edition')
    original5 = get_game_original_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller5)
    current5 = get_game_current_price(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller5)
    lowest5 = get_game_lowest(conn, 'Divinity: Original Sin 2 - Definitive Edition', seller5)
    info = {"DESC": desc3,'Name':'Divinity: Original Sin II - Definitive Edition','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )

def get_DragonAgeOrin(request):
    img = img_path('Dragon Age: Origins')
    release = get_game_release(conn, 'Dragon Age: Origins')
    dev = get_game_developer(conn,'Dragon Age: Origins')
    pub = get_game_publisher(conn,'Dragon Age: Origins')
    launcher =  get_game_launcher(conn,'Dragon Age: Origins')
    platform = get_game_platform(conn,'Dragon Age: Origins')
    seller = get_game_1seller(conn,'Dragon Age: Origins')
    original = get_game_original_price(conn, 'Dragon Age: Origins', seller)
    current = get_game_current_price(conn, 'Dragon Age: Origins', seller)
    lowest = get_game_lowest(conn, 'Dragon Age: Origins', seller)
    seller2 = get_game_2seller(conn,'Dragon Age: Origins')
    original2 = get_game_original_price(conn, 'Dragon Age: Origins', seller2)
    current2 = get_game_current_price(conn, 'Dragon Age: Origins', seller2)
    lowest2 = get_game_lowest(conn, 'Dragon Age: Origins', seller2)
    seller3 = get_game_3seller(conn,'Dragon Age: Origins')
    original3 = get_game_original_price(conn, 'Dragon Age: Origins', seller3)
    current3 = get_game_current_price(conn, 'Dragon Age: Origins', seller3)
    lowest3 = get_game_lowest(conn, 'Dragon Age: Origins', seller3)
    seller4 = get_game_4seller(conn,'Dragon Age: Origins')
    original4 = get_game_original_price(conn, 'Dragon Age: Origins', seller4)
    current4 = get_game_current_price(conn, 'Dragon Age: Origins', seller4)
    lowest4 = get_game_lowest(conn, 'Dragon Age: Origins', seller4)
    seller5 = get_game_5seller(conn,'Dragon Age: Origins')
    original5 = get_game_original_price(conn, 'Dragon Age: Origins', seller5)
    current5 = get_game_current_price(conn, 'Dragon Age: Origins', seller5)
    lowest5 = get_game_lowest(conn, 'Dragon Age: Origins', seller5)
    info = {"DESC": desc6,'Name':'Dragon Age: Origins','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_RedDeadRedemption(request):
    img = img_path('Red Dead Redemption 2')
    release = get_game_release(conn, 'Red Dead Redemption 2')
    dev = get_game_developer(conn,'Red Dead Redemption 2')
    pub = get_game_publisher(conn,'Red Dead Redemption 2')
    launcher =  get_game_launcher(conn,'Red Dead Redemption 2')
    platform = get_game_platform(conn,'Red Dead Redemption 2')
    seller = get_game_1seller(conn,'Red Dead Redemption 2')
    original = get_game_original_price(conn, 'Red Dead Redemption 2', seller)
    current = get_game_current_price(conn, 'Red Dead Redemption 2', seller)
    lowest = get_game_lowest(conn, 'Red Dead Redemption 2', seller)
    seller2 = get_game_2seller(conn,'Red Dead Redemption 2')
    original2 = get_game_original_price(conn, 'Red Dead Redemption 2', seller2)
    current2 = get_game_current_price(conn, 'Red Dead Redemption 2', seller2)
    lowest2 = get_game_lowest(conn, 'Red Dead Redemption 2', seller2)
    seller3 = get_game_3seller(conn,'Red Dead Redemption 2')
    original3 = get_game_original_price(conn, 'Red Dead Redemption 2', seller3)
    current3 = get_game_current_price(conn, 'Red Dead Redemption 2', seller3)
    lowest3 = get_game_lowest(conn, 'Red Dead Redemption 2', seller3)
    seller4 = get_game_4seller(conn,'Red Dead Redemption 2')
    original4 = get_game_original_price(conn, 'Red Dead Redemption 2', seller4)
    current4 = get_game_current_price(conn, 'Red Dead Redemption 2', seller4)
    lowest4 = get_game_lowest(conn, 'Red Dead Redemption 2', seller4)
    seller5 = get_game_5seller(conn,'Red Dead Redemption 2')
    original5 = get_game_original_price(conn, 'Red Dead Redemption 2', seller5)
    current5 = get_game_current_price(conn, 'Red Dead Redemption 2', seller5)
    lowest5 = get_game_lowest(conn, 'Red Dead Redemption 2', seller5)
    info = {"DESC": desc4, 'Name':'Red Dead Redemption 2','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_DiscoElysium(request):
    img = img_path('Disco Elysium')
    release = get_game_release(conn, 'Disco Elysium')
    dev = get_game_developer(conn,'Disco Elysium')
    pub = get_game_publisher(conn,'Disco Elysium')
    launcher =  get_game_launcher(conn,'Disco Elysium')
    platform = get_game_platform(conn,'Disco Elysium')
    seller = get_game_1seller(conn,'Disco Elysium')
    original = get_game_original_price(conn, 'Disco Elysium', seller)
    current = get_game_current_price(conn, 'Disco Elysium', seller)
    lowest = get_game_lowest(conn, 'Disco Elysium', seller)
    seller2 = get_game_2seller(conn,'Disco Elysium')
    original2 = get_game_original_price(conn, 'Disco Elysium', seller2)
    current2 = get_game_current_price(conn, 'Disco Elysium', seller2)
    lowest2 = get_game_lowest(conn, 'Disco Elysium', seller2)
    seller3 = get_game_3seller(conn,'Disco Elysium')
    original3 = get_game_original_price(conn, 'Disco Elysium', seller3)
    current3 = get_game_current_price(conn, 'Disco Elysium', seller3)
    lowest3 = get_game_lowest(conn, 'Disco Elysium', seller3)
    seller4 = get_game_4seller(conn,'Disco Elysium')
    original4 = get_game_original_price(conn, 'Disco Elysium', seller4)
    current4 = get_game_current_price(conn, 'Disco Elysium', seller4)
    lowest4 = get_game_lowest(conn, 'Disco Elysium', seller4)
    seller5 = get_game_5seller(conn,'Disco Elysium')
    original5 = get_game_original_price(conn, 'Disco Elysium', seller5)
    current5 = get_game_current_price(conn, 'Disco Elysium', seller5)
    lowest5 = get_game_lowest(conn, 'Disco Elysium', seller5)
    info = {"DESC": desc7,'Name':'Disco Elysium','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_BaldursGate3(request):
    img = img_path("Baldur's Gate III")
    release = get_game_release(conn, "Baldur's Gate 3")
    dev = get_game_developer(conn,"Baldur's Gate 3")
    pub = get_game_publisher(conn,"Baldur's Gate 3")
    launcher =  get_game_launcher(conn,"Baldur's Gate 3")
    platform = get_game_platform(conn,"Baldur's Gate 3")
    seller = get_game_1seller(conn,"Baldur's Gate 3")
    original = get_game_original_price(conn, "Baldur's Gate 3", seller)
    current = get_game_current_price(conn, "Baldur's Gate 3", seller)
    lowest = get_game_lowest(conn, "Baldur's Gate 3", seller)
    seller2 = get_game_2seller(conn,"Baldur's Gate 3")
    original2 = get_game_original_price(conn, "Baldur's Gate 3", seller2)
    current2 = get_game_current_price(conn, "Baldur's Gate 3", seller2)
    lowest2 = get_game_lowest(conn, "Baldur's Gate 3", seller2)
    seller3 = get_game_3seller(conn,"Baldur's Gate 3")
    original3 = get_game_original_price(conn, "Baldur's Gate 3", seller3)
    current3 = get_game_current_price(conn, "Baldur's Gate 3", seller3)
    lowest3 = get_game_lowest(conn, "Baldur's Gate 3", seller3)
    seller4 = get_game_4seller(conn,"Baldur's Gate 3")
    original4 = get_game_original_price(conn, "Baldur's Gate 3", seller4)
    current4 = get_game_current_price(conn, "Baldur's Gate 3", seller4)
    lowest4 = get_game_lowest(conn, "Baldur's Gate 3", seller4)
    seller5 = get_game_5seller(conn,"Baldur's Gate 3")
    original5 = get_game_original_price(conn, "Baldur's Gate 3", seller5)
    current5 = get_game_current_price(conn, "Baldur's Gate 3", seller5)
    lowest5 = get_game_lowest(conn, "Baldur's Gate 3", seller5)
    info = {"DESC": desc8,'Name':"Baldur's Gate 3",'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_BioshockInfinite(request):
    img = img_path('BioShock Infinite')
    release = get_game_release(conn, "BioShock Infinite")
    dev = get_game_developer(conn,"BioShock Infinite")
    pub = get_game_publisher(conn,"BioShock Infinite")
    launcher =  get_game_launcher(conn,"BioShock Infinite")
    platform = get_game_platform(conn,"BioShock Infinite")
    seller = get_game_1seller(conn,"BioShock Infinite")
    original = get_game_original_price(conn, "BioShock Infinite", seller)
    current = get_game_current_price(conn, "BioShock Infinite", seller)
    lowest = get_game_lowest(conn, "BioShock Infinite", seller)
    seller2 = get_game_2seller(conn,"BioShock Infinite")
    original2 = get_game_original_price(conn, "BioShock Infinite", seller2)
    current2 = get_game_current_price(conn, "BioShock Infinite", seller2)
    lowest2 = get_game_lowest(conn, "BioShock Infinite", seller2)
    seller3 = get_game_3seller(conn,"BioShock Infinite")
    original3 = get_game_original_price(conn, "BioShock Infinite", seller3)
    current3 = get_game_current_price(conn, "BioShock Infinite", seller3)
    lowest3 = get_game_lowest(conn, "BioShock Infinite", seller3)
    seller4 = get_game_4seller(conn,"BioShock Infinite")
    original4 = get_game_original_price(conn, "BioShock Infinite", seller4)
    current4 = get_game_current_price(conn, "BioShock Infinite", seller4)
    lowest4 = get_game_lowest(conn, "BioShock Infinite", seller4)
    seller5 = get_game_5seller(conn,"BioShock Infinite")
    original5 = get_game_original_price(conn, "BioShock Infinite", seller5)
    current5 = get_game_current_price(conn, "BioShock Infinite", seller5)
    lowest5 = get_game_lowest(conn, "BioShock Infinite", seller5)
    info = {"DESC": desc9,'Name':"BioShock Infinite",'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
   
def get_Dishonored(request):
    img = img_path("Dishonored")
    release = get_game_release(conn, 'Dishonored')
    dev = get_game_developer(conn,'Dishonored')
    pub = get_game_publisher(conn,'Dishonored')
    launcher =  get_game_launcher(conn,'Dishonored')
    platform = get_game_platform(conn,'Dishonored')
    seller = get_game_1seller(conn,'Dishonored')
    original = get_game_original_price(conn, 'Dishonored', seller)
    current = get_game_current_price(conn, 'Dishonored', seller)
    lowest = get_game_lowest(conn, 'Dishonored', seller)
    seller2 = get_game_2seller(conn,'Dishonored')
    original2 = get_game_original_price(conn, 'Dishonored', seller2)
    current2 = get_game_current_price(conn, 'Dishonored', seller2)
    lowest2 = get_game_lowest(conn, 'Dishonored', seller2)
    seller3 = get_game_3seller(conn,'Dishonored')
    original3 = get_game_original_price(conn, 'Dishonored', seller3)
    current3 = get_game_current_price(conn, 'Dishonored', seller3)
    lowest3 = get_game_lowest(conn, 'Dishonored', seller3)
    seller4 = get_game_4seller(conn,'Dishonored')
    original4 = get_game_original_price(conn, 'Dishonored', seller4)
    current4 = get_game_current_price(conn, 'Dishonored', seller4)
    lowest4 = get_game_lowest(conn, 'Dishonored', seller4)
    seller5 = get_game_5seller(conn,'Dishonored')
    original5 = get_game_original_price(conn, 'Dishonored', seller5)
    current5 = get_game_current_price(conn, 'Dishonored', seller5)
    lowest5 = get_game_lowest(conn, 'Dishonored', seller5)
    info = {"DESC": desc10,'Name':'Dishonored','Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_CivIV(request):
    img = img_path("Sid Meier's Civilization IV")
    release = get_game_release(conn, "Sid Meier's Civilization IV")
    dev = get_game_developer(conn,"Sid Meier's Civilization IV")
    pub = get_game_publisher(conn,"Sid Meier's Civilization IV")
    launcher =  get_game_launcher(conn,"Sid Meier's Civilization IV")
    platform = get_game_platform(conn,"Sid Meier's Civilization IV")
    seller = get_game_1seller(conn,"Sid Meier's Civilization IV")
    original = get_game_original_price(conn, "Sid Meier's Civilization IV", seller)
    current = get_game_current_price(conn, "Sid Meier's Civilization IV", seller)
    lowest = get_game_lowest(conn, "Sid Meier's Civilization IV", seller)
    seller2 = get_game_2seller(conn,"Sid Meier's Civilization IV")
    original2 = get_game_original_price(conn, "Sid Meier's Civilization IV", seller2)
    current2 = get_game_current_price(conn, "Sid Meier's Civilization IV", seller2)
    lowest2 = get_game_lowest(conn, "Sid Meier's Civilization IV", seller2)
    seller3 = get_game_3seller(conn,"Sid Meier's Civilization IV")
    original3 = get_game_original_price(conn, "Sid Meier's Civilization IV", seller3)
    current3 = get_game_current_price(conn, "Sid Meier's Civilization IV", seller3)
    lowest3 = get_game_lowest(conn, "Sid Meier's Civilization IV", seller3)
    seller4 = get_game_4seller(conn,"Sid Meier's Civilization IV")
    original4 = get_game_original_price(conn, "Sid Meier's Civilization IV", seller4)
    current4 = get_game_current_price(conn, "Sid Meier's Civilization IV", seller4)
    lowest4 = get_game_lowest(conn, "Sid Meier's Civilization IV", seller4)
    seller5 = get_game_5seller(conn,"Sid Meier's Civilization IV")
    original5 = get_game_original_price(conn, "Sid Meier's Civilization IV", seller5)
    current5 = get_game_current_price(conn, "Sid Meier's Civilization IV", seller5)
    lowest5 = get_game_lowest(conn, "Sid Meier's Civilization IV", seller5)
    info = {"DESC": desc11,'Name':"Sid Meier's Civilization IV",'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_Undertale(request):
    img = img_path("Undertale")
    release = get_game_release(conn, "Undertale")
    dev = get_game_developer(conn,"Undertale")
    pub = get_game_publisher(conn,"Undertale")
    launcher =  get_game_launcher(conn,"Undertale")
    platform = get_game_platform(conn,"Undertale")
    seller = get_game_1seller(conn,"Undertale")
    original = get_game_original_price(conn, "Undertale", seller)
    current = get_game_current_price(conn, "Undertale", seller)
    lowest = get_game_lowest(conn, "Undertale", seller)
    seller2 = get_game_2seller(conn,"Undertale")
    original2 = get_game_original_price(conn, 'Red Dead Redemption 2', seller2)
    current2 = get_game_current_price(conn, "Undertale", seller2)
    lowest2 = get_game_lowest(conn, "Undertale", seller2)
    seller3 = get_game_3seller(conn,"Undertale")
    original3 = get_game_original_price(conn, "Undertale", seller3)
    current3 = get_game_current_price(conn, "Undertale", seller3)
    lowest3 = get_game_lowest(conn, "Undertale", seller3)
    seller4 = get_game_4seller(conn,"Undertale")
    original4 = get_game_original_price(conn, "Undertale", seller4)
    current4 = get_game_current_price(conn, "Undertale", seller4)
    lowest4 = get_game_lowest(conn, "Undertale", seller4)
    seller5 = get_game_5seller(conn,"Undertale")
    original5 = get_game_original_price(conn, "Undertale", seller5)
    current5 = get_game_current_price(conn, "Undertale", seller5)
    lowest5 = get_game_lowest(conn, "Undertale", seller5)
    info = {"DESC": desc12,'Name':"Undertale",'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    

def get_Sims4(request):
    img = img_path("The Sims 4")
    release = get_game_release(conn, "The Sims 4")
    dev = get_game_developer(conn,"The Sims 4")
    pub = get_game_publisher(conn,"The Sims 4")
    launcher =  get_game_launcher(conn,"The Sims 4")
    platform = get_game_platform(conn,"The Sims 4")
    seller = get_game_1seller(conn,"The Sims 4")
    original = get_game_original_price(conn, "The Sims 4", seller)
    current = get_game_current_price(conn, "The Sims 4", seller)
    lowest = get_game_lowest(conn, "The Sims 4", seller)
    seller2 = get_game_2seller(conn,"The Sims 4")
    original2 = get_game_original_price(conn, "The Sims 4", seller2)
    current2 = get_game_current_price(conn, "The Sims 4", seller2)
    lowest2 = get_game_lowest(conn, "The Sims 4", seller2)
    seller3 = get_game_3seller(conn,"The Sims 4")
    original3 = get_game_original_price(conn, "The Sims 4", seller3)
    current3 = get_game_current_price(conn, "The Sims 4", seller3)
    lowest3 = get_game_lowest(conn, "The Sims 4", seller3)
    seller4 = get_game_4seller(conn,"The Sims 4")
    original4 = get_game_original_price(conn, "The Sims 4", seller4)
    current4 = get_game_current_price(conn, "The Sims 4", seller4)
    lowest4 = get_game_lowest(conn, "The Sims 4", seller4)
    seller5 = get_game_5seller(conn,"The Sims 4")
    original5 = get_game_original_price(conn, "The Sims 4", seller5)
    current5 = get_game_current_price(conn, "The Sims 4", seller5)
    lowest5 = get_game_lowest(conn, "The Sims 4", seller5)
    info = {"DESC": desc13,'Name':"The Sims 4",'Seller1': seller,'Seller2': seller2,'Seller3': seller3,'Seller4': seller4,'Seller5': seller5, 'Original': original,
     'Original2': original2,'Original3': original3,'Original4': original4,'Original5': original5, 'Current':current, 'Current2':current2,
     'Current3':current3,'Current4':current4,'Current5':current5,'Lowest':lowest,'Lowest2':lowest2,'Lowest3':lowest3,
     'Lowest4':lowest4,'Lowest5':lowest5,'Image':img, 'Release':release, 'Developer':dev, 'Publisher':pub, 'Launcher':launcher, 'Platform':platform}
    return render(request, 'More.html', info )
    



# prediction(conn, 'Hades')