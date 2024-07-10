from haystack.components.builders.prompt_builder import PromptBuilder

from src.prompts.jd_extraction_prompt import (JD_EXAMPLE,
                                              JD_EXTRACT_TEMPLATE,
                                              JD_EXTRACT_DICT)
from src.pipeline.llm_pipeline import LLMPipeline


class JDExtractor(LLMPipeline):
    def __init__(self):
        super().__init__()
        self.jd_extract_prompt_builder = PromptBuilder(template=JD_EXTRACT_TEMPLATE)
        self.pipeline.add_component(instance=self.jd_extract_prompt_builder, name="prompts")

        # Connect component
        self.pipeline.connect("prompts", "llm")

    def run(self, extract_type: str, jd: str):
        assert extract_type in JD_EXTRACT_DICT, f"Extract type {extract_type} is not supported"

        description, output_example = JD_EXTRACT_DICT[extract_type]

        prompt_input = {
            "description": description,
            "jd_example": JD_EXAMPLE,
            "output_example": output_example,
            "jd": jd
        }
        # print(prompt_input)

        output = self.pipeline.run({"prompts": prompt_input})['llm']['replies'][0]

        # Remove the last line for JSON convert
        output_lines = output.strip().split("\n")
        if output_lines[-1] == "====== Output for job description end ======":
            output_lines.pop()
        final_output = "\n".join(output_lines)

        return final_output
