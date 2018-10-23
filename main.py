# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:56:52 2018

@author: mshem
"""

from PIL import Image

from datetime import datetime

from os import walk
from os.path import join
from glob import glob

from camiryo import astro
from camiryo import color

import ftplib

from time import sleep

h5 = astro.H5(verb=True)
ceu = color.Eumetsat(verb=True)
atime = astro.time(verb=True)

wait_time = 30 #number of minutes to waits before repeat
max_size = [800, 600] #Size limit to devide by two, [width, height]
frames_for_animation = 8 #Number of frame for animation. The lower, the faster

ip = "10.141.3.219"
usr = "admin"
passwd = "********"
remote_path = "/web/dagmam/img/"

root = "D:\\TMet_Products\\"

def create_file(fl, jd, time, typ):
    the_file = open(fl, "w")
    the_file.write("{\n")
    the_file.write("	info: {\n")
    the_file.write("		Time:'{}',\n".format(time))
    the_file.write("		JD: '{}',\n".format(jd))
    the_file.write("		type: '{}',\n".format(typ))
    the_file.write("	}\n")
    the_file.write("}")

def resize_if(image_obj):
    if image_obj.width > max_size[0] or image_obj.height > max_size[1]:
        w = int(image_obj.width / 2)
        h = int(image_obj.height / 2)
        
        return(image_obj.resize((w, h)))
        
    else:
        return(image_obj)
        

def do():
    for path, subdirs, files in walk(root):
        #Remove MPF directory. I don't know how to process MPF files.
        subdirs = [ x for x in subdirs if "MPF" not in x ]
        for name in subdirs:
            the_path = join(path, name)
            all_files = sorted(glob("{}/*.h5".format(the_path)))
            
            if len(all_files) > 0:
                
                last_file = all_files[-1]
                gif_files = all_files[-1 * frames_for_animation:]
                
                info = h5.data(last_file, "TMet_Info")
                p_name = info[0][1].decode('UTF-8')
                p_time = info[4][1].decode('UTF-8')
                the_time = str(datetime.strptime(p_time, '%Y%d%m%H%M'))
                the_jd = atime.jd(the_time)
                
                print(p_name, the_time, the_jd)
            
                session = ftplib.FTP(ip, usr, passwd)
                session.cwd(remote_path)
                
                gif_arr = []
                
                print("\t+Creating gif Day")
                for gif_file in gif_files:
                    gif_arr.append(resize_if(Image.fromarray(ceu.vssdfD(gif_file))))
                    
                gif_arr[0].save('meteosat/anim_{}_D.gif'.format(p_name),
                       format='GIF', save_all=True, append_images=gif_arr[1:],
                       duration=500, loop=0)
                try:
                    file = open('meteosat/anim_{}_D.gif'.format(p_name), 'rb')
                    session.storbinary('STOR meteosat/anim_{}_D.gif'.format(p_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-Gif created Day")
                
                gif_arr = []
                
                print("\t+Creating gif Night")
                for gif_file in gif_files:
                    gif_arr.append(resize_if(Image.fromarray(ceu.cfcN(gif_file))))
                    
                gif_arr[0].save('meteosat/anim_{}_N.gif'.format(p_name),
                       format='GIF', save_all=True, append_images=gif_arr[1:],
                       duration=500, loop=0)
                try:
                    file = open('meteosat/anim_{}_N.gif'.format(p_name), 'rb')
                    session.storbinary('STOR meteosat/anim_{}_N.gif'.format(p_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-Gif created Night")
                
                
                print("\t+Creating vssdfD")
                datavssdfD = ceu.vssdfD(last_file)
                out_file_name = "meteosat/{}_vssdfD".format(p_name)
                imgdatavssdfD = Image.fromarray(datavssdfD)
                imgdatavssdfD = resize_if(imgdatavssdfD)
                imgdatavssdfD.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Vegetation, Snow, Smoke, Dust and Fog (Day)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-vssdfD done")
                
    
                print("\t+Creating ccsfD")
                dataccsfD = ceu.ccsfD(last_file)
                out_file_name = "meteosat/{}_ccsfD".format(p_name)
                imgdataccsfD = Image.fromarray(dataccsfD)
                imgdataccsfD = resize_if(imgdataccsfD)
                imgdataccsfD.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Clouds, Convection, Snow, Fog and Fires (Day)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-ccsfD done")
    
                
                print("\t+Creating sfD")
                datasfD = ceu.sfD(last_file)
                out_file_name = "meteosat/{}_sfD".format(p_name)
                imgdatasfD = Image.fromarray(datasfD)
                imgdatasfD = resize_if(imgdatasfD)
                imgdatasfD.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Snow and Fog (Day)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-sfD done")
    
                print("\t+Creating scD")
                datascD = ceu.scD(last_file)
                out_file_name = "meteosat/{}_scD".format(p_name)
                imgdatascD = Image.fromarray(datascD)
                imgdatascD = resize_if(imgdatascD)
                imgdatascD.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Severe Convection (Day)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-scD done")
    
                print("\t+Creating cfsN")
                datacfcN = ceu.cfcN(last_file)
                out_file_name = "meteosat/{}_cfcN".format(p_name)
                imgdatacfcN = Image.fromarray(datacfcN)
                imgdatacfcN = resize_if(imgdatacfcN)
                imgdatacfcN.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Clouds, Fog and Contrails (Night)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-cfsN done")
    
                print("\t+Creating dtccDN")
                datadtccDN = ceu.dtccDN(last_file)
                out_file_name = "meteosat/{}_dtccDN".format(p_name)
                imgdatadtccDN = Image.fromarray(datadtccDN)
                imgdatadtccDN = resize_if(imgdatadtccDN)
                imgdatadtccDN.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Dust, Thin Clouds and Contrails (Day and Night)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-dtccDN done")
    
    
                print("\t+Creating scjPVaDN")
                datascjPVaDN = ceu.scjPVaDN(last_file)
                out_file_name = "meteosat/{}_scjPVaDN".format(p_name)
                imgdatascjPVaDN = Image.fromarray(datascjPVaDN)
                imgdatascjPVaDN = resize_if(imgdatascjPVaDN)
                imgdatascjPVaDN.save('{}.png'.format(out_file_name))
                create_file("{}.json".format(out_file_name), the_jd, the_time,
                            "Severe Cyclones, Jets and PV Analysis, (Day and Night)")
                
                file = open('{}.png'.format(out_file_name), 'rb')
                session.storbinary('STOR {}.png'.format(out_file_name), file)
                file.close()
                try:
                    file = open('{}.json'.format(out_file_name), 'rb')
                    session.storbinary('STOR {}.json'.format(out_file_name), file)
                    file.close()
                except Exception as e:
                    print("Something went wrong: {}".format(e))
                print("\t\t-scjPVaDN done")
                session.quit()
                
while True:
    do()
    print("Waiting {} minutes".format(wait_time))
    for i in range(wait_time):
        print("\t*{} minutes left to repeat.".format(wait_time - i))
        sleep(60)