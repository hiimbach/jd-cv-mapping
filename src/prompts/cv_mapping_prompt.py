# Mapping task
CV_EXAMPLE = """
Michael Johnson

Email: michael.johnson@example.com
Phone: +1-321-654-9870
Location: 1234 Maple Street, Anytown, USA

Professional Summary

Skilled Deep Learning Engineer with extensive experience in developing and implementing deep learning models. Proficient in using popular deep learning frameworks and programming in Python. Demonstrated ability to handle complex image and speech recognition tasks. Strong problem-solving skills and excellent teamwork abilities.

Work Experience

Deep Learning Engineer
Innovative AI Solutions, Anytown, USA
June 2018 - Present

	- Developed and deployed deep learning models using TensorFlow and PyTorch for various applications, including image classification and object detection.
	- Implemented neural network architectures, focusing on optimizing training methodologies to improve model performance.
	- Worked on multiple image recognition projects, designing models that achieved state-of-the-art accuracy.
	- Effectively communicated technical concepts to non-technical stakeholders.

Machine Learning Specialist
TechVision Labs, Anytown, USA
August 2015 - May 2018

	- Designed and implemented deep learning models for speech recognition tasks using Keras.
	- Conducted extensive data preprocessing and augmentation to enhance the quality of training datasets.
	- Collaborated with data scientists and engineers to refine models and improve overall system performance.
	- Demonstrated strong project management skills, leading several successful projects.

Education

Master of Science in Computer Science
State University, Anytown, USA
Graduated: May 2015

Bachelor of Science in Computer Engineering
State University, Anytown, USA
Graduated: May 2013

Certifications

	- TensorFlow Developer Certificate
	- Certified Machine Learning Specialist

Skills

	- Deep Learning Frameworks (TensorFlow, PyTorch, Keras)
	- Neural Network Architectures and Training
	- Python Programming
	- Image and Speech Recognition
	- Data Preprocessing and Augmentation
	- Problem Solving
	- Teamwork
	- Project Management
	- Communication Skills

Languages

	- English (Fluent)
	- German (Conversational)

Projects

	- Developed an image classification model that achieved over 95% accuracy on a large-scale dataset.
	- Designed a speech recognition system that improved transcription accuracy by 20% over existing models.
"""

MAPPING_REQUIREMENTS_EXAMPLE_HARD_SKILL = """
- Experience with deep learning frameworks such as TensorFlow, PyTorch, or Keras
- Strong understanding of neural network architectures and training methodologies
- Proficiency in Python programming
- Ability to design and implement deep learning models for image and speech recognition tasks
- Experience with large-scale data processing and augmentation
"""
MAPPING_OUTPUT_EXAMPLE_HARD_SKILL = """
{
  "requirements": [
    {
      "requirement": "Experience with deep learning frameworks such as TensorFlow, PyTorch, or Keras",
      "satisfied": true,
      "explanation": "The CV mentions experience in developing and deploying deep learning models using TensorFlow and PyTorch."
    },
    {
      "requirement": "Strong understanding of neural network architectures and training methodologies",
      "satisfied": true,
      "explanation": "The CV highlights the implementation of neural network architectures and optimization of training methodologies."
    },
    {
      "requirement": "Proficiency in Python programming",
      "satisfied": true,
      "explanation": "The CV states proficiency in Python programming."
    },
    {
      "requirement": "Ability to design and implement deep learning models for image and speech recognition tasks",
      "satisfied": true,
      "explanation": "The CV mentions experience in designing models for image classification and speech recognition tasks."
    },
    {
      "requirement": "Experience with large-scale data processing and augmentation",
      "satisfied": false,
      "explanation": null
    }
  ]
}
"""

MAPPING_REQUIREMENTS_EXAMPLE_SOFT_SKILL = """
- Strong problem-solving skills
- Excellent teamwork and collaboration abilities
- Effective communication skills, especially in conveying technical concepts to non-technical stakeholders
- Ability to work under pressure and meet tight deadlines
"""
MAPPING_OUTPUT_EXAMPLE_SOFT_SKILL = """
{
  "requirements": [
    {
      "requirement": "Strong problem-solving skills",
      "satisfied": true,
      "explanation": "The CV mentions strong problem-solving skills in the professional summary and highlights this in the skills section."
    },
    {
      "requirement": "Excellent teamwork and collaboration abilities",
      "satisfied": true,
      "explanation": "The CV mentions excellent teamwork abilities in the professional summary and collaboration with data scientists and engineers in the work experience section."
    },
    {
      "requirement": "Effective communication skills, especially in conveying technical concepts to non-technical stakeholders",
      "satisfied": true,
      "explanation": "The CV includes a specific mention of effectively communicating technical concepts to non-technical stakeholders."
    },
    {
      "requirement": "Ability to work under pressure and meet tight deadlines",
      "satisfied": false,
      "explanation": "The CV does not provide any information or examples indicating the ability to work under pressure or meet tight deadlines."
    }
  ]
}"""

MAPPING_REQUIREMENTS_EXAMPLE_DEGREE = """
- Bachelor’s Degree in Computer Science or equivalent stream
- Master’s Degree in Information Security or Cybersecurity
- Certification in TensorFlow Developer
"""
MAPPING_OUTPUT_EXAMPLE_DEGREE = """
{
  "requirements": [
    {
      "requirement": "Bachelor's Degree in Computer Science or equivalent stream",
      "satisfied": true,
      "explanation": "The CV mentions a Bachelor's Degree in Computer Engineering."
    },
    {
      "requirement": "Master's Degree in Information Security or Cybersecurity",
      "satisfied": false,
      "explanation": "The CV mentions a Master's Degree in Computer Science, not in Information Security or Cybersecurity."
    },
    {
      "requirement": "Certification in TensorFlow Developer",
      "satisfied": true,
      "explanation": "The CV lists a TensorFlow Developer Certificate."
    }
  ]
}
"""

