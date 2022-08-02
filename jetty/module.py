from osv.modules import api

api.require('java')

java_cmd = "-Djetty.base=/jetty/demo-base -jar /jetty/start.jar"

default = api.run(cmdline=f"java.so {java_cmd}")
native = api.run(cmdline=f"/usr/bin/java {java_cmd}")
