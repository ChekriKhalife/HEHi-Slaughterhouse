import streamlit as st
# Initialize session state for tracking file uploads
if 'file_uploaded_career' not in st.session_state:
    st.session_state['file_uploaded_career'] = False

if 'file_uploaded_volunteer' not in st.session_state:
    st.session_state['file_uploaded_volunteer'] = False

# Define the positions and opportunities with descriptions
careers = {
    "Environmental Compliance Officer": {
        "description": "Ensure adherence to environmental laws and regulations. Ideal candidates should have a background in environmental science or related field, with experience in regulatory compliance."
    },
    "Waste Management Specialist": {
        "description": "Oversee the processing and disposal of waste products. Responsibilities include developing waste management systems and ensuring compliance with environmental policies."
    },
    "Community Outreach Coordinator": {
        "description": "Engage with the local community and stakeholders to promote sustainability initiatives. Requires excellent communication skills and experience in public relations or community work."
    }
}

volunteering_opportunities = {
    "Urban Gardening Volunteer": {
        "description": "Assist in creating community gardens using organic waste. Volunteers will help with planting, maintenance, and community education."
    },
    "Educational Workshop Leader": {
        "description": "Conduct workshops on sustainability and waste management. Ideal for individuals with teaching experience and knowledge in environmental conservation."
    },
    "Clean-up Campaign Volunteer": {
        "description": "Participate in local clean-up campaigns to improve the environment. Suitable for those willing to work outdoors and contribute to community cleanliness."
    }
}

# Function to display application form for careers
def display_career_application_form(title, description):
    with st.form(key=f"{title}_form_career"):
        st.write(f"### Apply for {title}")
        st.write(description)
        full_name = st.text_input("Full Name", key=f"{title}_fullname_career")
        email = st.text_input("Email", key=f"{title}_email_career")
        cover_letter = st.text_area("Cover Letter", key=f"{title}_cover_letter_career")
        resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"], key=f"{title}_resume_career")
        
        # Check if a file is uploaded
        if resume is not None:
            st.session_state['file_uploaded_career'] = True
        
        submit_button = st.form_submit_button("Submit Application")
        
        if submit_button:
            if full_name and email and cover_letter and st.session_state['file_uploaded_career']:
                st.success("Application submitted successfully!")
                # Reset the file uploaded state
                st.session_state['file_uploaded_career'] = False
            else:
                st.error("Please fill in all fields and upload your resume.")

# Function to display application form for volunteering
def display_volunteer_application_form(title, description):
    with st.form(key=f"{title}_form_volunteer"):
        st.write(f"### Apply for Volunteering: {title}")
        st.write(description)
        full_name = st.text_input("Full Name", key=f"{title}_fullname_volunteer")
        email = st.text_input("Email", key=f"{title}_email_volunteer")
        why_interested = st.text_area("Why are you interested in this opportunity?", key=f"{title}_interest_volunteer")
        
        submit_button = st.form_submit_button("Submit Application")
        
        if submit_button:
            if full_name and email and why_interested:
                st.success("Application submitted successfully!")
                # Reset the file uploaded state for volunteers
                st.session_state['file_uploaded_volunteer'] = False
            else:
                st.error("Please fill in all fields.")

# Function to simulate social media content
def display_social_media_updates():
    st.header("Social Media Updates")

    # Placeholder content representing social media posts
    st.subheader("Latest Updates from Our Slaughterhouse")
    st.write("Follow us on our social media platforms to stay updated with the latest news and events.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Clean-up Campaign")
        st.image("Cleanup.jpg", caption="Join our latest clean-up campaign!", use_column_width=True)
        st.markdown("[Facebook Post Link](https://facebook.com/yourpostlink)")

    with col2:
        st.markdown("### Sustainability Workshop")
        st.image("sustainability.jpg", caption="Learn about sustainability at our workshop.", use_column_width=True)
        st.markdown("[Instagram Post Link](https://instagram.com/yourpostlink)")

    with col3:
        st.markdown("### Community Gardening")
        st.image("community gardening.jpg", caption="Get involved in community gardening!", use_column_width=True)
        st.markdown("[Twitter Post Link](https://twitter.com/yourpostlink)")

