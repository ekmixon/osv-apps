from osv.modules import api

api.require('httpserver-html5-gui')
api.require('httpserver-html5-cli')

_exe = '/libhttpserver-api.so --config-file=/etc/httpserver.conf'
daemon = api.run_on_init(f'{_exe} &!')

fg = api.run(_exe)

fg_ssl = api.run(f'{_exe} --ssl')
fg_cors = api.run(f'{_exe} --access-allow=true')

default = daemon
