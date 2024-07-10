import streamlit as st
from src.mapping_system import MappingSystem
from src.utils import pdf_to_text, score_cv
import heapq as hq


# headings
st.set_page_config(page_title="JD-CV Matcher")
st.title("JD-CV Matcher Pipeline")

# Sidebar for parameters
st.sidebar.title("Parameters")
h = st.sidebar.slider('Hard Skill value', value=0.5,
                      min_value=0.0, max_value=1.0)

s = st.sidebar.slider('Soft Skill value', value=0.5,
                      min_value=0.0, max_value=1.0)

d = st.sidebar.slider('Certificates/Degree Value', value=0.5,
                      min_value=0.0, max_value=1.0)

# Initialize the pipeline
pipeline = MappingSystem()


# Option to upload PDF or paste JD text
st.header("Upload JD")
jd_option = st.selectbox("How would you like to provide the JD?", ["Upload PDF", "Paste text"])

if jd_option == "Upload PDF":
    jd_file = st.file_uploader("Upload JD PDF", type=["pdf", "docx"])
    if jd_file:
        jd_text = pdf_to_text(jd_file)
    else:
        jd_upload_status = st.empty()
        jd_upload_status.text("⏳ Waiting for file upload...")
        jd_text = ''

else:
    jd_text = st.text_area("Paste JD text here")


# Upload multiple CVs
st.header("Upload CVs")
cv_files = st.file_uploader("Upload CV PDFs", type=["pdf", "docx"], accept_multiple_files=True)

# Dropdown to select top k
if cv_files:
    k = st.selectbox("Select top k results", range(1, len(cv_files) + 1))
else:
    k = 1

# Process and display results
col1, col2 = st.columns([1, 3])
with col1:
    run_button = st.button("Start Matching")


# Process and display results
if run_button:
    jd_status = st.empty()
    jd_status.text("Processing JD...")
    jd_pbar = st.progress(0)

    # Process JD
    pipeline.add_jd(jd_text)
    st.write(pipeline.requirements)
    jd_status.text("Finished processing JD")
    jd_pbar.progress(100)

    # Process CV
    score_hq = []
    results = {}

    cv_prog = 0
    cv_status = st.empty()
    cv_pbar = st.progress(cv_prog)
    step = 100 / len(cv_files)

    for cv_file in cv_files:
        cv_text = pdf_to_text(cv_file)
        result = pipeline.check_cv(cv_text)
        score = score_cv(h, s, d, result['requirements'])
        results[cv_file.name] = result['requirements']
        hq.heappush(score_hq, (-score, cv_file.name))

        # Update pbar
        cv_prog += step
        if int(cv_prog == 100):
            cv_status.text("Finished processing CVs")
        else:
            cv_status.text(f"Processing CV {cv_file.name}...")
        cv_pbar.progress(int(cv_prog))

    # Output
    st.subheader("Top CVs")

    # Get top k CVs
    for i in range(k):
        score, cv_name = hq.heappop(score_hq)
        st.write()
        with st.expander(f"{cv_name} - Score {-score}"):
            st.write(results[cv_name])
