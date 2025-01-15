import streamlit as st

def welcome_page():
    # Check if the user is logged in and is a regular user
    if "user" in st.session_state and st.session_state["user"]["role"] == "user":
            # Display welcome messages
            st.subheader("🔅〽️ Welcome")
            st.subheader("Managing your Income and Expenses")
            st.markdown("---")

    # Example function to simulate fetching user income data
    def get_user_income(user_id):
        # Simulated data fetching logic (replace this with actual database or API logic)
        return f"Simulated income data for user {user_id}"

    rtl_css = """
    <style>
    .rtl {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Optional: Specify a font that supports Arabic */
        font-size: 20px; /* Adjust as needed */
    }
    </style>
    """
    # Inject the CSS
    st.markdown(rtl_css, unsafe_allow_html=True)


    # Arabic text content
    arabic_text = """
    <p class="rtl">
     يمكن اسستخدام هذا النموذج لادارة مينزاتيك بفعالية عن طريق إضافة المصروفات الشهرية 
    وتحديد كيقية انفاق أموالك بشكل يتناسب مع احتياجاتك المالية ابدأ بإدخال اجمالي دخلك الشهري
    لكل شهر من السنة تم قم بتحديد المصروفات الشهرية في نموذج المصروفات لكل فئة من الفئات
    التي تتناسب بما يتناسب مع متطلباتك واحتياجاك المالي مكن إضافة مذخراتك كل شهر عن 
    </p>
    """   

    # Adding custom CSS for text justification
    eng_css = """
    <style>
    .justify {
        text-align: justify;
    }
    </style>
    """

    # Inject the CSS
    st.markdown(eng_css, unsafe_allow_html=True)

    # Write a justified paragraph
    eng_text = """
    <p class="justify">
    You can personalize this simple budget by changing any labels and deciding where you want your money to go. 
    Start by inserting your total income and all expenses. 
    Then play around with the template until you are satisfied. It is working well for you with a unique financial need. 
    You can create a new entry every month by inserting the income and expenses every day  
    </p>
    """

    # Render the justified paragraph
    st.markdown(eng_text, unsafe_allow_html=True)

 # Render the Arabic text
    st.markdown(arabic_text, unsafe_allow_html=True)
     # Render the Arabic text


   
   # Dividing paragraphs
    st.write("---")  # Add a horizontal divider   
        
# Custom CSS for Arabic text alignment to the right
    rtl_css = """
    <style>
    .rtl-section {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Specify a font that supports Arabic */
        font-size: 14px; /* Adjust font size */
        margin-right: 10px; /* Optional: Add space from the right edge */
        line-height: 1.8; /* Adjust line spacing */
    }
    </style>
    """

    # Inject the CSS
    st.markdown(rtl_css, unsafe_allow_html=True)

    # Render the Arabic content with proper line breaks
    st.markdown(
        """
        <div class="rtl-section">
            <h5>Saving Section (المذخرات)</h5>
            <p> %25 = التوفير الأول </p>
            <p> %30 = صندوق الطواري</p>
            <p> %20 = خطة الديون</p>
            <p> %25 = التوفير الثانية</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("---")  # Add a horizontal divider
    st.write("👈:orange[©2024 copyright By Arefco, Contact: Email:arefco@gmail.com]" )