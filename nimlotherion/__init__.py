
"""

The Nimlotherion is a microframework for creating software which transfers data
from one source to another where ETL (Extract, transform, load), synchronization, 
replication or migration process is used. Therefore is the framework suitable for 
small or big backgroud processes or tasks and needs to be, 
but not necessarily, integrated into another GUI software.

The framework has an option to extract data using web-API, database or flat file
like *.csv*. The loading can be done using any database, usually 
operational database, or a web-API. The transformation process like 
formatting, mapping, cleaning, joining or aggregating of data are the 
core functions of the microframework. 

One of the main advantages of the framework is that there are many functions 
available where the date and time is calculating.

"""

__title__ = "nimlotherion"
__summary__ = "Library"
__url__ = "https://github.com/wamberger/nimlotherion"

__version__ = "0.1.0"

__author__ = "Alan Wamberger"
__status__ = "Alpha"

__license__ = "MIT"
__copyright__ = "2024 %s" % __author__


from nimlotherion.file import read_file
from nimlotherion.file import FileCSV
from nimlotherion.file import FileJSON
from nimlotherion.file import FileTOML
from nimlotherion.file import FileYAML
from nimlotherion.utils import CryptoSafe
from nimlotherion.utils import config
from nimlotherion.utils import Log
from nimlotherion.utils import cli_args
from nimlotherion.utils import Audit
from nimlotherion.utils import Email
from nimlotherion.conn import Database
from nimlotherion.conn import DatabaseHolder
from nimlotherion.conn import RESTapiSession