def display_blogs_and_news():
    st.header("Blogs & News")

    # Placeholder content representing blog posts and news articles
    st.subheader("Our Latest Blog Posts & News Articles")
    st.write("Keep up with the latest stories, insights, and updates from our slaughterhouse community.")

    # Example of a blog post entry
    st.markdown("#### The Impact of Sustainable Practices on Local Communities")
    st.markdown("""
    Sustainability isn’t just about the environment; it’s also about fostering a resilient community. 
    In our latest blog post, we explore how our slaughterhouse is engaging with local residents to build a greener future.
    [Read more](#link_to_your_blog_post)
    """)

    # Example of a news article entry
    st.markdown("#### Karantina Slaughterhouse: A Beacon of Progress")
    st.markdown("""
    The Karantina Slaughterhouse has been featured in a prominent news outlet for its innovative approach to waste management 
    and community development. Find out what makes our initiative stand out.
    [Read more](#link_to_your_news_article)
    """)
    
# Function to display donation options and information
def display_donation_section():
    st.header("Support Our Mission")
    st.write(
        """
        Your donations empower us to tackle key challenges in our community and environment. By contributing,
        you join our commitment to making a tangible difference in Karantina. Here's how your generosity helps:
        """
    )

    # Details about how donations have been used
    st.subheader("Your Contributions at Work")
    st.write(
        """
        **Community Development:** $25,000 helped refurbish the local community center, providing a venue for
        educational workshops and events.
        
        **Waste Management:** $40,000 invested in waste processing equipment, improving our capacity to recycle
        and manage organic waste efficiently.
        
        **Education and Training:** $15,000 funded the training of over 50 individuals in sustainable agricultural
        practices, enhancing local expertise.
        
        **Infrastructure:** $30,000 contributed to the upgrade of the slaughterhouse facilities to meet environmental
        standards and improve safety.
        """
    )

    

    # Showcasing stories of impact
    st.subheader("Stories of Impact")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Empowering Women in Agriculture")
        st.image("Empowering women in gardening.jpg", caption="Women's cooperative garden initiative", use_column_width=True)
    with col2:
        st.markdown("#### Advancing Green Energy")
        st.image("Advancing green energy.jpg", caption="Biogas plant installation", use_column_width=True)

    st.write(
        """
        Read more about how we're driving positive change and advancing our mission with the help of donors like you.
        [Impact Stories](#link_to_impact_stories)
        """
    )

    # Methods of donation
    st.subheader("Make a Donation")
    st.markdown(
        """
        Every donation, big or small, furthers our mission. You can contribute in the following ways:
        
        - **Online Portal**: Secure and convenient. [Donate Now](#link_to_online_donations).
        - **Bank Transfer**: Direct and straightforward. [Transfer Details](#link_to_bank_transfer_info).
        """
    )

    # Display bank details and mail address as hidden/expander
    with st.expander("View Bank Transfer Details"):
        st.markdown(
            """
            **Bank Name:** XYZ National Bank
            **Account Number:** 000123456789
            **Routing Number:** 011000015
            **IBAN:** LB62 0999 0000 0001 0019 0012 104
            **SWIFT/BIC:** XYZBLBBX
            """
        )
    # QR Code for quick donations
    st.subheader("Quick Donate via QR Code")
    # Set the width to a smaller size, e.g., 200 pixels
    st.image("qr2.jpg", caption="Scan to donate.", width=200)

    st.markdown(
        """
        We ensure that every dollar is accounted for and drives impact where it's needed most. If you have any
        questions about donations, or if you'd like to see more detailed financials, please [contact us](#link_to_contact).
        """
    )

