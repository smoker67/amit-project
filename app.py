import random
import streamlit as st

st.title("🎮 נצח את המודל!")

# מקדמי המודל
W_BUDGET = 17750549.77157962
W_VOTES = 2.8742058244586395
B = -109360178.61238256

# 20 הסרטים מהדאטה שלך (תקציב, דירוג, הכנסות אמת)
DATASET = [
    {"votes": 7.2, "budget": 237000000, "actual": 2787965087},
    {"votes": 6.9, "budget": 300000000, "actual": 961000000},
    {"votes": 6.3, "budget": 245000000, "actual": 880674609},
    {"votes": 7.6, "budget": 250000000, "actual": 1084939099},
    {"votes": 6.1, "budget": 260000000, "actual": 284139100},
    {"votes": 5.9, "budget": 258000000, "actual": 890871626},
    {"votes": 7.4, "budget": 260000000, "actual": 591794936},
    {"votes": 7.3, "budget": 280000000, "actual": 1405403694},
    {"votes": 7.4, "budget": 250000000, "actual": 933959197},
    {"votes": 5.7, "budget": 250000000, "actual": 873260194},
    {"votes": 5.4, "budget": 270000000, "actual": 391081192},
    {"votes": 6.1, "budget": 200000000, "actual": 586090727},
    {"votes": 7.0, "budget": 200000000, "actual": 1065659812},
    {"votes": 5.9, "budget": 255000000, "actual": 89289910},
    {"votes": 6.5, "budget": 225000000, "actual": 662845518},
    {"votes": 6.3, "budget": 225000000, "actual": 419651413},
    {"votes": 7.4, "budget": 220000000, "actual": 1519557910},
    {"votes": 6.4, "budget": 380000000, "actual": 1045713802},
    {"votes": 6.2, "budget": 225000000, "actual": 624026776},
    {"votes": 7.1, "budget": 250000000, "actual": 956019788},
]

# בחירת סרט אקראי מתוך הרשימה
if "movie_idx" not in st.session_state:
    st.session_state.movie_idx = random.randint(0, len(DATASET) - 1)

if st.button("🎲 בחר סרט חדש"):
    st.session_state.movie_idx = random.randint(0, len(DATASET) - 1)

current_movie = DATASET[st.session_state.movie_idx]

# הצגת נתוני הסרט
st.write(f"**תקציב הסרט:** ${current_movie['budget']:,}")
st.write(f"**דירוג הצופים:** {current_movie['votes']} / 10")

# ניחוש השחקן
player_guess = st.number_input(
    "מה לדעתך היו ההכנסות האמיתיות של הסרט ($)?",
    min_value=0.0,
    step=10000000.0,
)

if st.button("בדוק מי ניצח"):
    actual = current_movie["actual"]
    model_pred = (
        current_movie["budget"] * W_BUDGET + current_movie["votes"] * W_VOTES + B
    )

    player_error = abs(player_guess - actual)
    model_error = abs(model_pred - actual)

    st.write("---")
    st.write(f"**הכנסות אמת:** ${actual:,.2f}")
    st.write(f"**תחזית המודל:** ${model_pred:,.2f}")
    st.write(f"**הניחוש שלך:** ${player_guess:,.2f}")

    if player_error < model_error:
        st.success("🎉 ניצחת! היית קרוב יותר מהמודל.")
    elif model_error < player_error:
        st.error("🤖 המודל ניצח! התחזית שלו הייתה מדויקת יותר.")
    else:
        st.info("🤝 תיקו!")
# import streamlit as st

# budget = st.number_input("הכנס תקציב לסרט(מספר חיובי)")
# votes = st.number_input("הכנס דירוג ממוצע לסרט בין 1-10")


# # -------------------------
# # Model
# # -------------------------
# w_budget = 17750549.77157962
# w_votes = 2.8742058244586395
# b = -109360178.61238256

# prediction = budget*w_budget+votes*w_votes+b
# st.write("ההכנסות החזויות של הסרט הן:", prediction, "$")

# # MAX_BUDGET = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# # # -------------------------
# # # Custom CSS
# # # -------------------------
# # st.markdown("""
# # <style>
# #     .main {
# #         background-color: #f5f7fb;
# #     }

# #     .title {
# #         text-align: center;
# #         color: #1f2937;
# #         font-size: 42px;
# #         font-weight: bold;
# #         margin-bottom: 10px;
# #     }

# #     .subtitle {
# #         text-align: center;
# #         color: #6b7280;
# #         font-size: 18px;
# #         margin-bottom: 30px;
# #     }

# #     .result {
# #         background-color: #e8f5e9;
# #         padding: 20px;
# #         border-radius: 12px;
# #         text-align: center;
# #         font-size: 24px;
# #         font-weight: bold;
# #         color: #166534;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # -------------------------
# # # Navigation
# # # -------------------------
# # st.sidebar.title("🎬 Movie Project")

# # page = st.sidebar.radio(
# #     "בחר עמוד:",
# #     ["חיזוי הכנסות", "🎮 נצח את המודל"]
# # )

# # # =================================================
# # # PAGE 1 - PREDICTOR
# # # =================================================

# # if page == "חיזוי הכנסות":

# #     st.markdown(
# #         '<div class="title">🎬 חוזה הכנסות של סרטים</div>',
# #         unsafe_allow_html=True
# #     )

