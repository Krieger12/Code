import os, time, stat
x = (os.path.dirname(os.path.realpath('__file__')))
print (os.path.dirname(os.path.realpath('__file__')))
#print (os.listdir(x))
for file in os.listdir(x):
    if file.endswith(".pyc"):
        print (file)
        try:
            os.remove(file)
            print ("file removed?" + file)
        except OSError as e: # name the Exception `e`
            print ("Failed with:", e.strerror) # look what it says
            print ("Error code:", e.code )
