from haystack.components.builders.prompt_builder import PromptBuilder

from src.pipeline.llm_pipeline import LLMPipeline

PROMPT_FIXING_TEMPLATE = """
This is a JSON that is not formatted correctly. Please fix it so I can parse it by calling json.loads() in Python.
Don't add or remove any data, just fix the formatting.
If the JSON is already correct, return the JSON as it is.

Input JSON:
{{json}}

Output JSON:

"""


class JSONFixer(LLMPipeline):
    def __init__(self):
        super().__init__()
        self.jd_extract_prompt_builder = PromptBuilder(template=PROMPT_FIXING_TEMPLATE)
        self.pipeline.add_component(instance=self.jd_extract_prompt_builder, name="prompts")

        # Connect component
        self.pipeline.connect("prompts", "llm")

    def run(self, json_str: str) -> str:
        prompt_input = {
            "json": json_str
        }
        # print(prompt_input)

        output = self.pipeline.run({"prompts": prompt_input})['llm']['replies'][0]

        return output
