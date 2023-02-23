# Importing required libraries
import streamlit as st
from streamlit_option_menu import option_menu


# Setting the page title
st.set_page_config(page_title="My Portfolio Website")

# navbar -----------------------------------------------------------------------------

# as sidebar menu


selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Skills", "Projects", "Contact"],
    icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],
    default_index=3,
    orientation="horizontal",
)
if selected == "Home":
    st.write("Home")
    st.html(
        """
        <script>
        window.scrollTo({top: 0, behavior: 'smooth'});
        </script>
        """
    )
if selected == "About":
    st.write("About")

if selected == "Skills":
    st.write("skills")

if selected == "Projects":
    st.write("Projects")

if selected == "Contact":
    st.write("Contact")



# isi page -----------------------------------------------------------------------------

# Defining the layout
col1, col2 = st.columns(2)
with col1:
    st.image("Potrait_photo.png", use_column_width=True)
with col2:
    st.title("Stefanus Adri Irawan")
    st.subheader("Data Analyst")
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

if st.button("Move to top"):
    st.components.v1.html(
        """
        <script>
        console.log("Hello, JavaScript!");
        </script>
        """
        ,scrolling=True
    )

