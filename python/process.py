import os

'''
# exec command
exe = "D:/workspace/xdelta/xdelta.exe"

argument = [
    'patch',
    'diff.vcdiff',
    'D:/workspace/xdelta/XtAmpTradeClient_win32_rzrk_201601_45th_sp1_sim_6.0.0.5484.exe',
    'XtAmpTradeClient_win32_rzrk_201601_45th_sp1_sim_6.0.0.5492.exe'
]

cmd = exe + " " + ' '.join(argument)
os.system(cmd)
'''

def traverse(path):
    if not os.path.isdir(path):
        print path
        return

    fs = os.listdir(path)
    for f in fs:
        tmp_path = os.path.join(path, f)
        print(tmp_path)
        if os.path.isdir(tmp_path):
            traverse(tmp_path)

path = "D:\\workspace\\python"
traverse(path)
