import subprocess
subprocess.check_call("./retrieve_data.sh %s %s %s %s" % (str(5), str(0.6), str(1.8), str(0.4)), shell=True)
