from flask import Flask
import subprocess
import time

app= Flask(__name__)
app.debug = True

@app.route("/")
def find_process():
	ps = subprocess.Popen('ps aux'.split(), stdout=subprocess.PIPE)
	grep = subprocess.Popen('grep sleep'.split(), stdin=ps.stdout, stdout=subprocess.PIPE)
	ps.stdout.close()
	output = grep.communicate()[0]
	ps.wait()
	return output

@app.route("/start_process")
def sleep():
	subprocess.Popen(["sleep","200s"])
	return 'Process started'

if __name__ == '__main__':
    app.run()