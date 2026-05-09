import streamlit as st
from pypdf import PdfReader
from groq import Groq

st.title("📄 AI PDF Summarizer Agent")

st.write("Upload a PDF and get an AI-generated summary.")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    reader = PdfReader(uploaded_file)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    st.write("✅ Text Extracted")
    st.write(f"Total Characters: {len(full_text)}")

    chunk = full_text[:12000]

    if st.button("Generate Summary"):
        with st.spinner("AI is summarizing..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize this PDF clearly:\n\n{chunk}"
                    }
                ]
            )

            summary = response.choices[0].message.content

        st.subheader("Summary")
        st.write(summary) 