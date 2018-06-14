from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    # Django 中的 render 函数。这个函数的第一个参数是请求对象的，
    # 第二个参数是渲染的模板名。 Django 会自动在所有的应用目录中搜索名为 templates 的文件夹，
    # 然后根据模板中的内容构建一个 HttpResponse 对象
    return render(request, 'home.html')
    # def home_page(request):
    #     if request.method == 'POST':
    #         return HttpResponse(request.POST['item_text'])
    #         return render(request, 'home.html')

    # def home_page(request):
    #     return render(request, 'home.html', {
    #         'new_item_text': request.POST['item_text'],
    #     })

    def home_page(request):
        return render(request, 'home.html', {
            'new_item_text': request.POST.get('item_text', ''),
        })