import glob
import time
for dir in glob.glob("/root/others/sample_code/**"):
    time.sleep(20)
    print(dir)