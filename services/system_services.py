import os
import platform
import subprocess
import psutil

class SystemService: 
    def get_cpu(): 
        if os.name == 'nt': 
            output = subprocess.check_output("wmic cpu get name", shell=True)
            return output.decode().strip().split('\n')[1] 
        else : 
            raise Exception("OS not supported")

    def get_gpu():
        output = subprocess.check_output("wmic path win32_videocontroller get name", shell=True)
        if os.name == 'nt':
            return (output.decode().strip().split("\n")[1])
        else:
            raise Exception("OS not supported")

    def get_ram():
        return(f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)}")

    def get_os(): 
        if os.name == 'nt':
            return platform.system() + " " + platform.release()
        else:
            raise Exception("OS not supported")
        
    def get_all_info_string():
        return "cpu: " +  SystemService.get_cpu() + ", " + " gpu: " +  SystemService.get_gpu()+  ", " + " ram: " +  SystemService.get_ram()+  "GB" +  " os: " +  SystemService.get_os()
    
    def get_all_info():
        return {
            "cpu": SystemService.get_cpu(),
            "gpu": SystemService.get_gpu(),
            "ram": SystemService.get_ram(),
            "os": SystemService.get_os()
        }