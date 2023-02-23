# Importing required libraries
import streamlit as st
#from streamlit_option_menu import option_menu


# Setting the page title
st.set_page_config(page_title="My Portfolio Website")

#options=["Home", "About", "Skills", "Projects", "Contact"],
        #icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],

# navbar -----------------------------------------------------------------------------

# as sidebar menu
st.markdown(
    """
    <style>
    
    /* For mobile phones: */
    [class*="col-"] {
        width: 100%;
    }
    
    /* For tablets and up: */
    @media only screen and (min-width: 768px) {
        /* Three equal columns */
        .col-3 {
            float: left;
            width: 33.33%;
        }
    }
        
    body {
        margin: 0;
        padding: 0;
        font-family: sans-serif;
    }
    
    header {
        background-color: #f2f2f2;
        padding: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    
    .logo a {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        text-decoration: none;
    }
    
    ul {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    li {
        margin: 0 10px;
    }
    
    a {
        color: #333;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Media queries for responsive design */
    @media only screen and (max-width: 600px) {
        .logo a {
            font-size: 16px;
        }
        li {
            margin: 0 5px;
        }
    }
    </style>
    
    


<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Minimalist Navbar</title>
	<link rel="stylesheet" type="text/css" href="navbar.css">
</head>
<body>
	<header>
		<nav>
			<div class="logo"><a href="#">My Website</a></div>
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="#">About</a></li>
				<li><a href="#">Services</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
		</nav>
	</header>
	<br>
	
</body>
</html>

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
- LinkedIn: 
""")