# Function to display policies and regulations
def display_policies_and_regulations():
    st.header("Policies and Regulations")

    # Introduction to your policies and regulations
    st.markdown(
        """
        At the Karantina Slaughterhouse, we are committed to the highest standards of ethics and compliance. 
        Below, you'll find our key policies and regulatory frameworks that guide our operations and interactions with all stakeholders.
        """
    )

    # List your main policies
    st.subheader("Operational Policies")
    st.write(
        """
        - **Health and Safety Policy**: Outlines our commitment to ensuring the health and safety of our employees, visitors, and the animals.
        - **Environmental Policy**: Details our efforts to minimize environmental impact and outlines sustainable practices.
        - **Quality Control Policy**: Ensures that all products meet the strict quality standards set by health authorities.
        """
    )

    # If you have documents to share, you can allow users to download them
    st.subheader("Downloadable Policies")
    st.markdown("Download our detailed policy documents for more information.")
    with st.expander("Health and Safety Policy"):
        st.write("Detailed information about health and safety measures and guidelines.")
        st.download_button(label="Download Health and Safety Policy", data="Example content", file_name="Health_and_Safety_Policy.pdf")

    with st.expander("Environmental Policy"):
        st.write("Comprehensive environmental strategies and objectives.")
        st.download_button(label="Download Environmental Policy", data="Example content", file_name="Environmental_Policy.pdf")

    with st.expander("Quality Control Policy"):
        st.write("Quality control procedures and compliance measures.")
        st.download_button(label="Download Quality Control Policy", data="Example content", file_name="Quality_Control_Policy.pdf")

    # Regulations
    st.subheader("Regulatory Compliance")
    st.write(
        """
        - **Food Safety Regulations**: Adherence to national and international food safety standards.
        - **Animal Welfare Regulations**: Compliance with animal welfare laws and regulations.
        - **Waste Management Regulations**: Following best practices for waste management to protect the environment.
        """
    )

    # For regulations that require certifications, you might want to display them
    st.subheader("Certifications")
    st.image("foodsafety.jpg", caption="Our Food Safety Certification")


# Page configuration and CSS
st.set_page_config(page_title="Karantina Slaughterhouse", layout="wide", initial_sidebar_state="expanded")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf, #2e7bcf);
    color: white;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Karantina Slaughterhouse")
st.sidebar.info("Building a sustainable future for our community.")
menu = ["Careers & Volunteering", "Social Media Updates", "Blogs & News", "Policies & Regulations", "Complaints & Feedback", "Donation", "About"]
choice = st.sidebar.radio("Menu", menu)

# Main content based on navigation choice
if choice == "Careers & Volunteering":
    st.header("Careers & Volunteering")
    
    st.subheader("Available Career Positions")
    for career_title, info in careers.items():
        with st.expander(f"{career_title}"):
            st.write(info["description"])
            if st.button(f"Apply Now - {career_title}", key=f"btn_{career_title}_career"):
                display_career_application_form(career_title, info["description"])
    
    st.subheader("Volunteering Opportunities")
    for volunteer_title, info in volunteering_opportunities.items():
        with st.expander(f"{volunteer_title}"):
            st.write(info["description"])
            if st.button(f"Apply Now - {volunteer_title}", key=f"btn_{volunteer_title}_volunteer"):
                display_volunteer_application_form(volunteer_title, info["description"])

elif choice == "Social Media Updates":
    display_social_media_updates()

elif choice == "Blogs & News":
    display_blogs_and_news()

elif choice == "Policies & Regulations":
    display_policies_and_regulations()

elif choice == "Complaints & Feedback":
    st.header("We Value Your Feedback")
    feedback = st.text_area("Enter your complaint or feedback here")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
elif choice == "About":
    st.header("About Us")
    st.write("""
    The Karantina Slaughterhouse is committed to maintaining the highest standards of safety and environmental 
    sustainability. We strive to support our community by providing job opportunities, fostering social ties, and 
    adhering to strict policies and regulations to ensure a better future for all. Join us as we work towards 
    regaining the trust and confidence of the people in our community.
    """)

elif choice == "Donation":
    display_donation_section()


# Note: This is a frontend template. Backend integration is required for full functionality.
