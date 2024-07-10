

JD_EXAMPLE = f"""
Application Support Analyst (L2/L3) at Onepoint (PUNE_JD2023-02_IN.007)

Minimum Bachelor's Degree in Computer Science or equivalent stream.

2-3 years experience in Cloud-based (Azure, AWS and Google Cloud) Application Support,
ideally in a Managed service environment.

Experience in supporting core business applications on Azure (Logic apps, Data Factory,
Functions) and Snowflake or equivalent cloud data warehouse.

Experience with REST APls, SQL, JSON, XML.

Experience with Business Intelligence BI and Analytical reporting using PowerBI.
Knowledge in programming languages like Python, Java.

Knowledge about integration platforms or low code platforms.

Exposure to ITIL.

Knowledge in Al, ML preferred.

Excellent interpersonal skills to collaborate with various stakeholders.

A learning enthusiast who would quickly pick up new programming languages, technologies,
and frameworks.

Cisco Certified Network Associate (CCNA)

A proactive Self-Starter with excellent time management skills.

Problem-solving and analytical skills across technical, product, and business questions.
"""

JD_DESCRIPTION = """
Please extract the technical skills.
The skills should be extracted based on some bullet points or main requirements. 
Sub-requirements (the thing listed in a big requirement as some examples) should be describe in that bullet point instead of splitting it into a big new requirement.

Here are some examples of expertise that you might find:
- Experience programming production systems in Python or C++
- Experience building distributed or data intensive systems
- Understand and implement the market research
- Experience with photoshop and illustrator
- SEO and SEM understanding and optimization
- High experience in social media accounts
- Experience with marketing campaigns and strategies
- Experience in organization budget and forecast
- Familiar with MS tools
- Strong knowledge of the VA IO and sub-adviced US retailed market place
Keep wording like this. These are just examples, find it yourself from the JD below
The output should be in JSON format, will "requirement" key for the description and "type" key is for the type of the requirement (hard_skill, soft_skill, degree).

Here is an example of how you extract skills:
"""

JD_OUTPUT_EXAMPLE_ALL = """
{
    "requirements": [
        {
            "requirement": "Bachelor's Degree in Computer Science or equivalent stream",
            "type": "degree"
        },
        {
            "requirement": "2-3 years experience in Cloud-based (Azure, AWS and Google Cloud) Application Support, ideally in a Managed service environment",
            "type": "hard_skill"
        },
        {
            "requirement": "Experience in supporting core business applications on Azure (Logic apps, Data Factory, Functions) and Snowflake or equivalent cloud data warehouse",
            "type": "hard_skill"
        },
        {
            "requirement": "Experience with REST APls, SQL, JSON, XML",
            "type": "hard_skill"
        },
        {
            "requirement": "Experience with Business Intelligence BI and Analytical reporting using PowerBI",
            "type": "hard_skill"
        },
        {
            "requirement": "Knowledge in programming languages like Python, Java",
            "type": "hard_skill"
        },
        {
            "requirement": "Knowledge about integration platforms or low code platforms",
            "type": "hard_skill"
        },
        {
            "requirement": "Exposure to ITIL",
            "type": "hard_skill"
        },
        {
            "requirement": "Knowledge in AI, ML preferred",
            "type": "hard_skill"
        },
        {
            "requirement": "Cisco Certified Network Associate (CCNA)",
            "type": "degree"
        },
        {
            "requirement": "Excellent interpersonal skills to collaborate with various stakeholders",
            "type": "soft_skill"
        },
        {
            "requirement": "A learning enthusiast who would quickly pick up new programming languages, technologies, and frameworks",
            "type": "soft_skill"
        },
        {
            "requirement": "A proactive Self-Starter with excellent time management skills",
            "type": "soft_skill"
        },
        {
            "requirement": "Problem-solving and analytical skills across technical, product, and business questions",
            "type": "soft_skill"
        }
    ]
}
"""
JD_EXAMPLE_ALL = """
- Experience in Cloud-based (Azure, AWS and Google Cloud) Application Support, ideally in a Managed service environment.
- Experience in supporting core business applications on Azure (Logic apps, Data Factory, Functions) and Snowflake or equivalent cloud data warehouse.
- Experience with REST APls, SQL, JSON, XML.
- Experience with Business Intelligence BI and Analytical reporting using PowerBI.
- Knowledge in programming languages like Python, Java.
- Knowledge about integration platforms or low code platforms.
- Exposure to ITIL.
- Knowledge in Al, ML preferred.
- Strong presentation skills
- Excellent problem-solving abilities
- Effective communication skills
- Strong organizational skills
- Ability to work independently and as part of a team
- Adaptability in a fast-paced environment
- Strong leadership and mentorship abilities
- Detail-oriented with strong analytical skills
- Excellent time management skills
- Creative thinking and innovation
- Strong interpersonal skills
- Bachelor's degree in Computer Science or related field
- Master's degree in Business Administration (MBA)
- Certification in Project Management (PMP)
- Certified Public Accountant (CPA)
- Professional Engineer (PE) license
- Certified Information Systems Security Professional (CISSP)
- Certification in Human Resources (PHR or SPHR)
- Certification in Digital Marketing
- AWS Certified Solutions Architect
"""

