
# see every files extension 
# same files extension to be placed in a folder 
# create a new folder if it doesn't exist
# notification thats its done sorting



import os
import pathlib
import shutil


current_dir = os.getcwd()

videos_ext = ['.mp4', '.mkv', '.avi','.webm','.3gp']
music_ext = ['.mp3', '.wav' ,'.midi']
pictures_ext =['.jpg', '.jpeg', '.gif', '.png','.svg']

videos_path = os.path.join(os.getcwd(), 'videos')
music_path = os.path.join(os.getcwd(), 'music')
pictures_path = os.path.join(os.getcwd(), 'pictures')

for file in os.listdir(current_dir):
    print(file)
    file_ext = os.path.splitext(file)[1]
    if file_ext in videos_ext:
        if not os.path.exists(videos_path):
            os.mkdir(videos_path)
        else :
            try:
                full_path = os.path.join(os.getcwd(),videos_path)
                file_path = pathlib.PurePath(os.path.join(os.getcwd(), file))
                shutil.move(file_path,full_path)
            except OSError as e:
                  print ('Failed to move video to %s: %s' % (videos_path, e))

    elif file_ext in music_ext:
        if not os.path.exists(music_path):
            os.mkdir(music_path)  

        else:     
            try:
                full_path = os.path.join(os.getcwd(),music_path )
                file_path = pathlib.PurePath(os.path.join(os.getcwd(), file))
                shutil.move(file_path, full_path)  
            except OSError as e:
                print ('Failed to move music to %s: %s' % (music_path, e))

    elif file_ext in pictures_ext:   
        
        if not os.path.exists(pictures_path):
            os.mkdir(pictures_path)
        else:
            try:
                full_path = os.path.join(os.getcwd(),pictures_path )
                file_path = pathlib.PurePath(os.path.join(os.getcwd(), file))
                shutil.move(file_path,full_path)
            except OSError as e:
                print ('Failed to move picture to %s: %s' % (videos_path, e))

    else:
        continue
