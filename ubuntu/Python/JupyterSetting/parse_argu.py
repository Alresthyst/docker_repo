import sys
import os
from optparse import OptionParser


parser = OptionParser()

parser.add_option("-p", "--port", dest="jupyter_port", help="Setting jupyter server port",
                  default=8888)
parser.add_option("-r", "--run_server", dest="jupyter_server_run", help="Choose whether server run or stop",
                  default=True)
(options, args) = parser.parse_args(sys.argv)

if options.jupyter_server_run.lower() != 'false':
	os.system("python3 default_config_print.py")
	command_str = "jupyter notebook --allow-root --port=" + options.jupyter_port
	command_str += " --config jupyter_notebook_config.py --no-browser"
	os.system(command_str)
