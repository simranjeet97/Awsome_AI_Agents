import streamlit as st
import os
import io
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# MUST BE FIRST
st.set_page_config(
    page_title="MedGemma AI | Clinical Analysis Dashboard",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

from PIL import Image
import numpy as np
from fpdf import FPDF
from utils.image_processor import MedicalImageProcessor
from core.model_handler import MedGemmaHandler

# --- Load Custom CSS ---
if os.path.exists("assets/styles.css"):
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Initialize Session State ---
if "current_report" not in st.session_state:
    st.session_state.current_report = ""
if "processed_images" not in st.session_state:
    st.session_state.processed_images = []
if "expert_sign_off" not in st.session_state:
    st.session_state.expert_sign_off = False

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/medical-doctor.png", width=80)
    st.title("Nexus Medical AI")
    st.markdown("---")
    
    st.subheader("🛠 Configuration")
    hf_token = st.text_input(
        "Hugging Face Token", 
        value=os.getenv("HF_TOKEN", ""),
        type="password", 
        help="Required to access MedGemma 1.5. Can also be set in .env file."
    )
    scan_type = st.selectbox("Scan Modality", ["CT Scan", "MRI Scan", "Mammography"])
    
    use_mock = st.checkbox("Use Demo Mode (Mock AI)", value=True, help="Toggle this if you don't have a GPU or HF weights locally.")
    
    st.markdown("---")
    st.info("MedGemma 1.5-4B-IT is optimized for medical visual reasoning.")

# --- Helper Functions ---
def generate_pdf(report_text, scan_type, expert_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Clinical Analysis Report - {scan_type}", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Analysis Summary:", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, txt=report_text)
    
    pdf.ln(20)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(200, 10, txt=f"Digitally Validated By: {expert_name}", ln=True)
    
    return pdf.output(dest='S').encode('latin-1')

# --- Main App Logic ---
st.title("🩺 MedGemma Clinical Analysis")
st.write("Advance your clinical workflow with multimodal medical reasoning.")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="clinical-card">', unsafe_allow_html=True)
    st.subheader("📁 Scan Data Upload")
    
    # Accept any medical or standard image format
    supported_types = ["dcm", "nii", "nii.gz", "jpg", "jpeg", "png", "bmp", "webp", "tiff"]
    uploaded_files = st.file_uploader(
        f"Upload {scan_type} files", 
        type=supported_types, 
        accept_multiple_files=True
    )

    if uploaded_files:
        st.session_state.processed_images = []
        for f in uploaded_files:
            file_ext = f.name.lower()
            
            # 1. Handle DICOM
            if file_ext.endswith(".dcm"):
                with open("temp.dcm", "wb") as tmp:
                    tmp.write(f.read())
                hu_data, _ = MedicalImageProcessor.load_dicom_slice("temp.dcm")
                rgb_slice = MedicalImageProcessor.process_ct_rgb(hu_data)
                resized = MedicalImageProcessor.resize_for_model(rgb_slice)
                st.session_state.processed_images.append(Image.fromarray(resized))
            
            # 2. Handle NIfTI
            elif file_ext.endswith(".nii") or file_ext.endswith(".nii.gz"):
                slices = MedicalImageProcessor.extract_nifti_slices(f.read())
                st.session_state.processed_images.extend(slices)
            
            # 3. Handle Standard Image Formats
            else:
                processed_img = MedicalImageProcessor.prepare_any_image(f.read())
                if processed_img:
                    st.session_state.processed_images.append(processed_img)

        # Truncate to a reasonable amount if too many were uploaded for the model context
        st.session_state.processed_images = st.session_state.processed_images[:5]

        # Display Preview
        if len(st.session_state.processed_images) > 1:
            slice_idx = st.slider("Select Slice/Image to View", 0, len(st.session_state.processed_images)-1, 0)
            st.image(st.session_state.processed_images[slice_idx], caption=f"Selected View {slice_idx+1}", use_column_width=True)
        elif st.session_state.processed_images:
            st.image(st.session_state.processed_images[0], caption="Scan Preview", use_column_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="clinical-card">', unsafe_allow_html=True)
    st.subheader("🤖 AI Analysis Preview")
    
    analyze_btn = st.button("GENERATE CLINICAL INSIGHTS", disabled=not st.session_state.processed_images)
    
    if analyze_btn:
        with st.spinner("Analyzing scan data..."):
            if use_mock:
                handler = MedGemmaHandler()
                st.session_state.current_report = handler.mock_analyze(scan_type)
            else:
                if not hf_token:
                    st.error("Please enter a Hugging Face Token in the sidebar.")
                else:
                    handler = MedGemmaHandler()
                    handler.initialize(hf_token=hf_token)
                    st.session_state.current_report = handler.analyze(st.session_state.processed_images)
    
    if st.session_state.current_report:
        st.markdown("### Findings & Interpretation")
        edited_report = st.text_area("Edit findings as needed:", value=st.session_state.current_report, height=250)
        st.session_state.current_report = edited_report
        
        st.markdown("---")
        st.subheader("✍️ Validation & Signature")
        expert_name = st.text_input("Full Name of Reviewing Clinician")
        st.session_state.expert_sign_off = st.checkbox("Sign-off: I confirm these findings are accurate.")
        
        if st.session_state.expert_sign_off and expert_name:
            pdf_bytes = generate_pdf(st.session_state.current_report, scan_type, expert_name)
            st.download_button(
                label="📥 DOWNLOAD FINAL REPORT (PDF)",
                data=pdf_bytes,
                file_name=f"Clinical_Final_{scan_type.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("Complete the sign-off to generate the final PDF report.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("AI-assisted diagnostics should be interpreted by qualified healthcare professionals. Based on Google MedGemma 1.5.")
