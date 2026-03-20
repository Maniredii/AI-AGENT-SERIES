
# Routes queries to local or cloud LLM based on sensitivity

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class ModelGateway:
    """
    Routes queries to the right model based on sensitivity:
    - HIGH sensitivity (patient data, financials) → local model
    - LOW sensitivity (general queries) → cloud model
    """

    def __init__(self):
        # Cloud LLM (OpenAI)
        self.cloud_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        # Local LLM placeholder
        # In production: use Ollama → pip install langchain-ollama
        # self.local_llm = OllamaLLM(model="llama3")
        self.local_llm = None

    def route(self, query, sensitivity="low"):
        """Returns appropriate model for the sensitivity level."""
        if sensitivity == "high":
            if self.local_llm:
                print("🔒 Using local model (high sensitivity)")
                return self.local_llm
            else:
                print("⚠️  Local model not configured — using cloud with caution")
        print("☁️  Using cloud model")
        return self.cloud_llm

    def generate(self, query, sensitivity="low"):
        """Route and generate in one call."""
        model = self.route(query, sensitivity)
        response = model.invoke(query)
        return response.content


# Demo
if __name__ == "__main__":
    gateway = ModelGateway()

    # General query → cloud
    result1 = gateway.generate("What is machine learning?", sensitivity="low")
    print(f"\nCloud result:\n{result1}")

    # Sensitive query → would use local model if configured
    result2 = gateway.generate("Analyze patient symptoms", sensitivity="high")
    print(f"\nSensitive result:\n{result2}")