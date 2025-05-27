import streamlit as st

# Page configuration
st.set_page_config(page_title="Jyothi Surla -  Portfolio", layout="wide")

# Title and introduction
st.title("Jyothi Surla")
st.subheader("AI Master's Student | Python Developer | Machine Learning Engineer")

# Profile Summary
st.markdown("""
## Profile Summary
I'm a Master's student in Artificial Intelligence at BTU Cottbus-Senftenberg with industry experience from Genpact and TCS. 
My background includes Python-based automation tools, machine learning pipelines, and computer vision systems.
I'm currently seeking working student and internship opportunities along with thesis in AI, machine learning, or software development roles.
""")

# Skills section
st.markdown("## Skills")

st.write("""
- **Languages:** Python, Bash, SQL, HTML, CSS, JavaScript  
- **Libraries & Frameworks:** TensorFlow, PyTorch, Scikit-learn, OpenCV, Pandas, YOLO, Matplotlib  
- **Tools:** Git, Docker, Azure, Linux, JSON  
""")

# Projects section
st.markdown("## Projects")

st.markdown("""**Smart Research Assistant**  
A Streamlit-based web app that searches for a topic, retrieves recent articles, summarises them using Hugging Face models, and generates a downloadable PDF.  
[Live App](https://jyothi-surla-smart-research-assistant.streamlit.app)  
Technologies: Python, Streamlit, Hugging Face Transformers, FPDF, DuckDuckGo Search""")

st.markdown("""**Image Quality Checker**  
A lightweight tool that detects blur and exposure issues in images using OpenCV, designed for sensor-data pipelines in autonomous systems.  
Technologies: Python, OpenCV, JSON""")

st.markdown("""**Health Risk Prediction with Explainable AI**  
A model trained to predict patient risk categories from clinical indicators, with SHAP-based explainability for transparent decision-making.  
Technologies: Python, Scikit-learn, SHAP, Pandas, Matplotlib""")

# Contact section
st.markdown("## Contact")

st.write("""
- Location: Berlin, Germany  
- Email: jyothisurlaai@gmail.com  
- Phone: +49 15510671172  
- GitHub: [github.com/Jyothi-Surla](https://github.com/Jyothi-Surla)
""")
