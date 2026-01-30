import streamlit as st
import base64
from PIL import Image

st.set_page_config(
    page_title="International School on Statistical Inference from Biological Data",
    page_icon="🧬",
    layout="wide",
)

try:
    header_image = Image.open("assets/images/banner_escuela_simbad.png")  # reemplaza con tu archivo

    # Mostrar la imagen a ancho completo
    st.image(header_image, use_column_width=True)
except Exception:
    st.title("🧬 International School on Statistical Inference from Biological Data")
    










st.markdown(
    """
    
    📅 **Dates:** February 2-13, 2026  
    📍 **Location:** Physics Faculty, Havana University, Havana, Cuba \\
    🔗 **Webpage:** You can visit the official school page [here](https://indico.ictp.it/event/11113).
    
    
    Use the sidebar to navigate through the sections.

    DESCRIPTION:
    The last two decades have witnessed giant experimental breakthroughs in
    different areas of the life sciences, from genomics to epidemiology. Thanks
    to modern high-throughput techniques, biological systems across multiple
    scales -from single molecules up to entire populations- can now be probed
    quantitatively at high spatial and temporal resolutions.These data potentially
    encode a plethora of information about the functional constraints that
    govern its evolution and the physical constraints that limit its performance.
    Extracting this information is also crucial for applications ranging from the
    design of proteins with a desired functionality to the reconstruction of
    contacts during epidemics. Inverse statistical mechanics attempts to do it
    by inferring generative models from data using methods from the physics
    of disordered and random systems but more recently also exploring AI
    approaches. Specific characteristics of biological data however, like strong
    undersampling and heterogeneity, limit the effectiveness of these tools.
    The school will explore the opportunities and limits of statistical inference
    across biological systems and applications.

    DIRECTORS:
    - Andrea De Martino, Politecnico di Torino, Italy
    - Jacopo Grilli, ICTP, Italy
    - Roberto Mulet, University of Havana, Cuba
    """
)
def load_css(path: str):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/styles/custom.css")

# Cargar imágenes de los logos
logo1 = Image.open("assets/images/scf.jpg")
logo2 = Image.open("assets/images/image.png")
logo3 = Image.open("assets/images/Logo CSC.jpg")
logo4 = Image.open("assets/images/UH.jpg")
logo5 = Image.open("assets/images/ff.png")
logo6 = Image.open("assets/images/ictp.jpg")

# Crear columnas según cantidad de logos
cols = st.columns(6)  # 6 logos, una columna por logo
# Mostrar cada logo en su columna
cols[0].image(logo6, width=90)
cols[1].image(logo3, width=120)
cols[2].image(logo2, width=90)
cols[3].image(logo4, width=90)
cols[4].image(logo5, width=120)
cols[5].image(logo1, width=90)


pdf_path = "assets/posters/winter_school_poster.pdf"

def display_pdf(path: str, width: int = 700, height: int = 900):
    """
    Embed a PDF file in the Streamlit app.

    Parameters
    ----------
    path : str
        Path to the PDF file.
    width : int
        Width of the embedded viewer.
    height : int
        Height of the embedded viewer.
    """
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="{width}"
            height="{height}"
            type="application/pdf">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)


st.download_button(
    label="📄 Download poster (PDF)",
    data=open(pdf_path, "rb"),
    file_name="Winter_School_2026_Poster.pdf",
    mime="application/pdf",
)

with st.expander("📋 View Poster (click to expand)"):
    display_pdf(pdf_path)