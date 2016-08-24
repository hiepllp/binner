

class Runtime(object):
  def __init__(self, args):
    self.args = args

  ## deprecated in favour of RuntimeCLI and RuntimeWeb
  def initv1(self, args):
    a = args
    if len(a[0]) > 1:
      first = a[0][1]

      if first == 'web':
        """ add config """
        api = RuntimeAPI(sys.argv)
        global_config = {
          "server.socket_host":api.ip,
          "server.socket_port":api.port
        } 
        my_config = {"/": {}}
        cherrypy.config.update(global_config)
        cherrypy.quickstart(api, "/", config=my_config)
      else:
        RuntimeCLI(a[0][1:])
    else:
      """ no input exit """
      print "You must specify either web or cli as the first argument!"
  ## deprecated in favour of RuntimeCLI and RuntimeWeb
  def initv2(self,*args):
	 RuntimeCLI(*args)


