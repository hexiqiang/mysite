from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def index(require):
    # 获取当前时间
    now = datetime.datetime.now()

    return render(require, 'app/index.html', {'get_date': now, })
