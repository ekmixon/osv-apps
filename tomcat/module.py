from osv.modules import api

api.require('java8')

_catalina_base = "/usr/tomcat"
_catalina_home = _catalina_base
_catalina_tmpdir = "/tmp/catalina"

_logging_config = [
    f"-Djava.util.logging.config.file={_catalina_base}/conf/logging.properties",
    "-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager",
]

_classpath = [
    f"{_catalina_home}/bin/bootstrap.jar",
    f"{_catalina_base}/bin/tomcat-juli.jar",
]

default = api.run_java(
    classpath=_classpath,
    args=(
        _logging_config
        + [
            f"-Dcatalina.base={_catalina_base}",
            f"-Dcatalina.home={_catalina_base}",
            f"-Djava.io.tmpdir={_catalina_tmpdir}",
            "org.apache.catalina.startup.Bootstrap",
            "start",
        ]
    ),
)
