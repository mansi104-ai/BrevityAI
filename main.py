import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from PyPDF2 import PdfReader
import json
from io import BytesIO
from fpdf import FPDF

# Load T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
model = model.to("cuda" if torch.cuda.is_available() else "cpu")

# CSS Styling
st.markdown("""pip
    <style>
        .title {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #4A90E2;
            margin-top: 0.5em;
            margin-bottom: 0.5em;
        }
        .stFileUploader, .stTextArea {
            background-color: #f7f9fc;
            border: 1px solid #cfcfcf;
            padding: 10px;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: #4A90E2;
            color: #FFFFFF;
            border: none;
            padding: 0.5em 1em;
            font-size: 1em;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #357ABD;
        }
        .download-button {
            background-color: #ff6b6b;
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-size: 1em;
            text-decoration: none;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Extract text from JSON
def extract_text_from_json(file):
    data = json.load(file)
    return json.dumps(data, indent=2)  # Converts JSON data to a readable string

# Summarize text with adjustable length parameters
def summarize_text(text, max_length=200, min_length=100, length_penalty=1.5):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True).to(model.device)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=length_penalty,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Save summary to PDF in memory
def create_pdf_in_memory(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary_text)
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

# Streamlit interface
st.markdown('<h1 class="title">📄 Text Summarization App</h1>', unsafe_allow_html=True)
st.write("Upload a PDF or JSON file, or enter text manually to generate a summary!")

# File upload section
uploaded_file = st.file_uploader("Choose a PDF or JSON file", type=["pdf", "json"])
manual_text = st.text_area("Or, enter text here:", placeholder="Enter text to summarize...")

# Summarize text only if there is uploaded file or manually entered text
if uploaded_file is not None or manual_text.strip():
    # Extract text based on file type or use manual input
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        if file_type == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "json":
            extracted_text = extract_text_from_json(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()
    else:
        extracted_text = manual_text.strip()

    # Display extracted or entered text
    st.subheader("Extracted Text")
    st.text_area("Text from file or input", extracted_text, height=300)

    # Generate summary settings
    st.subheader("Summary Options")
    max_length = st.slider("Maximum Summary Length", 50, 500, 200)
    min_length = st.slider("Minimum Summary Length", 30, 150, 100)
    length_penalty = st.slider("Length Penalty", 1.0, 3.0, 1.5)

    # Generate summary button
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(extracted_text, max_length=max_length, min_length=min_length, length_penalty=length_penalty)
        st.subheader("Summary")
        st.write(summary)

        # Save summary as PDF and download
        pdf_output = create_pdf_in_memory(summary)
        st.download_button(label="📥 Download Summary as PDF", data=pdf_output, file_name="summary.pdf", mime="application/pdf")
