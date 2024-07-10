from src.pipeline import JDExtractor, CVMapper
from src.utils import pdf_to_text


class MappingSystem:
    def __init__(self, extract_type='all'):
        # System components
        self.jd_extractor = JDExtractor()
        self.cv_mapper = CVMapper()
        self.extract_type = extract_type

        # Data update laters
        self.jd = None
        self.requirements = None
        self.cv_dict = {}

    def add_jd(self, jd: str):
        self.jd = jd
        print("Extracting requirements from the JD")
        self.requirements = self.jd_extractor.run(extract_type=self.extract_type, jd=jd)

    def reset_jd(self):
        self.jd = None
        self.requirements = None

    def check_cv(self, cv_desc: str):
        print(f"Mapping CV to requirements")
        out = self.cv_mapper.run(extract_type=self.extract_type, requirements=self.requirements, cv=cv_desc)

        return out
