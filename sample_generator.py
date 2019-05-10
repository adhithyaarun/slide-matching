import os
import shutil

frames = './frames'
shutil.rmtree(frames, ignore_errors=True)
os.makedirs(frames)
slides = './slides'
shutil.rmtree(slides, ignore_errors=True)
os.makedirs(slides)

for subdir, dirs, files in os.walk('./'):
    for file in files:
        if(subdir not in ['./slides', './frames'] and file.split('.')[1] != "py"):
            if file.split('.')[0] == "ppt":
                print(os.path.join(subdir, file))
                shutil.copy(os.path.join(subdir, file), './slides/')
                os.rename('./slides/ppt.jpg', './slides/'+subdir+'_ppt.jpg')
            else:
                print(os.path.join(subdir, file))
                shutil.copy(os.path.join(subdir, file), './frames/')
                os.rename('./frames'+'/'+file, './frames/'+subdir+'_'+file)
