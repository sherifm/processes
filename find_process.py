import subprocess

ps = subprocess.Popen('ps aux'.split(), stdout=subprocess.PIPE)
grep = subprocess.Popen('grep sleep'.split(), stdin=ps.stdout, stdout=subprocess.PIPE)
ps.stdout.close()
output = grep.communicate()[0]
ps.wait()

print output

