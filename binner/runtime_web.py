from binner.runtime import Runtime
from runtime import runtime
from runtime_cli import RuntimeCLI
from runtime_web_api import RuntimeWebAPI
import cherrypy


class RuntimeWeb(Runtime, RuntimeCLI):
  def __init__(self,*args):
       super(RuntimeWeb,self).__init__(self,*args)
       self.initv2()
  def run( self, args ):
       api =  RuntimeWebAPI()
       global_config = {
          "server.socket_host": args.host,
          "server.socket_port": args.port
        } 
       my_config = {"/": {}}
       cherrypy.config.update(global_config)
       cherrypy.quickstart(api, "/", config=my_config)


