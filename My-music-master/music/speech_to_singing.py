from aip import AipSpeech
import os

'''
Must be absolute path
'''

def create(text, beat_file_path, tmp_file_path, out_putpath):
    APP_ID = '11146787'
    API_KEY = 'KcG5fjvLcdFi6fSR28YpiPIX'
    SECRET_KEY = '5bc350195ef3c592f9499e0172388143'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, { 'spd': 4,'vol': 5,'per':4 })
    # print(result)
    # if not isinstance(result, dict): 
    with open(tmp_file_path, 'wb') as f: 
        f.write(result)
    oscmd = 'ffmpeg.exe -i ' + beat_file_path + ' -i ' + tmp_file_path + ' -filter_complex amix=inputs=2:duration=shortest:dropout_transition=2 -f mp3 ' + out_putpath
    os.system(oscmd)