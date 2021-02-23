from django.shortcuts import render
from Script_02.musics import python_unittest_load



def test1(request):
  return render(request, 'confirm.html')

def index1(request):
    #code_all = request.GET.get('code')  # 獲取程式碼
    #ans = {}
    #ans['head'] = 'hello,' + code_all  #

    #python_unittest_load.remanetxt(code_all) # 編譯成.py
    #python_unittest_load.webtest() # 執行測試

    # 取得textarea數量
    # textarea數量，最少為1
    textarea_count = 1
    for i in range(1,10):
        name = 'code'+str(i)
        if request.GET.get(name) is not None:
            print(name)
            textarea_count = textarea_count + 1
        else :
            print('break: ' , i)
            break

    # 獲取程式碼
    ans = {}
    first_code = request.GET.get('code')
    each_code = []
    each_code.append(first_code)
    ans['head'] = first_code
    for i in range(1,textarea_count):
        name = 'code' + str(i)
        temp = request.GET.get(name)
        each_code.append(temp)
        temp = []

    for i in range(0, textarea_count):
        ans['head'] = ans['head'] + each_code[i]

    python_unittest_load.multiremanetxt(each_code)  # 編譯成.py
    '''
    # 獲取程式碼
    first_code = request.GET.get('code')
    each_code = []
    each_code.append(first_code)
    count11 = request.GET.get('code1')
    each_code.append(count11)
    count11 = request.GET.get('code2')
    each_code.append(count11)

    # 設定回傳值
    ans = {}
    ans['head'] = first_code + "code1: " + each_code[0] + "code2: " + each_code[1];

    python_unittest_load.multiremanetxt(each_code)# 編譯成.py
    '''
    return render(request, 'hello_django.html', ans)


def create_test1(request):
    python_unittest_load.muldel()
    return render(request, 'htmlcreate_test.html')