# -*- coding: gbk -*-
import urllib2
import datetime
import goslate
import os
import subprocess
import HTMLParser

#CAFE
ALL_SIGN_URL_TARGET = 'http://www.cafeastrology.com/ariesdailyhoroscopetom.html'
Aries_URL_TARGET = 'http://www.cafeastrology.com/dailyhoroscopes/arieshorocodeT.php'
Scorpio_URL_TARGET = 'http://www.cafeastrology.com/dailyhoroscopes/scorpiohorocodeT.php'
Libra_URL_TARGET = 'http://www.cafeastrology.com/dailyhoroscopes/librahorocodeT.php'
#Susan Miller
Sagittarius_URL_TARGET_TEMPLATE = 'http://www.dailyastrologyzone.com/Sample.php?i={0}'
SIGN_DICT = {'aries':Aries_URL_TARGET, 
             'scorpio':Scorpio_URL_TARGET,
             'libra':Libra_URL_TARGET}

def get_cafe(sign):
    f = urllib2.urlopen(SIGN_DICT[sign])
    content = f.readlines()
    
    date_line = content[7]
    astro_line = content[12]
    if len(date_line.strip()) > 50:
        date_str = date_line[127:]
        date_str = date_str[:-8]
        date_str = date_str.lower()
        print date_str
        
        cafe_date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        print cafe_date
        
        astro_str = astro_line[19:]
        astro_str = astro_str[:-3]
        
        html_parser = HTMLParser.HTMLParser()
        astro_str = html_parser.unescape(astro_str)
        print astro_str
        
        cafe_astro = astro_str
        
        return (cafe_date, cafe_astro)

def get_cafe_all_sign():
    f = urllib2.urlopen(ALL_SIGN_URL_TARGET)
    content = f.readlines()
    date_line = ''
    date_line_index = 0
    
    fortune_start_index = 0
    fortune_end_index = 0
    
    for i, a_line in enumerate(content):
        try:
            a_line.index('<h4>The Astrology of Tomorrow - All Signs</h4>')
        except ValueError:
            pass
        else:
            date_line = a_line
            date_line_index = i
        try:
            a_line.index('<h3 style="text-align: center"><a href="thisweekinastrology.html">This Week in')
        except ValueError:
            pass
        else:
            fortune_end_index = i
            
    date_line = content[date_line_index]
    astro_line = content[date_line_index+2:fortune_end_index+1]
    print date_line
    print astro_line
    
    if len(date_line.strip()) > 50:
        date_str = date_line[49:]
        date_str = date_str[:-6]
        date_str = date_str.lower()
        print date_str
        
        cafe_date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        print cafe_date
        
        astro_str = ' '.join([a.strip() for a in astro_line])
        
        print 
        
        astro_str = astro_str[4:]
        astro_str = astro_str[:-78]
        
        html_parser = HTMLParser.HTMLParser()
        astro_str = html_parser.unescape(astro_str)
        print astro_str
        
        cafe_astro = astro_str
        
        return (cafe_date, cafe_astro)

def get_susan(i):
    Sagittarius_URL_TARGET = Sagittarius_URL_TARGET_TEMPLATE.format(i)
    f = urllib2.urlopen(Sagittarius_URL_TARGET)
    content = f.readlines()
    date_line = content[42]
    astro_line = ''
    
    TO_Sagittarius = False
    for line in content:
        if TO_Sagittarius == True:
            astro_line = line
            break
        try:
            line.index('Sagittarius Nov. 23 to Dec. 21')
        except ValueError:
            continue
        TO_Sagittarius = True
    
    date_str = date_line[27:]
    date_str = date_str[:-12]
    date_str = date_str.strip()
    print date_str
    susan_date = datetime.datetime.strptime(date_str, "%A %B %d, %Y")
    print susan_date
    
    if len(astro_line) > 50:
        astro_str = astro_line[27:]
        try:
            astro_str.index('</span></TD>')
        except ValueError:
            pass
        else:
            astro_str = astro_str[:-13]
        astro_str = astro_str.strip()
    
    html_parser = HTMLParser.HTMLParser()
    astro_str = html_parser.unescape(astro_str)
    susan_astro= astro_str
    print susan_astro
    
    return (susan_date, susan_astro)


