import json
from haystack.components.builders.prompt_builder import PromptBuilder

from src.prompts.cv_mapping_prompt import (CV_EXAMPLE,
                                           MAPPING_CV_TEMPLATE,
                                           MAPPING_CV_DICT)
from src.pipeline import LLMPipeline, JSONFixer


class CVMapper(LLMPipeline):
    def __init__(self):
        super().__init__()
        self.cv_mapping_prompt_builder = PromptBuilder(template=MAPPING_CV_TEMPLATE)
        self.pipeline.add_component(instance=self.cv_mapping_prompt_builder, name="prompts")
        self.json_fixer = JSONFixer()

        # Connect component
        self.pipeline.connect("prompts", "llm")

    def run(self, extract_type: str, requirements: str, cv: str):
        assert extract_type in MAPPING_CV_DICT, f"Extract type {extract_type} is not supported"

        requirements_example, output_example = MAPPING_CV_DICT[extract_type]
        prompt_input = {
            "requirements_example": requirements_example,
            "cv_example": CV_EXAMPLE,
            "output_example": output_example,
            "requirements": requirements,
            "cv": cv
        }

        output_str = self.pipeline.run({"prompts": prompt_input})['llm']['replies'][0]

        # Clean the output
        output_lines = output_str.strip().split("\n")
        if output_lines[-1] == "====== Output end ======":
            output_lines.pop()
        output = "\n".join(output_lines)

        try:
            json_out = json.loads(output)
        except json.JSONDecodeError:
            # If the output is not a valid JSON, try to fix it
            output = self.json_fixer.run(output)
            import ipdb; ipdb.set_trace()
            json_out = json.loads(output)

        return json_out
