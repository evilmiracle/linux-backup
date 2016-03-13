@@ -0,0 +1,28 @@
import os
import time
import pdb


source = ['/root/']  # your need backup the directory
target_dir = '/mnt/' # your put on backup file the directory

today = target_dir+time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

command = raw_input('Enter something -->') # some changed tips if you file changed
if len(command) == 0:
	target = today+os.sep+now+'.zip'
else:
	target = today+os.sep+now+'_'+\
	command.replace('','_')

if os.path.exists(today) != True:
	os.mkdir(today)
	print 'Successfully created directory',today

zip_command = "zip -qr %s %s" % (target,''.join(source))

if os.system(zip_command) == 0:
	print 'Successful back up to',today
else:
	print 'Back up FAILED'
\ No newline at end of file
