class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ParsingError(Error):
  """Exception raise for inability to parse
  
  Attributes:
        message -- explanation of the error
  """

  def __init__(self, message):
    self.message = 'Error Parsing'