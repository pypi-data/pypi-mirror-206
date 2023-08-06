# encoding: utf-8
import os
import jdk
import time
import glob
import urllib.request
import psutil
from robot.api.deco import keyword

current_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = os.path.dirname(current_path)

class SeleniumGridServer(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 0.1
    
    def __init__(self):
        pass
        
    def killdriver(self):
        for proc in psutil.process_iter():
            if 'chromedriver' in proc.name():
                proc.kill()
            if 'geckodriver' in proc.name():
                proc.kill()
            if 'edgedriver' in proc.name():
                proc.kill()
                
    def java_loader(self):
        if 'windows' in jdk.OS:
            java_name = '%s/jdk*/bin' %(main_path)
        else:
            java_name = '%s/jdk*/Contents/Home/bin' %(main_path)
        os_name = glob.glob(java_name)
        if len(os_name) == 0:
            jdk.install(version='11', path=main_path)
            os_name = glob.glob(java_name)
        return os_name[0].replace('\\', '/')
        
    def selenium(self):
        if not 'selenium-server.jar' in os.listdir(main_path):
            url = 'https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.7.0/selenium-server-4.7.2.jar'
            urllib.request.urlretrieve(url, '%s/selenium-server.jar' %(main_path))
        return '%s/selenium-server.jar' %(main_path)

    @keyword('Start Server')
    def start_Server(self, port=4444):
        self.port = port
        self.killdriver()
        java_path = self.java_loader()
        selenium_path = self.selenium()
        port_num = [i.laddr.port for i in psutil.net_connections()]
        if not port in port_num:
            command = '%s/java -jar %s standalone --port %s' %(java_path, selenium_path, port)
            os.popen(command)
            time.sleep(5)