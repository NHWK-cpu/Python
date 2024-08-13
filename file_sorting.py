import os

os.chdir('D:\Programing learn\Python\PROJECT\materi') # getting path of the directory

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # split file name and extentsion

    f_title, f_index = f_name.split('-') # split title and index
    
    if not f_index.isdigit():
        f_title, f_index = f_index, f_title

    f_title = f_title.strip()
    f_index = f_index.strip().zfill(3)

    new_name = '{}-{}{}'.format(f_index,f_title,f_ext)

    os.rename(f, new_name)