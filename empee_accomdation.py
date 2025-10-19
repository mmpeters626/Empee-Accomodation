import streamlit as st
import os
import base64

# --- APP CONFIGURATION ---
st.set_page_config(page_title='Empee Accommodation Web App', layout="wide")

st.title('Welcome to Empee accommodation web app')

# --- SIDEBAR ---
with st.sidebar:
    st.header("Empee Accommodation")
    st.write("Welcome!!!. 👋")
    st.markdown("---")
    select_option = st.radio("Go to", ("Private Hostels off campus", "Portfolio", "About", "Contact"))
    st.markdown("---")
    st.subheader("Settings")
    st.write("Pick a theme color:")
    selected_color = st.color_picker("", "#0000FF")
    # Apply the selected color to a header
    st.markdown(f"<h1 style='color:{selected_color};'>My Title</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📫 Contact Me")
    st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [https://www.linkedin.com/in/petersmicheal/](https://www.linkedin.com/)")

# --- GLOBAL IMAGE HELPER FUNCTION ---
# Defined once globally, NOT inside the 'Hostels' section
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except FileNotFoundError:
        # st.error(f"Error: The file '{image_path}' was not found.")
        # Removed st.error here to avoid cluttering the app on every run if files are missing
        return None

# --- MAIN CONTENT BODY ---

if select_option == "Private Hostels off campus":
    st.markdown(
        """
        ## These are the hostels for both male and female available for booking with their prices.
        NOTE: the ones taken are marked as taken
        """
    )
    st.write("Male Hostels")
    st.markdown("---")

    # --- PROFILE IMAGE (Moved inside the IF block and using the global function) ---
    # The image path "My Profile Pics.jpg" must exist in the same folder as this script.
    profile_image_base64 = get_base64_image("My Profile Pics.jpg")
    if profile_image_base64:
        # Added basic CSS to make the profile image display better, e.g., circular
        st.markdown("""
            <style>
            .profile-img {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 20px;
            }
            </style>
        """, unsafe_allow_html=True)
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)
    else:
        st.error(f"Error: Profile image 'My Profile Pics.jpg' not found.")
    
    st.markdown("---")
    
    # --- FEMALE HOSTEL IMAGES SECTION ---
    st.subheader("Female Hostel Images")
    
    image_with_comments = [
        {
            "filename": "female hostel picture 2 room.jpg",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        
        {
            "filename": "female hostel picture 2 kitchen.jpg",
            "description": "Tour of the male hostel rooms."
        },
        {
            "filename": "female hostel picture 1.jpg",
            "description": "Common areas in the hostel."
        },
        {
            "filename": "female hostel picture 1.jpg",
            "description": "Hostel dining area."
        }
    ]

    # Display images
    for image_info in image_with_comments:
        filename = image_info["filename"]
        description = image_info["description"]
        if os.path.exists(filename):
            st.image(filename, width=350)
            st.markdown(f"**Description:** {description}")
            st.markdown("---")
        else:
            st.error(f"Image file '{filename}' not found for female hostels.")
            
    st.markdown("---")

    # --- MALE HOSTEL VIDEOS SECTION (INCLUDING THE CORRECTED DESCRIPTION) ---
    st.subheader("Male Hostel Videos")

    # List of videos with descriptions
    videos_with_comments = [
           
        {
            "filename": "male hostel video 1.mp4",
            "description": "**8 man room male private hostel**\n"
            "**Location:** moore road, off university road, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 530k total package per bed space for the 1st year and 450 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Close Proximity to both Unilag and Yabatech etc\n\n"
            
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 2.mp4",
            "description": "**4 man room male private hostel** available\n"
            "**Location:** Pako, Akoka, Lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for a year and 650k in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 3.mp4",
            "description": "**6 man room male private hostel** available\n"
            "**Location:** Pako, Akoka, Lagos, very close to yabatech/unilag\n"
            "**Price:** 680k total package per bed space for a year and 600k in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 4.mp4",
          "description": "**2 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 780k total package per bed space for the 1st year and 700 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

        },
        
        {
            "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"

             "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
           "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"

             "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        { 
            "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"

             "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"

            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 8.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Iwaya, akoka, Yaba, lagos, unilag\n"
            "**Price:** 600k total package per bed space for the 1st year and 500k in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Working Air conditioner\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- 1 minute walk to unilag back gate\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 9.mp4",
          "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 10.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        {
            "filename": "male hostel video 11.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 12.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 13.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 14.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 15.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 16.mp4",
           "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
        },
        
        {
            "filename": "male hostel video 17.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"

            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
             "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters using the link below to reserve your bed space in this hostel:\n"
            "https://wa.me/2348146399129"
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
            st.video(filename, format="video/mp4", start_time=0, width = 350) # Added format for robustness
            # Display the comment or description below the video
            st.markdown(f"**Description:** {description}")
            st.markdown("---")
        else:
            st.error(f"Video file '{filename}' not found.")

    # --- RESUME SECTION (Still included in Hostels option, but logically should be separate) ---
    # NOTE: The resume content is currently displayed under the 'Hostels' tab.
    # I recommend moving this content to a separate elif block for the "Portfolio" or "About" tab
    # if you want a cleaner structure. I've left it here to fix the original code errors.
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
    
    

#py -m streamlit run empee_accomdation.py