from typing import ClassVar, Optional, Dict, Any, Union
import aiohttp

from novu import __novu_version__, __version__


class Route:
    BASE = ClassVar[str] = f"https://api.novu.co/{__novu_version__}"

    def __init__(
        self,
        method: str,
        path: str,
        data: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
    ) -> None:
        self.method: str = method
        self.path: str = path
        self.data: Optional[Dict[str, str]] = data
        self.params: Optional[Dict[str, str]] = params
        
class HttpClient:
    def __init__(self, api_key: str) -> None:

        self._headers = {
            "Authorization": f"ApiKey {api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"Novu Python Wrapper novu/{__novu_version__}, novupy/{__version__}"
        }
        self._session = aiohttp.ClientSession(headers=self._headers)
        
    async def request(self, route: Route) -> Any:
        method: str = route.method
        url: str = route.path
        kwargs: Dict[str, Any] = {}
        kwargs["data"] = route.data
        kwargs["params"] = route.params
        
        async with self._session.request(method, url, **kwargs) as response:
            pass