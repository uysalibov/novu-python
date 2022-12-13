"""
Novu Base Class
~~~~~~~~~~~~~~~~~~~
Main class for Novu API
"""

import novu


class Novu:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        
    