if __name__ == '__main__':
    gs = goslate.Goslate()
    
    #cafe scorpio
    (cafe_date, cafe_astro) = get_cafe('scorpio')
    cafe_astro_cn = gs.translate(cafe_astro, 'zh')
    
    cafe_date_str_0 = cafe_date.strftime("%Y-%m-%d")
    cafe_date_str_1 = cafe_date.strftime("%Y.%m.%d")
    cafe_file_name = 'cafe_scorpio' + cafe_date_str_0 + ".txt"
    
    f = open(cafe_file_name, 'w')
    f.write("#cafe日运#"+cafe_date_str_1+"#天蝎座#")
    f.write("\n")
    f.write(cafe_date_str_0)
    f.write("\n")
    f.write(cafe_astro)
    f.write("\n")
    f.write("\n")
    f.write(cafe_date_str_0)
    f.write("\n")
    f.write("#cafe日运#"+cafe_date_str_1+"#天蝎座#")
    f.write(cafe_astro_cn.encode("GB18030"))
    f.write("\n")
    f.close()
    subprocess.Popen("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + cafe_file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    #os.system("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + cafe_file_name)
    
    #cafe libra
    (cafe_date, cafe_astro) = get_cafe('libra')
    cafe_astro_cn = gs.translate(cafe_astro, 'zh')
    
    cafe_date_str_0 = cafe_date.strftime("%Y-%m-%d")
    cafe_date_str_1 = cafe_date.strftime("%Y.%m.%d")
    cafe_file_name = 'cafe_libra' + cafe_date_str_0 + ".txt"
    
    f = open(cafe_file_name, 'w')
    f.write("#cafe日运#"+cafe_date_str_1+"#天秤座#")
    f.write("\n")
    f.write(cafe_date_str_0)
    f.write("\n")
    f.write(cafe_astro)
    f.write("\n")
    f.write("\n")
    f.write(cafe_date_str_0)
    f.write("\n")
    f.write("#cafe日运#"+cafe_date_str_1+"#天秤座#")
    f.write(cafe_astro_cn.encode("GB18030"))
    f.write("\n")
    f.close()
    subprocess.Popen("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + cafe_file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    #os.system("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + cafe_file_name)
    
    
    #susan
    for i in range(-20, 8):
        (susan_date, susan_astro) = get_susan(i)
        susan_astro_cn = gs.translate(susan_astro, 'zh')
         
        susan_date_str_0 = susan_date.strftime("%Y-%m-%d")
        susan_date_str_1 = susan_date.strftime("%Y.%m.%d")
        susan_file_name = 'susan_sagittarius' + susan_date_str_0 + ".txt"
         
        if not os.path.exists(susan_file_name): 
            f = open(susan_file_name, 'w')
            f.write("#苏珊米勒日运#"+susan_date_str_1+"#射手座#")
            f.write("\n")
            f.write(susan_date_str_0)
            f.write("\n")
            f.write(susan_astro)
            f.write("\n")
            f.write("\n")
            f.write(susan_date_str_0)
            f.write("\n")
            f.write("#苏珊米勒日运#"+susan_date_str_1+"#射手座#")
            f.write(susan_astro_cn.encode("GB18030"))
            f.write("\n")
            f.close()
     
    tom_date = datetime.date.today() + datetime.timedelta(days=1)
    tom_date_str_0 = tom_date.strftime("%Y-%m-%d")
    tom_file_name = 'susan_sagittarius' + tom_date_str_0 + ".txt"
    subprocess.Popen("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + tom_file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #os.system("\"D:\\Program Files\\Notepad++\\notepad++.exe\" " + susan_file_name)
    