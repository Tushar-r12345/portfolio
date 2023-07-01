from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic(3).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tushar Pal"
PAGE_ICON = ":wave:"
NAME = "Tushar Pal"
DESCRIPTION = """
Senior Year Computer Engineering Undergraduate | Exploring the Possibilities of Machine Learning and AI.
"""
EMAIL = "paltushar35@gmail.com"
SOCIAL_MEDIA = {
    "Leetcode": "https://leetcode.com/tushar_35/",
    "LinkedIn": "https://www.linkedin.com/in/tushar-pal-7494b5203/",
    "GitHub": "https://github.com/Tushar-r12345",
    "Twitter": "https://twitter.com/Tushar48923527",
}
PROJECTS = {
    "🏆 OptiScan: A CNN model integrated in Web app to detect eye disease": "https://youtu.be/Sb0A9i6d320",
    "🏆 Algo-Sage: A ML(rfc) model integrated in Web app to predict crops & price ratio ": "https://www.youtube.com/watch?v=v_FRRuwSJGQ",
    "🏆 Vital-Heart: A ML(rfc) integrated in Web app to predict heart disease and diagnosis": "https://www.youtube.com/watch?v=EqDTcK4uZlQ&t=14s",
    "🏆 Adyapnam: A MERN stack project providing education to underprivilige student": "https://drive.google.com/file/d/1Oce5vOQoJdb4BGHoJhhN_9JplduD4qQu/view",
}

ACHIEVEMENT = {
    "🥉 Secured 3rd place in I2C2 hackathon 2023":"https://youtu.be/Sb0A9i6d320",
    "🏅 Secured top 10 place in  Hacklipse 3.0 and won best business scope hack":"https://youtu.be/Sb0A9i6d320",
    "🏆 Max Leetcode rating is 1599 and 4-star in SQL on HackerRank":"https://youtu.be/Sb0A9i6d320",
    "🥇 Secured Global rank 2544 out of 25k participants Leetcode Weekly Contest 300":"https://youtu.be/Sb0A9i6d320",
    "🔥 Secured Global rank 4615 out of 24k participants in Leetcode Weekly Contest 298":"https://youtu.be/Sb0A9i6d320",
    "✨ Secured Global rank 5582 out of 23k participants in Leetcode Weekly Contest 297":"https://youtu.be/Sb0A9i6d320",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Student Trainee at Samsung Research and worked with On-device AI Team 
- ✔️ Final year Computer Engineering student from Delhi Technological University
- ✔️ Strong hands on experience and knowledge in Python and C++
- ✔️ Solid understanding of statistical principles and their implementation in ML/AI
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), C, C++, HTML/CSS, JavaScript, SQL 
- 📊 Framework: Tensorflow, PyTorch, Onnx, Flask, Streamlit, OpenCV
- 📚 Modeling: EDA & regression, Naive Bayes, decision trees, random forest classifiers
- 🗄️ Databases: MongoDB, MySQL
- 🧰 Tools: Github, VS Code, Pycharm, Intellij idea, Jupyter Notebook
- 🐧 OS: Windows, Linux, Ubuntu 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Student Trainee | Samsung Research Institute Banglore**")
st.write("06/2023 - Present")
st.write(
    """
- ► Working with On-Device AI department, in which i am part of SNAP (Samsung Neural Acceleration Platform) team.
- ► Accelerates and optimizes various AI processes in automated devices, while also limiting data to one's device
- ► Skills: C++, Python, Tensorflow, TfLite, Pytorch, Onnx
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Disciplinary Courses")
st.write("---")
st.write(
    """
- 🏫 Academics: Operating system, Advance database management system 
- 💻 Programming: Data structure and Algorithm, Object oriented programming
- 🌐 Network: Compiler design, Computer networks
- 🧩 Data Science: Applied mathematics, Statistics, Machine leaning, Deep learning
- 🏦 Open: CSR, Negotiation and Leadership, Supply chain management
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Achievements")
st.write("---")
for project, link in ACHIEVEMENT.items():
    st.write(f"[{project}]({link})")




