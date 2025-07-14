from deepeval.models.base_model import DeepEvalBaseLLM
import os
import requests
import json
class OllamaEndpointLLM(DeepEvalBaseLLM):
    def __init__(self, model: str):
        self.model_name = model
        self.endpoint_url = os.environ.get("OLLAMA_ENDPOINT_URL", "http://127.0.0.1:11434")
        self.session = requests.Session()

    def load_model(self):
        return None

    def get_model_name(self) -> str:
        return f"ollama:{self.model_name}(env)"

    def generate(self, prompt: str) -> str:
        # print("Prompt:")
        # print(prompt)
        # input()
        resp = self.session.post(
            f"{self.endpoint_url}/v1/completions",
            json={"model": self.model_name, "prompt": prompt},
        )
        resp.raise_for_status()
        data = resp.json()
        # print("Data: ")
        # print(data)
        # input()
        # try common fields
        for key in ("completions", "choices"):  
            if key in data:
                items = data[key]
                first = items[0]
                if isinstance(first, dict):
                    # OpenAI-like choice or Ollama completion
                    return first.get("output") or first.get("text") or first.get("message", {}).get("content", "")
                elif isinstance(first, str):
                    return first
        # fallback
        if isinstance(data, dict) and "output" in data:
            return data["output"]
        raise KeyError(f"No text field in response: {data}")

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)