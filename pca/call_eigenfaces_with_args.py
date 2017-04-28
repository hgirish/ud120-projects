import sys
import subprocess
pcas = [10, 15, 25, 50, 100, 250]
f = open('eigenfaces.log','w')
for pca in pcas:
    progname = './eigenfaces.py'
    print("Running {0} {1}".format(progname, pca))
    subprocess.call([sys.executable, progname, str(pca)], stdout=f)