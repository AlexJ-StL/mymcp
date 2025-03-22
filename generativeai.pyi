from typing import Any, Optional, Union, Dict, List
from google.generativeai.types.generation_types import GenerationConfig


def configure(api_key: str) -> None: ...


class GenerativeModel:
    def __init__(self, model_name: str) -> None: ...

    async def generate_content(
        self,
        prompt: Union[str, List[str], Dict[str, Any]],
        *,
        generation_config: Optional[GenerationConfig] = None,
        safety_settings: Optional[Dict[str, Any]] = None,
        stream: bool = False,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> Any: ...

    async def start_chat(
        self,
        history: Optional[List[Dict[str, Any]]] = None,
        generation_config: Optional[GenerationConfig] = None,
        safety_settings: Optional[Dict[str, Any]] = None,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> Any: ...
