from osv.modules import api

api.require('java')

#Run with --help to see what all options mean
#Warmup 30s, 1 iteration of 30s with 2 benchmark threads
common_cmd = '/usr/bin/java -Xms1400m -Xmx1400m -jar specjvm.jar -wt 30s -it 30s -bt 2 -i 1 -ikv -ict -ctf false -chf false -crf false'

all = api.run(cmdline=f'{common_cmd} compress crypto serial sunflow scimark!')

derby = api.run(cmdline=f'{common_cmd} derby!')
xml = api.run(cmdline=f'{common_cmd} xml!')

default = api.run(cmdline=f'{common_cmd} sunflow!')
