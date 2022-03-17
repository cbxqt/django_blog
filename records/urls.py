"""定义records的URL模式"""
from django.urls import path
from . import views


app_name = 'records'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # notes
    path('<str:note_topic>/<str:note_title>/', views.title, name='note'),
    # 向我发送邮件
    path('email/', views.email, name='email'),

    # 表单信息
    # 晨午晚检注册
    path('morninng_night_login/', views.morning_night_login, name='morning_night_login'),
]