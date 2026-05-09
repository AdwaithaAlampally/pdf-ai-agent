import streamlit as st
from pypdf import PdfReader
import ollama

# --------------------------------
# PAGE TITLE
# --------------------------------
st.title("📄 AI PDF Summarizer Agent")

st.write("Upload a PDF and get an AI-generated summary using TinyLlama.")

# --------------------------------
# FILE UPLOAD
# --------------------------------
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

# --------------------------------
# WHEN FILE IS UPLOADED
# --------------------------------
if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    full_text = ""

    # Extract text from all pages
    for page in reader.pages:
        text = page.extract_text()

        if text:
            full_text += text + "\n"

    st.write("✅ Text Extracted")

    # Show text length
    st.write(f"Total Characters: {len(full_text)}")

    # Small chunk for TinyLlama
    chunk = full_text[:3000]

    # Button
    if st.button("Generate Summary"):

        with st.spinner("TinyLlama is summarizing..."):

            response = ollama.chat(
                model="tinyllama",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize this PDF:\n\n{chunk}"
                    }
                ]
            )

            summary = response["message"]["content"]

        st.subheader("📌 Summary")

        st.write(summary)