JD_HARD_SKILL_DESCRIPTION = """
Please extract the technical skills.
The skills should be extracted based on some bullet points or main requirements. 
Sub-requirements (the thing listed in a big requirement as some examples) should be describe in that bullet point instead of splitting it into a big new requirement.

Here are some examples of expertise that you might find:
- Experience programming production systems in Python or C++
- Experience building distributed or data intensive systems
- Understand and implement the market research
- Experience with photoshop and illustrator
- SEO and SEM understanding and optimization
- High experience in social media accounts
- Experience with marketing campaigns and strategies
- Experience in organization budget and forecast
- Familiar with MS tools
- Strong knowledge of the VA IO and sub-adviced US retailed market place
Keep wording like this

Remember to exclude these ALL soft skills and ALL requirements in certification or degree since we DON'T need them.
Here is an example of how you extract skills:
"""
JD_OUTPUT_EXAMPLE_HARD_SKILL = """
- Experience in Cloud-based (Azure, AWS and Google Cloud) Application Support, ideally in a Managed service environment.
- Experience in supporting core business applications on Azure (Logic apps, Data Factory, Functions) and Snowflake or equivalent cloud data warehouse.
- Experience with REST APls, SQL, JSON, XML.
- Experience with Business Intelligence BI and Analytical reporting using PowerBI.
- Knowledge in programming languages like Python, Java.
- Knowledge about integration platforms or low code platforms.
- Exposure to ITIL.
- Knowledge in Al, ML preferred.
"""

JD_SOFT_SKILL_DESCRIPTION = """
Please extract the soft skills.
The skills should be extracted based on some bullet points or main requirements. Sub-requirements (the thing listed in a big requirement as some examples) should be described in that bullet point instead of splitting it into a big new requirement.

Here are some examples of soft skills that you might find:
- Strong presentation skills
- Excellent problem-solving abilities
- Effective communication skills
- Strong organizational skills
- Ability to work independently and as part of a team
- Adaptability in a fast-paced environment
- Strong leadership and mentorship abilities
- Detail-oriented with strong analytical skills
- Excellent time management skills
- Creative thinking and innovation
- Strong interpersonal skills

Remember to extract only the soft skills. Exclude ALL hard skills like technical abilities, programming languages, or software proficiency and ALL requirements in certification or degree.
Here is an example of how you extract skills:
"""
JD_OUTPUT_EXAMPLE_SOFT_SKILL = """
- Excellent written and verbal communication skills in English
- Excellent interpersonal skills to collaborate with various stakeholders
- A learning enthusiast who would quickly pick up new programming languages, technologies, and frameworks
- A proactive self-starter with excellent time management skills
- Problem-solving and analytical skills across technical, product, and business questions
"""

JD_DEGREE_DESCRIPTION = """
Please extract the certifications and degree requirements.
The requirements should be extracted based on some bullet points or main requirements. Sub-requirements (the thing listed in a big requirement as some examples) should be described in that bullet point instead of splitting it into a big new requirement.

Here are some examples of certifications and degrees that you might find:
- Bachelor's degree in Computer Science or related field
- Master's degree in Business Administration (MBA)
- Certification in Project Management (PMP)
- Certified Public Accountant (CPA)
- Professional Engineer (PE) license
- Cisco Certified Network Associate (CCNA)
- Certified Information Systems Security Professional (CISSP)
- Certification in Human Resources (PHR or SPHR)
- Certification in Digital Marketing
- AWS Certified Solutions Architect

Remember to extract only the certifications and degree requirements. Exclude ALL soft skills like communication, teamwork, or problem-solving abilities and ALL hard skills like technical abilities or software proficiency.
Here is an example of how you extract requirements:
"""
JD_OUTPUT_EXAMPLE_DEGREE = """
- Minimum Bachelor’s Degree in Computer Science or equivalent stream
"""

JD_EXTRACT_TEMPLATE = """
{{description}}}

====== Example start ======
{{jd_example}}
====== Example end ======

====== Output for example start ======
{{output_example}}
====== Output for example end ======

====== Job description to extract start ======
{{jd}}
====== Job description to extract end ======

====== Output for job description start ======
"""

JD_EXTRACT_DICT = {
    "hard_skill": [
        JD_HARD_SKILL_DESCRIPTION,
        JD_OUTPUT_EXAMPLE_HARD_SKILL
    ],
    "soft_skill": [
        JD_SOFT_SKILL_DESCRIPTION,
        JD_OUTPUT_EXAMPLE_SOFT_SKILL
    ],
    "degree": [
        JD_DEGREE_DESCRIPTION,
        JD_OUTPUT_EXAMPLE_DEGREE
    ],
    "all": [
        JD_DESCRIPTION,
        JD_OUTPUT_EXAMPLE_ALL
    ]
}