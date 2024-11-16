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
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# CSS Styling
st.markdown(
    """
    <style>
        .title { font-size: 2.5em; font-weight: bold; text-align: center; color: #4A90E2; margin: 0.5em 0; }
        .stButton > button { background-color: #4A90E2; color: #FFFFFF; border: none; padding: 0.5em 1em; font-size: 1em; border-radius: 10px; transition: 0.3s; }
        .stButton > button:hover { background-color: #357ABD; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Extract text from PDF
def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = "".join(page.extract_text() or "" for page in reader.pages)
        return text
    except Exception as e:
        st.error("Failed to extract text from PDF.")
        return ""

# Extract text from JSON
def extract_text_from_json(file):
    try:
        data = json.load(file)
        return json.dumps(data, indent=2)  # Converts JSON data to readable string
    except Exception as e:
        st.error("Failed to parse JSON file.")
        return ""

# Summarize text
def summarize_text(text, max_length=200, min_length=100, length_penalty=1.5, summary_type='paragraph'):
    try:
        inputs = tokenizer.encode(
            "summarize: " + text,
            return_tensors="pt",
            max_length=512,
            truncation=True,
        ).to(model.device)
        
        summary_ids = model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            length_penalty=length_penalty,
            num_beams=4,
            early_stopping=True,
        )
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # If points are requested, split summary into points
        if summary_type == 'points':
            summary = summary.replace('. ', '.\n- ')
            summary = '- ' + summary  # Add bullet points to start
        
        return summary
    except Exception as e:
        st.error("Error generating summary.")
        return ""

# Save summary to PDF
def create_pdf_in_memory(summary_text):
    try:
        # Create a PDF object
        pdf = FPDF()
        pdf.add_page()

        # Set font for the document
        pdf.set_font("Arial", size=12)

        # Add text content, ensuring it handles long content correctly
        pdf.multi_cell(0, 10, summary_text)

        # Save the output to a BytesIO object
        pdf_output = BytesIO()
        pdf.output(pdf_output, dest="S")  # 'S' saves to a string, instead of a file on disk
        pdf_output.seek(0)  # Reset pointer to the start of the BytesIO object
        return pdf_output
    except Exception as e:
        # Catch any exceptions and log them
        st.error(f"Error creating PDF: {e}")
        return None

# App Interface
st.markdown(
    """
    <div style="text-align: center;">
        <img src="/logo_2.png" alt="BrevityAI Logo" style="height: 100px; margin-bottom: 20px;">
    </div>
    <h1 class="title">📄 Text Summarization App</h1>
    """,
    unsafe_allow_html=True,
)

st.write("Upload a PDF/JSON file or enter text to summarize.")

# File upload and manual text input
uploaded_file = st.file_uploader("Upload a file (PDF/JSON)", type=["pdf", "json"])
manual_text = st.text_area("Or, enter text here:", placeholder="Enter text to summarize...")

# Process file or manual input
if uploaded_file or manual_text.strip():
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1].lower()
        extracted_text = ""
        if file_type == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "json":
            extracted_text = extract_text_from_json(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF or JSON file.")
    else:
        extracted_text = manual_text.strip()

    # Display extracted text
    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Content to summarize", extracted_text, height=300)

        # Summary options
        st.subheader("Summary Options")
        max_length = st.slider("Maximum Summary Length", 50, 500, 200)
        min_length = st.slider("Minimum Summary Length", 10, 100, 60)
        length_penalty = st.slider("Length Penalty", 1.0, 3.0, 1.5)
        
        summary_type = st.radio("Choose summary type", ('paragraph', 'points'))

        # Generate summary button
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(extracted_text, max_length, min_length, length_penalty, summary_type)
                if summary:
                    st.subheader("Generated Summary")
                    st.write(summary)

                    # Save and download summary as PDF
                    pdf_output = create_pdf_in_memory(summary)
                    if pdf_output:
                        st.download_button(
                            label="📥 Download Summary as PDF",
                            data=pdf_output,
                            file_name="summary.pdf",
                            mime="application/pdf",
                        )
    else:
        st.error("No text extracted or entered.")
