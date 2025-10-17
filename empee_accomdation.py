import streamlit as st
import os

st.set_page_config(page_title='Empee Accommodation Web App', layout="wide")

st.title('Welcome to Empee accommodation web app')

# Sidebar
with st.sidebar:
    st.header("Empee Accommodation")
    st.write("Welcome!!!. 👋")
    st.markdown("---")
    select_option = st.radio("Go to", ("Hostels", "Portfolio", "About", "Contact"))
    st.markdown("---")
    st.subheader("Settings")
    st.write("Pick a theme color:")
    selected_color = st.color_picker("", "#0000FF")
    # Apply the selected color to a header
    st.markdown(f"<h1 style='color:{selected_color};'>My Title</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📫 Contact Me")
    st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [https://www.linkedin.com/in/petersmicheal/](https://www.linkedin.com/)")

if select_option == "Hostels":
    st.markdown(
        """
        ## These are the hostels for both male and female available for booking with their prices.
        NOTE: the ones taken are marked as taken
        """
    )

    st.write("Male Hostels")

    # Display profile image
    def get_base64_image(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except FileNotFoundError:
            st.error(f"Error: The image file '{image_path}' was not found. Please make sure it's in the same directory.")
            return None

    profile_image_base64 = get_base64_image("My Profile Pics.jpg")
    if profile_image_base64:
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)

    st.markdown("---")

 


    # Function to load and encode image to base64
    def get_base64_image(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except FileNotFoundError:
            st.error(f"Error: The image file '{image_path}' was not found. Please ensure it is in the correct directory.")
            return None

    # Display profile image
    profile_image_base64 = get_base64_image("My Profile Pics.jpg")
    if profile_image_base64:
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)

    st.markdown("---")

    # List of videos with descriptions
    videos_with_comments = [
        {
            "filename": "This hostel is.mp4",
            "description": "This is an overview of the hostel facilities."
        },
        {
            "filename": "male hostel video 1.mp4",
            "description": "Tour of the male hostel rooms."
        },
        {
            "filename": "male hostel video 3.mp4",
            "description": "Common areas in the hostel."
        },
        {
            "filename": "male hostel video 4.mp4",
            "description": "Hostel dining area."
        },
        {
            "filename": "male hostel video 5.mp4",
            "description": "View of the hostel's recreational facilities."
        },
        {
            "filename": "male hostel video 6.mp4",
            "description": "Hostel security and safety features."
        },
        {
            "filename": "male hostel video 7.mp4",
            "description": "Student testimonials and reviews."
        },
        {
            "filename": "male hostel video 8.mp4",
            "description": "Night view of the hostel premises."
        },
        {
            "filename": "male hostel video 9.mp4",
            "description": "Hostel entrance and reception area."
        },
        
        {
            "filename": "male hostel video 10.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 11.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 12.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 13.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 14.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 15.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 16.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 17.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 18.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 19.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 20.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 21.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 22.mp4",
            "description": "Additional view of hostel facilities."
        },
        {
            "filename": "male hostel video 23.mp4",
            "description": "Additional view of hostel facilities."
        },
        
    ]

    # Loop through each video and display with comment
    for video_info in videos_with_comments:
        filename = video_info["filename"]
        description = video_info["description"]
        if os.path.exists(filename):
            st.video(filename, width=350)
            # Display the comment or description below the video
            st.markdown(f"**Description:** {description}")
            st.markdown("---")
        else:
            st.error(f"Video file '{filename}' not found.")

    # Resume section
    st.title("My Resume")
    st.markdown("### MICHEAL PETERS")
    st.markdown(
        """
        - Address: 3, Lalubu Street, Okeilewo, Abeokuta, Ogun State, Abeokuta North, Ogun State
        - Phone: 08146399129
        - Email: mmpeters626@gmail.com
        - LinkedIn: https://www.linkedin.com/in/petersmicheal/
        """
    )
    st.markdown("---")
    st.markdown("### OBJECTIVE")
    st.markdown(
        """
        Enthusiastic and detail-oriented aspiring Data Scientist with a strong foundation 
        in statistical analysis, machine learning, and data visualization. Eager to apply 
        academic knowledge and technical skills to real-world projects through an internship, 
        aiming to contribute to data-driven decision-making and gain practical industry experience.
        """
    )
    st.markdown("---")
    st.markdown("### SKILLS")
    st.markdown(
        """
        - Programming: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
        - Data Analysis & Visualization
        - Machine Learning Algorithms: Linear Regression, Logistic Regression, Decision Trees, Random Forest
        - SQL & Databases
        - Basic Knowledge of Big Data Tools (Spark, Hadoop)
        - Statistical Analysis & Hypothesis Testing
        """
    )
    st.markdown("---")
    st.markdown("### EDUCATION")
    st.markdown(
        """
        **Bachelor of Science in Education (BSc.Ed) in Technology Education (in view)**
        University of Yaba, Lagos
        *Expected Graduation: August 2026*
        *Relevant Coursework: Data Structures, Statistics, Machine Learning, Data Visualization, Databases*
        """
    )
    st.markdown("---")
    st.markdown("### PROJECTS")
    st.markdown(
        """
        **Customer Churn Prediction**
        - Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy.
        - Performed data cleaning, feature engineering, and model evaluation.

        **Employee Salary Prediction**

        **Sentiment Analysis of Social Media Data**
        - Analyzed Twitter data to classify sentiment using NLP techniques and Python libraries.
        - Visualized sentiment trends over time.

        **Sales Data Visualization Dashboard**
        - Created an interactive sales performance dashboard in Tableau to explore regional sales metrics.
        """
    )
    st.markdown("---")
    st.markdown("### CERTIFICATIONS AND COURSES")
    st.markdown(
        """
        - Introduction to Data Science in Python – Coursera, University of Michigan
        - Machine Learning – Coursera, Stanford University
        - Data Analysis with Python – freeCodeCamp
        """
    )
    st.markdown("---")
    st.markdown("### EXTRACURRICULAR ACTIVITIES")
    st.markdown(
        """
        - Member of [University Data Science Club]
        - Participated in Kaggle competitions (if applicable)
        - Volunteered for data analysis projects at [Organization Name]
        """
    )
    st.markdown("---")
    st.markdown("### LANGUAGES")
    st.markdown("- English (Fluent)")
    st.markdown("---")

elif select_option == "Portfolio":
    st.title("My Portfolio")
    st.markdown(
        """
        Welcome to my portfolio! Here you will find some of my key projects and work. 
        Each project showcases my skills in data science, machine learning, and data visualization.
        """
    )

    st.subheader("Project Showcase")
    st.markdown("#### Customer Churn Prediction App")
    st.write("- Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy \n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    st.markdown("#### Car Prices Prediction App")
    st.write("- Developed a Regression model to predict car prices using Python and Scikit-learn, achieving 81% accuracy \n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    st.markdown("#### Student performance Prediction")
    st.write("- Developed a classification model to predict students performances using Python and Scikit-learn, achieving 85% accuracy \n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    st.markdown("#### Diabetes Prediction")
    st.write("- Developed a classification model to predict the tendency of an individual to have diabetes due to some informations \n"
             "supplied by the individual as requested using Python and Scikit-learn, achieving 85% accuracy \n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    st.markdown("#### Weather App")
    st.write("- Built a Python application using Streamlit to provide real-time weather information for any location worldwide, here is the link to check out the app\n"
             "[https://whether-app-mop.streamlit.app](https://whether-app-mop.streamlit.app)")
    st.markdown("---")

elif select_option == "About":
    st.title("About Me")
    st.markdown("### Hello!!, This a brief overview about me")
    st.markdown(
        """
        I am a passionate and driven aspiring data scientist with a knack for solving problems
        and uncovering insights from data. I am currently pursuing my Bachelor of Science in 
        Education (BSc.Ed) in Technology Education at the University of Yaba, Lagos. 
        My goal is to leverage my skills in data science and machine learning to contribute
        to meaningful, data-driven solutions.
        """
    )
    st.markdown("---")
   
    st.markdown("- Studying")
    st.markdown("- Making Researches")
    st.markdown("- Praying")

elif select_option == "Contact":
    st.title("Contact")
    st.markdown("feel free to connect with me via.")
    st.markdown(
        """
        - **Email:** mmpeters626@gmail.com
        - **Phone:** 08146399129 0r 08112398005
        - **LinkedIn:** https://www.linkedin.com/in/petersmicheal/
        """
    )
    st.markdown("---")
    st.markdown(r"""
                **_Built Using Python and Streamlit_**
                """)
    st.markdown("### _Micheal Peters_")
    st.markdown("---")
    
    
    
   # py -m streamlit run empee_accomdation.py