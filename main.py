# Importing required libraries
import streamlit as st
#from streamlit_option_menu import option_menu


# Setting the page title
st.set_page_config(page_title="My Portfolio Website")

#options=["Home", "About", "Skills", "Projects", "Contact"],
        #icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],

# navbar -----------------------------------------------------------------------------

# as sidebar menu

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


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

