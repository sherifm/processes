from flask import Flask
import subprocess
import logging
import psutil

CALL_COUNT=0
p = None

app= Flask(__name__)
app.debug = True

@app.route("/start_process")
def start():
	global p
	try:
		p = subprocess.Popen(["stress","--cpu","8"])
		# p = subprocess.Popen(["sleep","200s"])
		logging.info('Child process started succesfully')
	except:
		logging.error('Could not start process')
	return 'Process started'

@app.route("/stop_process")
def stop():
	global p
	if p is not None:
		if p.poll() is None:
			try:
				kill(p.pid)
				p.wait()
			except:
				p_status='Running process not killed'
				logging.error('Could not kill process')	
		else:
			logging.warning('Process has already been stopped')	
		p_status = p.poll()	
	else:
		p_status = 'No running process found!'
	try:
		p_status = str(p_status)
	except:
		p_status = "conversion failed"
	return 'Attempting stop process. <br> \
		Returned status: {0:s}'.format(p_status)

@app.route("/find_process")
def find_process():
	global CALL_COUNT, p
	CALL_COUNT +=1
	if p is not None:
		p_status = p.poll()
	else:
		p_status = 'No running process found'
	try:
		p_status = str(p_status)
	except:
		p_status = "conversion failed"
	return 'This process has been called {0:d} <br> p_status \
		= {1:s}'.format(CALL_COUNT, p_status)

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()

if __name__ == '__main__':
	logging.getLogger().setLevel(logging.DEBUG)
	app.run()