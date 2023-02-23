# Importing required libraries
import streamlit as st

# Setting the page title
st.set_page_config(page_title="My Portfolio Website")

# Defining the layout
col1, col2 = st.columns(2)
with col1:
    st.image("Potrait_photo.png", use_column_width=True)
with col2:
    st.title("John Doe")
    st.subheader("Web Developer")
    st.write("""
    I am an experienced web developer with expertise in Python, Flask, Django, and React. 
    I have worked on several projects for clients from various industries, including healthcare, finance, and e-commerce. 
    In my free time, I like to contribute to open-source projects and learn new technologies. 
    """)
st.write("---")
# Adding a section for skills
st.header("Skills")
st.write("""
- Python
- Flask
- Django
- React
- HTML/CSS
- JavaScript
""")

# Adding a section for projects
st.header("Projects")
st.write("""
- [Project 1](https://github.com/project1)
- [Project 2](https://github.com/project2)
- [Project 3](https://github.com/project3)
""")

# Adding a section for contact information
st.header("Contact")
st.write("""
- Email: john.doe@email.com
- Phone: +1-123-456-7890
- LinkedIn: [https://www.linkedin.com/in/johndoe](https://www.linkedin.com/in/johndoe)
""")
