import requests as re
import shutil

# run this in console after getting a page
# var a = document.querySelectorAll('div #divImage img')
# var b = []
# for (var i = 0; i < a.length; i++) { b.push(a[i].src) }

# list of urls from website using javascript in chrome devtools console
url_list = ["https://2.bp.blogspot.com/-OP0M0brhN7I/UXv0eu0lTiI/AAAAAAAAJqU/Yu59XqXQ7mg/s0/000.png", "https://2.bp.blogspot.com/-Ut0kPrjp58M/UXv0f2ItSaI/AAAAAAAAJqs/-NAkAzsbegA/s0/001.png", "https://2.bp.blogspot.com/-EMZ4fczdet8/UXv0hJgn4KI/AAAAAAAAJq8/f5hGF8g9tNs/s0/002.png", "https://2.bp.blogspot.com/-AI-3XPqxOyk/UXv0iY-TYgI/AAAAAAAAJrM/BKCoUEu2LUs/s0/003.png", "https://2.bp.blogspot.com/-nhtN2_dD598/UXv0j4Y4vZI/AAAAAAAAJrg/H-kEMtnBfOk/s0/004.png", "https://2.bp.blogspot.com/-RUlZrgbZktw/UXv0kqxj9JI/AAAAAAAAJrw/albdvJ1a86M/s0/005.png", "https://2.bp.blogspot.com/-12cDNs3_pLg/UXv0l9Q-jqI/AAAAAAAAJsE/CXF6qQEUYq4/s0/006.png", "https://2.bp.blogspot.com/-sxApeqTZzHs/UXv0m8bn5NI/AAAAAAAAJsU/Wm0N6PEJAOY/s0/007.png", "https://2.bp.blogspot.com/-5Ijp9VkJ68w/UXv0oAWVHpI/AAAAAAAAJsk/WSr2NiS68J8/s0/008.png", "https://2.bp.blogspot.com/-LDpk6R1nlT8/UXv0pGLEptI/AAAAAAAAJsw/i_hkZL--p-s/s0/009.png", "https://2.bp.blogspot.com/-lWDv2GQoXB4/UXv0p-TILvI/AAAAAAAAJtE/Kn1uDHu2Uvw/s0/010.png", "https://2.bp.blogspot.com/-tNMJ29seUaU/UXv0q_OkivI/AAAAAAAAJtQ/HkbE1hyg_es/s0/011.png", "https://2.bp.blogspot.com/-JvorT2AOcFY/UXv0sAUeHPI/AAAAAAAAJtY/VcePdzTSsD4/s0/012.png", "https://2.bp.blogspot.com/-6uWHBN3EcjA/UXv0tJ3jSAI/AAAAAAAAJtg/1P5prDTdQe0/s0/013.png", "https://2.bp.blogspot.com/-2auEjjPCVAk/UXv0t8zgcSI/AAAAAAAAJts/w7u8khnW4FM/s0/014.png", "https://2.bp.blogspot.com/-yx4Qlt8mwF0/UXv0uxVJjHI/AAAAAAAAJt0/makeWfL332Q/s0/015.png", "https://2.bp.blogspot.com/-WssG1cQLS4o/UXv0vipi0sI/AAAAAAAAJt8/rCDaA55lQcg/s0/016.png", "https://2.bp.blogspot.com/-cw9pC5kNYY4/UXv0wSTDS9I/AAAAAAAAJuE/RuhJEXNaCnU/s0/017.png", "https://2.bp.blogspot.com/-nGxrxKTFPHg/UXv0xew9dUI/AAAAAAAAJuM/ljuwTCrtVqg/s0/018.png", "https://2.bp.blogspot.com/-pJ3LgEEjQcI/UXv0ySYADhI/AAAAAAAAJuU/zLFrMvf60TY/s0/019.png", "https://2.bp.blogspot.com/-EYaaBeurXwo/UXv0zJk-crI/AAAAAAAAJuc/jbYfTu9ud7w/s0/020.png", "https://2.bp.blogspot.com/-h8Fd69atyvg/UXv00PSEAFI/AAAAAAAAJuk/OhVDsd2JZqQ/s0/021.png", "https://2.bp.blogspot.com/-ZGjcrG-Yn7Q/UXv00yItIAI/AAAAAAAAJus/kyRRsseaIN4/s0/022.png", "https://2.bp.blogspot.com/-5R_3mhSgUGc/UXv01s-hWxI/AAAAAAAAJu0/vKl4oHhvuZc/s0/023.png", "https://2.bp.blogspot.com/-Ix79-p4sIgs/UXv02mLDs2I/AAAAAAAAJu8/4ReM3yCgD20/s0/024.png"]

# directory to save the files
save_dir = 'F:\\btech_books\\web_works\\manga-reader\\reader\\mangas\\Kono Bijutsubu ni wa Mondai ga Aru!\\2\\'

log_file = open('download-logs.txt', 'w')
urls_file = open(save_dir + 'urls.txt', 'w')

for url in url_list:
    urls_file.write(url)
    out_file = save_dir + url.split('/')[-1]
    res = re.get(url, stream=True)

    if res.status_code == 200:
        # save the image
        with open(out_file, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        log_file.write(f'<<<DOWNLOADED>>> {url}')
        log_file.write(f'<<<STORED AT>>> {out_file}\n')
        print(f'<<<DOWNLOADED>>> {url}')
    else:
        log_file.write(f'<<<FAILED :: {res.status_code}>>> {url}')
        print(f'<<<FAILED>>> {url}')

log_file.close()
urls_file.close()