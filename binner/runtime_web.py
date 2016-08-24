from binner.runtime import Runtime
from binner.runtime_cli import RuntimeCLI
from binner.runtime_web_api import RuntimeWebAPI
import cherrypy


class RuntimeWeb(RuntimeCLI):
  def __init__(self,args):
       super(RuntimeWeb,self).__init__(args)
       self.initv2()
  def run( self, args ):
       api =  RuntimeWebAPI()
       global_config = {
          "server.socket_host": args.host,
          "server.socket_port": int(args.port)
        } 
       my_config = {"/": {}}
       cherrypy.config.update(global_config)
       cherrypy.quickstart(api, "/", config=my_config)


