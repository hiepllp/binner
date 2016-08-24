from binner.runtime import Runtime
from binner.algo_small import AlgoSmallest
from binner.algo_multi import AlgoMulti
from binner.algo_single import AlgoSingle
from binner.collection_bin import BinCollection
from binner.collection_item import ItemCollection
from helpers import enumerate_json
import json
import argparse
class RuntimeCLI(Runtime):
  def __init__(self,args):
	super(RuntimeCLI, self).__init__(args)
        self.initv2( self.args )
  def initv1(self, a):
    for _i in range(0, len(a)):
      i = a[_i]
      try:
        j = a[_i + 1]
      except:
        j = a[_i]
        
      if i in ['-bin', '--bins']:
        self.bins = j 
      if i in ['-i', '--items']:
        self.items = j 
      if i in ['-a', '--algorithm']:
        self.algorithm = j
      if i in ['-h', '--help']:
        self._help()
        return None
    self.run(self)
  def initv2( self, a ):
		
	 parser = argparse.ArgumentParser()
	 ##parser.add_argument("--mode", help="mode, cli or web", default="cli")
	 parser.add_argument("--algorithm", help="algorithm to use 'small' or 'multi' or 'single'", default="single")
	 parser.add_argument("--bins", help="Bins to specify")
	 parser.add_argument("--items", help="Items to specify")
	 parser.add_argument("--host", help="Host to run API on", default="0.0.0.0")
	 parser.add_argument("--port", help="Port to run API on", default=9100)
	 result = parser.parse_args()
	 if len( a ) == 1:
		parser.print_help()
	 else:
	 	self.run( result )
        
  def _help(self):
    print """
usage: binner "{web|cli}" required_input required_input2
options:

SERVER SPECIFIC
--bins Bins to use
--items Items to pack
--algorithm What algorithm to use
"""
  
  def run(self, args):
      bins = BinCollection(enumerate_json(json.loads(args.bins)))
      items = ItemCollection(enumerate_json(json.loads(args.items)))

      if args.algorithm == 'single':
        binner_algo = AlgoSingle(bins,items)
      elif args.algorithm == 'multi':
        binner_algo = AlgoMulti(bins,items)
      else:
        binner_algo = AlgoSmallest(bins,items)
      binner_algo.run()
      print binner_algo.binner.show()