MAPPING_REQUIREMENTS_EXAMPLE_ALL = """
{
  "requirements": [
    {
        "requirement": "Bachelor's Degree in Computer Science or equivalent stream",
        "type": "degree",
    },
    {
        "requirement": "Master's Degree in Information Security or Cybersecurity",
        "type": "degree",
    },
    {
        "requirement": "Strong problem-solving skills",
        "type": "soft_skill",
    },
    {
        "requirement": "Excellent teamwork and collaboration abilities",
        "type": "soft_skill",
    },
    {
        "requirement": "Effective communication skills, especially in conveying technical concepts to non-technical stakeholders",
        "type": "soft_skill",
    },
    {
        "requirement": "Ability to work under pressure and meet tight deadlines",
        "type": "soft_skill",
    },
    {
        "requirement": "Strong understanding of neural network architectures and training methodologies",
        "type": "hard_skill",    
    },
    {
        "requirement": "Proficiency in Python programming",
        "type": "hard_skill",
    },
    {
        "requirement": "Ability to design and implement deep learning models for image and speech recognition tasks",
        "type": "hard_skill",
    },
    {
        "requirement": "Experience with large-scale data processing and augmentation",
        "type": "hard_skill",
    }
  ]
}
"""
MAPPING_OUTPUT_EXAMPLE_ALL = """
{
  "requirements": [
    {
      "requirement": "Bachelor's Degree in Computer Science or equivalent stream",
      "type": "degree",
      "satisfied": true,
      "explanation": "The CV mentions a Bachelor's Degree in Computer Engineering from State University, graduated in May 2013."
    },
    {
      "requirement": "Master's Degree in Information Security or Cybersecurity",
      "type": "degree",
      "satisfied": false,
      "explanation": "The CV mentions a Master's Degree in Computer Science from State University, graduated in May 2015, not in Information Security or Cybersecurity."
    },
    {
      "requirement": "Strong problem-solving skills",
      "type": "soft_skill",
      "satisfied": true,
      "explanation": "The CV highlights strong problem-solving skills in the professional summary and skills section."
    },
    {
      "requirement": "Excellent teamwork and collaboration abilities",
      "type": "soft_skill",
      "satisfied": true,
      "explanation": "The CV mentions excellent teamwork abilities in the professional summary and describes collaboration with data scientists and engineers at TechVision Labs."
    },
    {
      "requirement": "Effective communication skills, especially in conveying technical concepts to non-technical stakeholders",
      "type": "soft_skill",
      "satisfied": true,
      "explanation": "The CV mentions effective communication of technical concepts to non-technical stakeholders in the job description at Innovative AI Solutions."
    },
    {
      "requirement": "Ability to work under pressure and meet tight deadlines",
      "type": "soft_skill",
      "satisfied": false,
      "explanation": "The CV does not provide specific examples or mention the ability to work under pressure or meet tight deadlines."
    },
    {
      "requirement": "Strong understanding of neural network architectures and training methodologies",
      "type": "hard_skill",
      "satisfied": true,
      "explanation": "The CV highlights experience with neural network architectures and training methodologies in the job description at Innovative AI Solutions."
    },
    {
      "requirement": "Proficiency in Python programming",
      "type": "hard_skill",
      "satisfied": true,
      "explanation": "The CV states proficiency in Python programming in the skills section."
    },
    {
      "requirement": "Ability to design and implement deep learning models for image and speech recognition tasks",
      "type": "hard_skill",
      "satisfied": true,
      "explanation": "The CV mentions designing models for image classification and speech recognition tasks at both Innovative AI Solutions and TechVision Labs."
    },
    {
      "requirement": "Experience with large-scale data processing and augmentation",
      "type": "hard_skill",
      "satisfied": true,
      "explanation": "The CV mentions experience with data preprocessing and augmentation in the job description at TechVision Labs."
    }
  ]
}
"""

MAPPING_CV_TEMPLATE = """
You are an expert in human resources and you are an expert at understanding which requirement is satisfied by the candidate's resume. Be precise and careful.

Please tell me does the candidate satisfy the following requirement, return by the JSON file format. If the requirements can be satisfied clearly by some point of information, mark it as True, otherwise, mark it as False. If the requirement is not in the resume, mark it as False.
There should be the explanation in the JSON file to explain why the requirement is satisfied or not.
requirement types should stay in ['hard_skill', 'soft_skill', 'degree'].

====== Requirements example start ======
{{requirements_example}}
====== Requirements example end ======

====== CV example start ======
{{cv_example}}
====== CV example end ======

====== Output example start ======
{{output_example}}
====== Output example end ======

====== Requirements start ======
{{requirements}}
====== Requirements end ======

====== CV start ======
{{cv}}
====== CV end ======

====== Output start ======
"""

MAPPING_CV_DICT = {
    "hard_skill": [
        MAPPING_REQUIREMENTS_EXAMPLE_HARD_SKILL,
        MAPPING_OUTPUT_EXAMPLE_HARD_SKILL
    ],
    "soft_skill": [
        MAPPING_REQUIREMENTS_EXAMPLE_SOFT_SKILL,
        MAPPING_OUTPUT_EXAMPLE_SOFT_SKILL
    ],
    "degree": [
        MAPPING_REQUIREMENTS_EXAMPLE_DEGREE,
        MAPPING_OUTPUT_EXAMPLE_DEGREE
    ],
    "all": [
        MAPPING_REQUIREMENTS_EXAMPLE_ALL,
        MAPPING_OUTPUT_EXAMPLE_ALL
    ]
}