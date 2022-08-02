from osv.modules import api

api.require('java')

java_cmd = '-Xms64m -Xmx64m -Dvertx.disableDnsResolver=true -jar HelloWorld.jar'
default = api.run(f'/java.so {java_cmd}')
native = api.run(f'/usr/bin/java {java_cmd}')
