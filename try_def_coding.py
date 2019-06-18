#-*- coding:gb2312 -*-

import os
import shutil
import re

def win10_cmd_popen(command):
    print(command)
    p = os.popen(command) #获取返回值
    print(p.read())
    p.close()

def ffmpeg_union_def_veidos(local_path,file_name,file_type):

    union_str = r'ffmpeg -i E:\spiderFile\bilibili\概率论与数理统计\002?19考研数学概率统计强化第一章随机事件与概率事件的独立性_0.flv -c copy -bsf:v h264_mp4toannexb -f mpegts E:\spiderFile\bilibili\gl\input1.ts'
    print(union_str)
    win10_cmd_popen(union_str)
    union_str = 'ffmpeg -i E:\\spiderFile\\bilibili\\gl\\file1.flv -c copy -bsf:v h264_mp4toannexb -f mpegts E:\\spiderFile\\bilibili\\gl\\input2.ts'
    print(union_str)
    win10_cmd_popen(union_str)
    union_str = 'ffmpeg -i E:\\spiderFile\\bilibili\\gl\\file2.flv -c copy -bsf:v h264_mp4toannexb -f mpegts E:\\spiderFile\\bilibili\\gl\\input3.ts'
    print(union_str)
    win10_cmd_popen(union_str)
    union_str = 'ffmpeg -i E:\\spiderFile\\bilibili\\gl\\file3.flv -c copy -bsf:v h264_mp4toannexb -f mpegts E:\\spiderFile\\bilibili\\gl\\input4.ts'
    print(union_str)
    win10_cmd_popen(union_str)
    union_str = 'ffmpeg -i E:\\spiderFile\\bilibili\\gl\\file4.flv -c copy -bsf:v h264_mp4toannexb -f mpegts E:\\spiderFile\\bilibili\\gl\\input5.ts'
    print(union_str)
    win10_cmd_popen(union_str)
    union_str = 'ffmpeg -i "concat:E:\\spiderFile\\bilibili\\gl\\input1.ts|E:\\spiderFile\\bilibili\\gl\\input2.ts|E:\\spiderFile\\bilibili\\gl\\input3.ts|E:\\spiderFile\\bilibili\\gl\\input4.ts|E:\\spiderFile\\bilibili\\gl\\input5.ts" -c copy -bsf:a aac_adtstoasc -movflags +faststart output.mp4'
    win10_cmd_popen(union_str)

def ffmpeg_union_mp4_mp3(local_path):
    dirList = []
    for dir in os.walk(local_path):
        dirList.append(dir)
    fileList = dirList[0][2]
    for fileName in fileList:
        if fileName[-4:] == '.mp4':
            vediofile = fileName
        elif fileName[-4:] == '.mp3':
            audiofile = fileName
    remove_audio = 'ffmpeg -i '+local_path+'\\'+vediofile+' -c:v copy -an '+local_path+'\\input-no-audio.mp4'
    print(remove_audio)
    win10_cmd_popen(remove_audio)

    add_audio = 'ffmpeg -i '+local_path+'\\input-no-audio.mp4 -i '+local_path+'\\'+audiofile+' -c copy '+local_path+'\\output.mp4'
    win10_cmd_popen(add_audio)

if __name__ == '__main__':
    ffmpeg_union_mp4_mp3(r'E:\spiderFile\bilibili\小鹿')