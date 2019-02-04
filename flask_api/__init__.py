try:
  import googleclouddebugger
  googleclouddebugger.enable()
except ImportError:
  pass
except RuntimeError:
  pass

import os
import sys
#append to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from run_keras_server import app, celery