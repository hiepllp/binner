
import cherrypy
class RuntimeWebAPI(object):
  @cherrypy.expose
  @cherrypy.tools.json_in()
  def smallest(self, **params):
    json_request = cherrypy.request.json
    try:
      if isinstance(json_request, dict) and 'items' in json_request.keys() and 'bins' in json_request.keys():
        items = enumerate_json(json_request['items'])
        bins = enumerate_json(json_request['bins'])
        return json.dumps(Algo().find_smallest_bin(ItemCollection(items), BinCollection(bins)).get_smallest().to_dict())
    except: 
      return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""
    return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""

  @cherrypy.expose
  @cherrypy.tools.json_in()
  def single(self, **params):
    json_request = cherrypy.request.json
    try:
      if isinstance(json_request, dict) and 'items' in json_request.keys() and 'bins' in json_request.keys():
        items = enumerate_json(json_request['items'])
        bins = enumerate_json(json_request['bins'])
        
        return Algo().single_bin_packing(ItemCollection(items), BinCollection(bins)).show()
    except:
        return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""

    return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""
      
  @cherrypy.expose
  @cherrypy.tools.json_in()
  def multi(self, **params):
    try:
      json_request = cherrypy.request.json
      if 'items' in json_request.keys() and 'bins' in json_request.keys():
        items = enumerate_json(json_request['items'])
        bins  = enumerate_json(json_request['bins'])
        
        return Algo().multi_bin_packing(ItemCollection(items), BinCollection(bins)).show()
    except:
      return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""

    return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""
    
  @cherrypy.expose
  def index(self, **params):
      output = """<h1>Welcome to the Binner API</1>
      <br>
      to use you go to any of these links:
      <br>
      POST

      <p>
      <a href="/single/">/single/</a>
      <a href="/multi/">/multi/</a>
      <a href="/smallest/">/smallest/</a>

      your request should look like
      curl -H 'Content-Type: application/json' -XPOST -d '{"bins": [{"title": "an example", "w": 100, "h": 100, "d": 100 }], "items": [{"title": "item_1", "w": 100, "h": 100, "d": 100 }]}' """ + str(self.ip) + """:"""  + str(self.port) + """/single/ remember to look up the documentation for more

      </p>
      """
      return output 


