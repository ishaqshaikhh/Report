from django.shortcuts import render
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg
from django.contrib.auth import logout as lgout
import datetime
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def loginUrl(request):
    return render(request, "login.html")

def login_req(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        lg(request, user)
        # Redirect to a success page.
        return render(request, "home.html")  
    else:
        return render(request, "home.html")

@login_required(login_url="login")
def submit(request):
    region = Region.objects.all()
    states = State.objects.all()
    zimmedaris = ZIM
    divisions = Division.objects.all()
    districts = District.objects.all()
    print(divisions)
    return render(request, "submit.html",{"zimmedaris":zimmedaris,"divisions":divisions,"districts":districts})

def logoutUrl(request):
    lgout(request)
    return render(request, "home.html")


@login_required(login_url="login")
def view(request):
    
    cur = datetime.datetime.now().month
    print(cur)
    user = request.user
    
    usr = Zimmedar.objects.get(name=user)
    m1 = Report.objects.filter(created_at__month=cur).filter(alaqa=usr.alaqa)
    tq1 = 0
    ws1 = 0
    tim1 =0 
    tis1 = 0
    sim1 =0
    sis1 =0
    mea1 = 0
    yqmm1 = 0
    yqms1 = 0
    hiram1 = 0
    hiras1 = 0
    isim1= 0
    isis1 = 0

    for a1 in m1:
        tq1 += a1.taqseem
        ws1 += a1.wusool 
        isim1 += a1.islaheaamal_ijtima_maqam
        isis1 += a1.islaheaamal_ijtima_shuraqa
        tim1 += a1.tahajjud_ijtima_maqam 
        tis1 += a1.tahajjud_ijtima_shuraqa 
        sim1 += a1.sehri_ijtima_maqam 
        sis1 += a1.sehri_ijtima_shuraqa
        mea1 += a1.mehboob_e_attar 
        yqmm1 += a1.yaumequfle_madinah_maqam
        yqms1 += a1.yaumequfle_madinah_shuraqa
        hiram1 += a1.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras1+= a1.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
    m2 = Report.objects.filter(created_at__month=cur).filter(district=usr.district)
    
    tq2 = 0
    ws2 = 0
    tim2 =0 
    tis2 = 0
    sim2 =0
    sis2 =0
    mea2 = 0
    yqmm2 = 0
    yqms2 = 0
    hiram2 = 0
    hiras2 = 0
    isim2= 0
    isis2 = 0
    
    for a2 in m2:
        tq2 += a2.taqseem
        ws2 += a2.wusool 
        isim2 += a2.islaheaamal_ijtima_maqam
        isis2 += a2.islaheaamal_ijtima_shuraqa
        tim2 += a2.tahajjud_ijtima_maqam 
        tis2+= a2.tahajjud_ijtima_shuraqa 
        sim2 += a2.sehri_ijtima_maqam 
        sis2+= a2.sehri_ijtima_shuraqa
        mea2 += a2.mehboob_e_attar 
        yqmm2 += a2.yaumequfle_madinah_maqam
        yqms2 += a2.yaumequfle_madinah_shuraqa
        hiram2 += a2.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras2 += a2.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
    m3 = Report.objects.filter(created_at__month=cur).filter(division=usr.district.division_namef)
    tq3 = 0
    ws3 = 0
    tim3 =0 
    tis3 = 0
    sim3 =0
    sis3 =0
    mea3 = 0
    yqmm3 = 0
    yqms3 = 0
    hiram3 = 0
    hiras3 = 0
    isim3 = 0
    isis3 = 0

    for a3 in m3:
        tq3 += a3.taqseem
        ws3 += a3.wusool 
        isim3 += a3.islaheaamal_ijtima_maqam
        isis3 += a3.islaheaamal_ijtima_shuraqa
        tim3 += a3.tahajjud_ijtima_maqam 
        tis3 += a3.tahajjud_ijtima_shuraqa 
        sim3 += a3.sehri_ijtima_maqam 
        sis3 += a3.sehri_ijtima_shuraqa
        mea3 += a3.mehboob_e_attar 
        yqmm3 += a3.yaumequfle_madinah_maqam
        yqms3 += a3.yaumequfle_madinah_shuraqa
        hiram3 += a2.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras3 += a3.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
     
    m4 = Report.objects.filter(created_at__month=cur).filter(state=usr.district.division_namef.state_namef)

    tq4 = 0
    ws4 = 0
    tim4 =0 
    tis4 = 0
    sim4 =0
    sis4 =0
    mea4 = 0
    yqmm4 = 0
    yqms4 = 0
    hiram4 = 0
    hiras4 = 0
    isim4 = 0
    isis4 = 0

    for a4 in m4:
        tq4 += a4.taqseem
        ws4 += a4.wusool 
        isim4 += a4.islaheaamal_ijtima_maqam
        isis4 += a4.islaheaamal_ijtima_shuraqa
        tim4 += a4.tahajjud_ijtima_maqam 
        tis4 += a4.tahajjud_ijtima_shuraqa 
        sim4 += a4.sehri_ijtima_maqam 
        sis4 += a4.sehri_ijtima_shuraqa
        mea4 += a4.mehboob_e_attar 
        yqmm4 += a4.yaumequfle_madinah_maqam
        yqms4 += a4.yaumequfle_madinah_shuraqa
        hiram4 += a4.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras4 += a4.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
    
    m5 = Report.objects.filter(created_at__month=cur).filter(region=usr.district.division_namef.state_namef.region_namef)
    
    tq5 = 0
    ws5 = 0
    tim5 =0 
    tis5 = 0
    sim5 =0
    sis5 =0
    mea5= 0
    yqmm5 = 0
    yqms5 = 0
    hiram5 = 0
    hiras5 = 0
    isim5 = 0
    isis5 = 0

    for a5 in m5:
        tq5 += a5.taqseem
        ws5 += a5.wusool 
        isim5 += a5.islaheaamal_ijtima_maqam
        isis5 += a5.islaheaamal_ijtima_shuraqa
        tim5 += a5.tahajjud_ijtima_maqam 
        tis5+= a5.tahajjud_ijtima_shuraqa 
        sim5 += a5.sehri_ijtima_maqam 
        sis5 += a5.sehri_ijtima_shuraqa
        mea5+= a5.mehboob_e_attar 
        yqmm5 += a5.yaumequfle_madinah_maqam
        yqms5+= a5.yaumequfle_madinah_shuraqa
        hiram5 += a5.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras5 += a5.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
    
    m6 = Report.objects.filter(created_at__month=cur).filter(hind=usr.district.division_namef.state_namef.region_namef.hind_namef)
   
    tq6 = 0
    ws6 = 0
    tim6 =0 
    tis6 = 0
    sim6 =0
    sis6 =0
    mea6= 0
    yqmm6 = 0
    yqms6 = 0
    hiram6 = 0
    hiras6 = 0
    isim6 = 0
    isis6 = 0

    for a6 in m6:
        tq6 += a6.taqseem
        ws6 += a6.wusool 
        isim6 += a6.islaheaamal_ijtima_maqam
        isis6 += a6.islaheaamal_ijtima_shuraqa
        tim6 += a6.tahajjud_ijtima_maqam 
        tis6+= a6.tahajjud_ijtima_shuraqa 
        sim6 += a6.sehri_ijtima_maqam 
        sis6 += a6.sehri_ijtima_shuraqa
        mea6+= a6.mehboob_e_attar 
        yqmm6 += a6.yaumequfle_madinah_maqam
        yqms6+= a6.yaumequfle_madinah_shuraqa
        hiram6 += a6.haftawar_ijtima_main_raat_guzarne_wale_maqam 
        hiras5 += a6.haftawar_ijtima_main_raat_guzarne_wale_Shuraqa 
   
    if request.user.is_authenticated:
        if usr.zimmedari == "Alaqa Zimmedar Naik Aamal":
            return render(request, "alaqa.html",{"m1":m1,"tq2":tq1,"ws2":ws1,"isim":isim1,"isis":isis1,"tim":tim1,"tis":tis1,"sim":sim1,"sis":sis1,"mea":mea1,"yqmm":yqmm1,"yqms":yqms1,"hiram":hiram1,"hiras":hiras1,"usr":usr})
    
        elif usr.zimmedari == "District Zimmedar Naik Aamal":
            return render(request, "district.html",{"m2":m2,"tq2":tq2,"ws2":ws2,"isim":isim2,"isis":isis2,"tim":tim2,"tis":tis2,"sim":sim2,"sis":sis2,"mea":mea2,"yqmm":yqmm2,"yqms":yqms2,"hiram":hiram2,"hiras":hiras2,"usr":usr})
    
        elif usr.zimmedari == "Division Zimmedar Naik Aamal":
            return render(request, "division.html",{"m3":m3,"tq2":tq3,"ws2":ws3,"isim":isim3,"isis":isis3,"tim":tim3,"tis":tis3,"sim":sim3,"sis":sis3,"mea":mea3,"yqmm":yqmm3,"yqms":yqms3,"hiram":hiram3,"hiras":hiras3,"usr":usr})
    
        elif usr.zimmedari == "State Zimmedar Naik Aamal":
            return render(request, "state.html",{"m4":m4,"tq2":tq4,"ws2":ws4,"isim":isim4,"isis":isis4,"tim":tim4,"tis":tis4,"sim":sim4,"sis":sis4,"mea":mea4,"yqmm":yqmm4,"yqms":yqms4,"hiram":hiram4,"hiras":hiras4,"usr":usr})
    
        elif usr.zimmedari == "Region Zimmedar Naik Aamal":
            return render(request, "region.html",{"m5":m5,"tq2":tq5,"ws2":ws5,"isim":isim5,"isis":isis5,"tim":tim5,"tis":tis5,"sim":sim5,"sis":sis5,"mea":mea5,"yqmm":yqmm5,"yqms":yqms5,"hiram":hiram5,"hiras":hiras5,"usr":usr})
    
        elif usr.zimmedari == "Hind Zimmedar Naik Aamal":
            return render(request, "hind.html",{"m6":m6,"tq2":tq6,"ws2":ws6,"isim":isim6,"isis":isis6,"tim":tim6,"tis":tis6,"sim":sim6,"sis":sis6,"mea":mea6,"yqmm":yqmm6,"yqms":yqms6,"hiram":hiram6,"hiras":hiras6,"usr":usr})
    

        else:
            return render(request, "home.html")

    else:
        return render(request, "login.html")

def submitted(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        resp = request.POST.get('zimmedari')
        division_n = request.POST.get('division')
        district_n = request.POST.get('district')
        division_f = Division.objects.get(id=division_n)
        district_f = District.objects.get(id=district_n)
        alaqa = request.POST.get('alaqa')
        taqseem = request.POST.get('taqseem')
        wusool = request.POST.get('wusool')
        state = division_f.state_namef
        sim = request.POST.get('sim')
        sis = request.POST.get('sis')
        tim = request.POST.get('tim')
        tis = request.POST.get('tis')
        mea = request.POST.get('mea')
        yqmm = request.POST.get('yqmm')
        yqms = request.POST.get('yqms')
        iaim = request.POST.get('iaim')
        iais = request.POST.get('iais')
        hiram = request.POST.get('hiram')
        hiras = request.POST.get('hiras')
        print(wusool)
        print(yqmm)
        

        Report(district=district_f,state=state,division=division_f,zimmedari=resp, zimmedar_name=name,alaqa=alaqa, taqseem=taqseem, wusool=wusool, islaheaamal_ijtima_maqam=iaim,islaheaamal_ijtima_shuraqa=iais,tahajjud_ijtima_maqam=tim,tahajjud_ijtima_shuraqa=tis,sehri_ijtima_maqam=sim,sehri_ijtima_shuraqa=sis,mehboob_e_attar=mea,yaumequfle_madinah_maqam=yqmm,yaumequfle_madinah_shuraqa=yqms,haftawar_ijtima_main_raat_guzarne_wale_Shuraqa=hiras,haftawar_ijtima_main_raat_guzarne_wale_maqam=hiram).save()

    return render(request, "home.html") 
@login_required(login_url="login")
def addUser(request):
    zm = Zimmedaris.objects.all()
    districts = District.objects.all()
    return render(request, "register.html",{"zm":zm,"districts":districts})


def userAdded(request):
    
    uname = request.POST['username']
    password = request.POST['password']
    zimmedari = request.POST['zimmedari']
    district_n = request.POST['district']
    district = District.objects.get(id=district_n)
    alaqa = request.POST['alaqa']
    zh = request.POST['zehliHalqa']

    user = User.objects.create_user(uname, "madinah.com", password)
    user.save()
    new_user = Zimmedar(name=uname,zehliHalqa=zh,district=district,alaqa=alaqa,zimmedari=zimmedari,user=user)
    new_user.save()  

    return render(request, "home.html")
# n = int(input("Enter Number to add User:"))
# for i in range(n):

# f1 = input("Enter name of User:")
# f2 = input("Enter name of District:")
# f3 = input("Enter name of Alaqa:")
# f4 = input("Enter name of Zehli Halqa:")
# f5 = input("Enter Password")
# user = User.objects.create_user(f1, "madinah765@gmail.com", f5)
# new_user = Zimmedar(name=f1,zehliHalqa=f4,district=f2,alaqa=f3)
# new_user.save()
# user.save()
     