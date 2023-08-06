

import abc
import logging
import re
from typing import Dict, Optional

from aido.agents import metadata as agent_metadata

# Regex that controls what Func names are allowed.
ACCEPTED_FUNC_NAMES = re.compile(r"^\w+$")

logger = logging.getLogger(__file__)

class AgentBase(abc.ABC):
    def __init__(
        self,
        oauth_params: Optional[oauth.OAuthParams] = None,
    ):
        self.oauth_params = oauth_params
        self._funcs: Dict[str, agent_func.AgentFunc] = {}
        
    @abc.abstractmethod
    def metadata(self) -> agent_metadata.Metadata:
        """Returns metadata about how the agent should be interacted with."""

