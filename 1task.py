import os
import psutil
import platform
# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100

print("The CPU usage is : ", cpu_usage)




# Getting all memory using os.popen()
#total_memory, used_memory, free_memory = map(
#int, os.popen('free -t -m').readlines()[-1].split()[1:])

# Memory usage
#print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))
print('RAM memory % used:', psutil.virtual_memory()[2])




#Computer network name
print(f"Computer network name: {platform.node()}")
#Machine type
print(f"Machine type: {platform.machine()}")
#Processor type
print(f"Processor type: {platform.processor()}")
#Platform type
print(f"Platform type: {platform.platform()}")
#Operating system
print(f"Operating system: {platform.system()}")
#Operating system release
print(f"Operating system release: {platform.release()}")
#Operating system version
print(f"Operating system version: {platform.version()}")
