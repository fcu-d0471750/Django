from django.shortcuts import render
import os,shutil




def attackhome(request):
    if(os.path.isfile('Script_02/musics/test_case_folder/user_case.py') == True):
       os.remove('Script_02/musics/test_case_folder/user_case.py')

    for i in range(1, 10):
        filename = 'Script_02/musics/code_folder/mutant' + str(i) + '.py'
        if (os.path.isfile(filename) == True):
            os.remove(filename)

    for i in range(1,10):
        #filename = 'Script_02/musics/code_collect_folder/mutant' + str(i) + '/user_case' + str(i) + '.py'
        filename = 'Script_02/musics/code_collect_folder/mutant' + str(i)
        if (os.path.isdir(filename) == True):
            shutil.rmtree(filename)

    return render(request, 'attackpage.html')

def Do_Attack(request):
    # 取得使用者的Test Case-------------------------------------------------------------------------------------------------------------------
    user_test_case = request.GET.get('code')
    file = 'Script_02/musics/test_case_folder/user_case.txt'
    f = open(file, 'w+')
    f.write(str(user_test_case))
    f.seek(0)
    f.close()
    os.rename('Script_02/musics/test_case_folder/user_case.txt', 'Script_02/musics/test_case_folder/user_case.py')

    # 複製Test Case到code_collexct_folder-------------------------------------------------------------------------------------------------------------------
    shutil.copy('Script_02/musics/test_case_folder/user_case.py', 'Script_02/musics/code_collect_folder')

    # 取得Mutant-------------------------------------------------------------------------------------------------------------------
    # textarea數量，最少為1
    textarea_count = 0
    for i in range(1, 10):
        name = 'mutant' + str(i)
        if request.GET.get(name) is not None:
            print(name)
            textarea_count = textarea_count + 1
        else:
            print('break: ', i)
            break

    # 獲取程式碼
    each_code = []
    for i in range(1, textarea_count+1):
        name = 'mutant' + str(i)
        temp = request.GET.get(name)
        each_code.append(temp)
        temp = []

    # 編譯成.py
    filename = 'mutant'
    for i in range(0,textarea_count):
        file = 'Script_02/musics/code_folder/' + filename + str(i+1) + '.txt'
        f = open(file, 'w+')
        f.write(str(each_code[i]))
        f.seek(0)
        f.close()
        os.rename(file, 'Script_02/musics/code_folder/' + filename + str(i+1) + '.py')

    #新增資料夾-------------------------------------------------------------------------------------------------------------------
    for i in range(1,textarea_count+1):
        # 資料夾是否存在
        isexists = os.path.exists('Script_02/musics/code_collect_folder/' + filename + str(i))
        # 如果不存在
        if(isexists == False):os.makedirs('Script_02/musics/code_collect_folder/' + filename + str(i))

    #新增組別:Test Case、Mutant-------------------------------------------------------------------------------------------------------------------
    for i in range(1, textarea_count + 1):
        # 放入資料夾(Test Case)
        #shutil.copy('Script_02/musics/test_case_folder/user_case.py','Script_02/musics/code_collect_folder/' + filename + str(i))
        Test_file = open('Script_02/musics/test_case_folder/user_case.py','r')
        new_Test_file = open('Script_02/musics/code_collect_folder/mutant'+str(i)+'/user_case'+str(i)+'.txt', 'w+')
        new_Test_file.write("from mutant"+str(i)+" import calculator"+"\n" + Test_file.read())
        new_Test_file.seek(0)
        new_Test_file.close()
        os.rename('Script_02/musics/code_collect_folder/mutant'+str(i)+'/user_case'+str(i)+'.txt', 'Script_02/musics/code_collect_folder/mutant'+str(i)+'/user_case'+str(i)+ '.py')
        #放入資料夾(Mutant)
        shutil.copy('Script_02/musics/code_folder/' + filename + str(i) + '.py', 'Script_02/musics/code_collect_folder/' + filename + str(i))

    #執行單元測試-------------------------------------------------------------------------------------------------------------------
    for i in range(1, textarea_count + 1):
        print('-------------------------------')
        print('UnitTest',i,'-------------------------------')
        print('-------------------------------')
        file = 'Script_02/musics/code_collect_folder/mutant'+str(i)+'/user_case'+str(i)+ '.py'
        os.system('python ' + file)
    return render(request, 'hello_django.html')