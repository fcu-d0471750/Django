import os,sys
import coverage
import webbrowser

def webtest():
    # 執行---------------------------------------------------
    os.system("coverage run python_unittest_test.py" )
    # 執行---------------------------------------------------
    os.system("coverage report -m")
    # 執行---------------------------------------------------
    os.system("coverage html")
    # 執行---------------------------------------------------
    url = "file:///D:/program/pycharm/Python_Django_Test/Script_02/musics/htmlcov/index.html"
    webbrowser.open(url, new=0, autoraise=True)

def remanetxt(code):
    #directory = 'file:///D:/program/pycharm/Python_Django_Test/musics/'
    #os.rename(os.path.join(directory, 'test.txt'), os.path.join(directory, 'filename2.txt'))
    file = 'Script_02/musics/python_unittest_test.txt'
    f = open(file,'w+')
    f.write(code)
    f.seek(0)
    f.close()
    os.rename('Script_02/musics/python_unittest_test.txt', 'Script_02/musics/python_unittest_test.py')


def multiremanetxt(code):
    filename='code'
    for i in range(len(code)):
        file = 'Script_02/musics/code_folder/'+filename+str(i+1)+'.txt'
        f = open(file,'w+')
        f.write(code[i])
        f.seek(0)
        f.close()
        os.rename(file, 'Script_02/musics/code_folder/'+filename+str(i+1)+'.py')

def muldel():
    filename = 'code'
    file_DIR = 'Script_02/musics/code_folder/'
    file_count = len([name for name in os.listdir(file_DIR) if os.path.isfile(os.path.join(file_DIR, name))])
    if(file_count>=1):
        for i in range(1,file_count+1):
            os.remove('Script_02/musics/code_folder/'+filename + str(i)+'.py')