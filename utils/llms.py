import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# load Groq API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in environment. Set it in your .env or env vars."
    )

# set env var (langchain-groq checks this by default, but we also pass it explicitly)
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


class LLMModel:
    def __init__(self, model_name: str = "qwen/qwen3-32b", temperature: float = 0.0):
        """
        model_name: a Groq model id
        temperature: sampling temperature
        """
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        # Pass api_key explicitly to be safe
        self.client = ChatGroq(
            model=self.model_name, temperature=temperature, api_key=GROQ_API_KEY
        )

    def get_model(self):
        return self.client


if __name__ == "__main__":
    llm_instance = LLMModel()
    llm_model = llm_instance.get_model()
    response = llm_model.invoke("Hi, introduce yourself briefly.")

    print(response)