# #     st.markdown(
# #         '<div class="subtitle">תן לי דירוג ממוצע ותקציב התחלתי של סרט ואני אחזה לך כמה הכנסות יש לו</div>',
# #         unsafe_allow_html=True
# #     )

# #     # Input

# #     budget_text = st.text_input(
# #         "💰 הכנס את התקציב ההתחלתי",
# #         value="50000000"
# #     )

# #     votes = st.number_input(
# #         "⭐ הכנס את הדירוג הממוצע",
# #         min_value=1.0,
# #         max_value=10.0,
# #         value=5.0,
# #         step=0.1
# #     )

# #     # Validation

# #     try:
# #         budget = int(budget_text)
# #         budget_valid = 1 <= budget <= MAX_BUDGET
# #     except ValueError:
# #         budget = 0
# #         budget_valid = False

# #     # Prediction

# #     if not budget_valid:

# #         st.error("❌ התקציב חייב להיות מספר שלם בין 1 למקסימום שהוגדר")

# #     else:

# #         prediction = budget * w_budget + votes * w_votes + b

# #         st.success("✅ הנתונים תקינים")

# #         st.markdown(
# #             f"""
# #             <div class="result">
# #                 💰 ההכנסות החזויות הן<br>
# #                 {prediction:,.2f}$
# #             </div>
# #             """,
# #             unsafe_allow_html=True
# #         )

# # # =================================================
# # # PAGE 2 - BEAT THE MODEL GAME
# # # =================================================

# # elif page == "🎮 נצח את המודל":

# #     st.markdown(
# #         '<div class="title">🏆 Beat the Model</div>',
# #         unsafe_allow_html=True
# #     )

# #     st.markdown(
# #         '<div class="subtitle">האם אתה יכול לנצח את הבינה המלאכותית?</div>',
# #         unsafe_allow_html=True
# #     )

# #     st.write(
# #         "במשחק הזה אתה והמודל מנסים לחזות את ההכנסות של סרט."
# #     )

# #     st.divider()

# #     # Movie data

# #     st.subheader("🎬 נתוני הסרט")

# #     game_budget_text = st.text_input(
# #         "💰 תקציב הסרט בדולרים",
# #         value="50000000",
# #         key="game_budget"
# #     )

# #     game_votes = st.number_input(
# #         "⭐ דירוג הסרט",
# #         min_value=1.0,
# #         max_value=10.0,
# #         value=8.0,
# #         step=0.1,
# #         key="game_votes"
# #     )

# #     try:
# #         game_budget = int(game_budget_text)
# #         game_budget_valid = 1 <= game_budget <= MAX_BUDGET
# #     except ValueError:
# #         game_budget = 0
# #         game_budget_valid = False

# #     st.divider()

# #     # User guess

# #     st.subheader("🤔 מה לדעתך יהיו ההכנסות?")

# #     user_guess_text = st.text_input(
# #         "הכנס את הניחוש שלך בדולרים (אפשר גם מספר שלילי)",
# #         value="100000000",
# #         key="user_guess"
# #     )

# #     # Real revenue

# #     st.subheader("📊 מה היו ההכנסות האמיתיות?")

# #     real_revenue_text = st.text_input(
# #         "הכנס את ההכנסות האמיתיות של הסרט בדולרים",
# #         value="120000000",
# #         key="real_revenue"
# #     )

# #     # Check button

# #     if st.button("🏆 בדוק מי ניצח!", use_container_width=True):

# #         try:

# #             user_guess = int(user_guess_text)
# #             real_revenue = int(real_revenue_text)

# #             if not game_budget_valid:

# #                 st.error("❌ התקציב חייב להיות מספר שלם וחיובי בטווח המותר")

# #             elif real_revenue < 0:

# #                 st.error("❌ ההכנסות האמיתיות לא יכולות להיות שליליות")

# #             else:

# #                 # Model prediction

# #                 model_prediction = (
# #                     game_budget * w_budget
# #                     + game_votes * w_votes
# #                     + b
# #                 )

# #                 # Calculate errors

# #                 user_error = abs(user_guess - real_revenue)

# #                 model_error = abs(
# #                     model_prediction - real_revenue
# #                 )

# #                 st.divider()

# #                 st.subheader("📈 תוצאות המשחק")

# #                 col1, col2 = st.columns(2)

# #                 with col1:

# #                     st.metric(
# #                         "הניחוש שלך",
# #                         f"${user_guess:,.2f}",
# #                         f"טעות: ${user_error:,.2f}"
# #                     )

# #                 with col2:

# #                     st.metric(
# #                         "תחזית המודל",
# #                         f"${model_prediction:,.2f}",
# #                         f"טעות: ${model_error:,.2f}"
# #                     )

# #                 st.write(
# #                     f"**ההכנסות האמיתיות:** ${real_revenue:,.2f}"
# #                 )

# #                 st.divider()

# #                 # Winner

# #                 if user_error < model_error:

# #                     st.balloons()

# #                     st.success(
# #                         "🎉 ניצחת את המודל! אתה היית קרוב יותר!"
# #                     )

# #                 elif model_error < user_error:

# #                     st.error(
# #                         "🤖 המודל ניצח! התחזית שלו הייתה קרובה יותר."
# #                     )

# #                 else:

# #                     st.info(
# #                         "🤝 תיקו! אתה והמודל הייתם באותו מרחק מהתוצאה האמיתית."
# #                     )

# #         except ValueError:

# #             st.error(
# #                 "❌ יש להזין מספרים שלמים ותקינים בכל השדות"
# #             )
