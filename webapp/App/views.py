import hashlib
import random
from math import ceil
from urllib.parse import unquote

from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from App.models import User, mainPage_img, Inovel
import json


# 主界面
def home(request):
    # print('进入主页面')
    username = request.session.get('username')
    # print(username)
    data = {}
    if username:
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            data['is_login'] = True
            data['is_img'] = True
            data['user'] = user
            data['icon'] = '/static/uploadfiles/' + user.faceimg.url

    return render(request, 'html/main/home.html', context=data)

# 加密密码
def secret_password(password):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'html/main/register.html')
    else:
        user = User()
        user.username = request.POST.get('username')
        password = request.POST.get('password')
        user.password = secret_password(password)
        user.email = request.POST.get('email')
        user.faceimg = request.FILES['icon']

        user.save()

        return render(request, 'html/main/register_middle.html')

# 登录
def login(request):
    # 先跳转到登录页面
    if request.method == 'GET':
        return render(request, 'html/main/login.html')
    else:

        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username)

        if users.exists():
            user = users.first()
            if user.password == secret_password(password):
                request.session['username'] = username
                return redirect(reverse('main:home'))
        else:
            # 跳转到错误提示页面
            return render(request, 'html/main/pwderror.html')

# 注销
def unlogin(request):
    request.session.flush()
    return redirect(reverse('main:home'))

# 更改信息
def upload_info(request):
    username = request.session.get('username')
    if request.method == "GET":
        return render(request, 'html/main/change_userinfo.html')

    else:
        user = User.objects.get(username=username)

        new_name = request.POST.get('username')
        email = request.POST.get('email')

        user.username = new_name
        user.email = email

        user.save()

        return redirect(reverse('main:home'))

# 更改头像
def upload_icon(request):
    username = request.session.get('username')
    if request.method == "GET":
        user = User.objects.get(username=username)
        icon = '/static/uploadfiles/' + user.faceimg.url
        return render(request, 'html/main/upload_icon.html', context={'icon':icon})
    else:
        user = User.objects.get(username=username)
        icon = request.FILES['icon']
        user.faceimg = icon

        user.save()

        return redirect(reverse('main:home'))

# def add_mainpage_img(request):
#     img = mainPage_img()

# 添加实验用假数据
def add_inovel(request):
    type_list = ['玄幻','游戏','武侠']

    for i in range(10):
        inovel = Inovel()
        type = random.choice(type_list)
        num = random.randint(1,100)
        inovel.inovel_name = type + str(num)
        img_list = ['http://d.5857.com/dmdm_20180821/004.jpg','http://d.5857.com/rxdm_170930/001.jpg',
                    'http://d.5857.com/rxdm_170930/002.jpg','http://d.5857.com/rxdm_170930/004.jpg']

        inovel.inovel_cover = random.choice(img_list)
        inovel.inovel_type = type

        inovel.save()

    return HttpResponse('保存成功')

# 这里是测试代码
@csrf_exempt
def test(request):
    data = request.POST.get('word')
    # print(data)
    return HttpResponse('完成')

page_log = []
# 将小说分类,渲染到html页面
@csrf_exempt
def classify_inovel(request):
    data = {
        'status': '200',
    }

    global page_log
    # print(page_log)

    # 获取标签
    label = request.GET.get('label')
    # print(label)

    # 获取页码
    page = request.GET.get('page')

    if page == '上一页':
        page = page_log[-1] - 1
    if page == '下一页':
        page = page_log[-1] + 1
    else:
        page = int(page)

    # 将当前页码记录在列表中
    page_log.append(page)

    # 设置一页小说的个数
    inovel_num = 2
    inovel_list = Inovel.objects.filter(inovel_type=label)
    inovelss = []

    for inovel in inovel_list:
        inovelss.append({
            'inovel_name': inovel.inovel_name,
            'inovel_cover': inovel.inovel_cover.url,
            'inovel_type': inovel.inovel_type,
        })
        # print(inovel.inovel_cover.url)
    data[label] = inovelss[(page-1)*inovel_num:(page-1)*inovel_num+inovel_num]
    data['page_count'] = ceil(len(inovelss) / inovel_num)

    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})

# 每个分类的页面
def fantasy(request):
    return render(request, '../templates/html/classify/fantasy.html')

def qihuan(request):
    return render(request, '../templates/html/classify/qihuan.html')

def swordsman(request):
    return render(request, '../templates/html/classify/swordsman.html')

def xianxia(request):
    return render(request, '../templates/html/classify/xianxia.html')

def city(request):
    return render(request, '../templates/html/classify/city.html')

def reality(request):
    return render(request, '../templates/html/classify/reality.html')

def military(request):
    return render(request, '../templates/html/classify/military.html')

def history(request):
    return render(request, '../templates/html/classify/history.html')

def game(request):
    return render(request, '../templates/html/classify/game.html')

def sport(request):
    return render(request, '../templates/html/classify/sport.html')

def science_fiction(request):
    return render(request, '../templates/html/classify/science_fiction.html')

def spiritual(request):
    return render(request, '../templates/html/classify/spiritual.html')

def girl(request):
    return render(request, '../templates/html/classify/girl.html')

def cartoon(request):
    return render(request, '../templates/html/classify/cartoon.html')

# 输入词提醒,返回提示框json数据
def word_tip(request):
    input_word = request.GET.get('word')
    data = {}

    # 从数据库中查找书名或者作者
    bookname = Inovel.objects.filter(inovel_name__contains=input_word)
    # print(bookname)
    if bookname.exists():
        # print('书名存在')
        inovelss = []

        for inovel in bookname:
            inovelss.append(inovel.inovel_name)
            # print(inovel.inovel_cover.url)
        data[input_word] = inovelss
    else:
        authorname = Inovel.objects.filter(inovel_author__contains=input_word)
        if authorname.exists():
            inovelss = []

            for inovel in authorname:
                if inovel.inovel_author not in inovelss:
                    inovelss.append(inovel.inovel_author)

            data[input_word] = inovelss
    # print(data)
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})

# # 搜索跳转页面
# def find_jump(request):
#     # 获取表单内输入数据
#     return render(request,'find_result.html')


# return_log = []
@csrf_exempt
def return_data(request):
    data = {
        'status': '200',
    }

    # global return_log
    # print(page_log)

    # 获取标签
    word = request.GET.get('word')
    # print(label)

    word = unquote(word)

    # 获取页码
    page = int(request.GET.get('page'))

    # if page == '上一页':
    #     page = page_log[-1] - 1
    # if page == '下一页':
    #     page = page_log[-1] + 1
    # else:
    #     page = int(page)

    # 将当前页码记录在列表中
    # page_log.append(page)

    # # 设置一页小说的个数
    inovel_num = 2
    bookname = Inovel.objects.filter(inovel_name__contains=word)
    inovelss = []

    # print(bookname)
    if bookname.exists():
        # print('书名存在')

        for inovel in bookname:
            inovelss.append(inovel.inovel_name)
            # print(inovel.inovel_cover.url)

    else:
        authorname = Inovel.objects.filter(inovel_author__contains=word)
        if authorname.exists():

            for inovel in authorname:
                if inovel.inovel_author not in inovelss:
                    inovelss.append(inovel.inovel_author)

    data[word] = inovelss[(page - 1) * inovel_num:(page - 1) * inovel_num + inovel_num]
    data['page_count'] = ceil(len(inovelss) / inovel_num)
    print(data)

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


























































