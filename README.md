# Financial Statement Reader
The CV-JD Matching System is a Retrieval-Augmented Generation (RAG) framework crafted to enhance the recruitment process 
by mapping resumes (CVs) to job descriptions (JDs). This system utilizes advanced prompt engineering and scoring 
algorithms to assess and rank CVs based on the specific requirements outlined in JDs. By integrating sophisticated 
RAG techniques, the system facilitates precise and efficient evaluation of candidate qualifications relative to job 
expectations.


## About the Project
Key features include:

- Using Haystack as PromptBuilder and API Call for RAG.
- Scoring based on the importance of soft skills, hard skils, and certifications/degrees.
- Advanced prompt engineering and RAG to enhance the quality of CV-JD matching.
- A user-friendly interface built with Streamlit.
- Packaging the system into a Docker container for easy deployment.

## Quick Start with Docker
Run the following command to build the Docker image:
```
docker build -t cv . 
```

Run the following command to start the Docker container:
```
docker run -p 8501:8501 cv
```

## Install Python packages
```
pip install -r requirements.txt
```

## Usage
Run the following command to start the Streamlit app:
```
streamlit run app.py
```
In the app you can choose Demo if you dont have a financial statement file to upload.

## Contact 
If you have any questions, feel free to reach out to me at: 
- Email: lenhobach@gmail.com
- GitHub: hiimbach
