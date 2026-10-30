import streamlit as st
st.header("amit project")
# -------------------------
# Page settings
# -------------------------
st.set_page_config(
    page_title="Movie Revenue Predictor",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        color: #1f2937;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #166534;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown(
    '<div class="title">🎬חוזה הכנסות של סרטים</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">תן לי דירוג ממוצע ותקציב התחלתי של סרט ואני אחזה לך כמה הכנסות יש לו</div>',
    unsafe_allow_html=True
)

# -------------------------
# Input
# -------------------------

budget = st.number_input(
    "⭐ הכנס את התקציב ההתחלתי",
    min_value=0.0,
    max_value=99999999999999999.0,
    value=5.0,
    step=1000.0
)
votes = st.number_input(
    "⭐ הכנס את הדירוג הממוצע",
    min_value=1.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

# -------------------------
# Model
# -------------------------
w_budget = 17750549.77157962
w_votes = 2.8742058244586395

b= -109360178.61238256


prediction= budget*w_budget+votes*w_votes+b




# -------------------------
# Result
# -------------------------
if  votes< 1 or votes > 10:
    st.error("❌ הדירוג חייב להיות בין 1 ל-10")

else:
    st.success("✅ דירוג תקין")

    st.markdown(
        f"""
        <div class="result">
            💰 ההכנסות החזויות הן<br>
            {prediction:,.2f}$
        </div>
        """,
        unsafe_allow_html=True
    )
if  budget< 0 or budget > 999999999999999999999999999999999999999999999999999999999999999999:
    st.error("❌ התקציב חייב להיות בין 1 ל-999999999999999999999999999999999999999999999999999999999999999999")

else:
    st.success("✅ תקציב תקין")

        st.markdown(
            f"""
            <div class="result">
                💰 ההכנסות החזויות הן<br>
                {prediction:,.2f}$
            </div>
            """,
            unsafe_allow_html=True
        )

