import os
from abc import abstractmethod

from haystack import Pipeline
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator

os.environ["GOOGLE_API_KEY"] = "AIzaSyAAAR-c4ahbKgIZmRv-6zBUZWWAyJrEHqI"


class LLMPipeline:
    def __init__(self):
        self.llm = GoogleAIGeminiGenerator(model='gemini-pro')

        # Create pipeline
        self.pipeline = Pipeline()
        self.pipeline.add_component(instance=self.llm, name="llm")

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
