import subprocess
import os
import psutil
import time

image_path = "C:/Users/Luke/Desktop/HAMBURGERJPG/bruno-guerrero-kGR0GAZ4Z3s-unsplash.jpg"

# Open the image using the default image viewer
proc = subprocess.Popen(["start", "", image_path], shell=True)
print("Image opened in default viewer. Press Enter to close.")
input()

# Wait a bit to ensure the process starts
time.sleep(1)

# Scan all processes to find the one opening this specific image
found = False
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        if image_path in " ".join(proc.info['cmdline']):
            print(f"Found process for the image: {proc.info['name']} (PID: {proc.info['pid']})")
            proc.terminate()  # Can also use proc.kill()
            found = True
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

if not found:
    print("Could not find the specific process opening the image.")