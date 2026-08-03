import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Cricket AI Agent",
    page_icon="🏏",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/runs"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', sans-serif !important; }

/* ── Background ── */
.stApp { background: #0a0e0a; }

.block-container {
    background: transparent !important;
    padding: 2rem 2.5rem !important;
}

/* ── Title ── */
h1 {
    background: linear-gradient(90deg, #22c55e, #86efac, #fbbf24);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-size: 2.6rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.5px;
}

h2, h3 {
    color: #e2e8f0 !important;
    -webkit-text-fill-color: #e2e8f0 !important;
    font-weight: 700 !important;
}

p, label, span, div { color: #94a3b8 !important; }

/* ── Search bar ── */
div[data-baseweb="input"] {
    background: #0f1a0f !important;
    border: 1.5px solid #166534 !important;
    border-radius: 12px !important;
    transition: all 0.2s ease !important;
}
div[data-baseweb="input"]:focus-within {
    border-color: #22c55e !important;
    box-shadow: 0 0 0 3px rgba(34,197,94,0.15) !important;
}
div[data-baseweb="input"] input {
    background: transparent !important;
    color: #f1f5f9 !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
}
div[data-baseweb="input"] input::placeholder { color: #374151 !important; }

/* ── Search Button ── */
.stButton > button {
    background: linear-gradient(135deg, #16a34a, #22c55e) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.65rem 2rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 4px 16px rgba(34,197,94,0.35) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.03) !important;
    box-shadow: 0 8px 24px rgba(34,197,94,0.5) !important;
}
.stButton > button:active { transform: scale(0.97) !important; }

/* ── Metric cards ── */
div[data-testid="stMetric"] {
    background: #0f1a0f !important;
    border: 1px solid #166534 !important;
    border-radius: 14px !important;
    padding: 16px 14px !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    transition: all 0.25s ease !important;
}
div[data-testid="stMetric"]:hover {
    border-color: #22c55e !important;
    box-shadow: 0 0 20px rgba(34,197,94,0.2) !important;
    transform: translateY(-3px) !important;
}
div[data-testid="stMetricValue"] {
    color: #22c55e !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}
div[data-testid="stMetricLabel"] {
    color: #86efac !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.5px;
}

/* ── Tabs ── */
button[data-baseweb="tab"] {
    background: #0f1a0f !important;
    color: #4b5563 !important;
    border-radius: 10px 10px 0 0 !important;
    border: 1px solid #166534 !important;
    border-bottom: none !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
}
button[data-baseweb="tab"]:hover { color: #22c55e !important; }
button[data-baseweb="tab"][aria-selected="true"] {
    background: #166534 !important;
    color: #86efac !important;
    border-color: #22c55e !important;
}

/* ── Tab panel ── */
div[data-testid="stTabPanel"] {
    background: #0a0e0a !important;
    border: 1px solid #166534 !important;
    border-radius: 0 12px 12px 12px !important;
    padding: 1.5rem !important;
}

/* ── Dataframe ── */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #166534;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}

/* ── Expander ── */
details {
    background: #0f1a0f !important;
    border: 1px solid #166534 !important;
    border-radius: 12px !important;
}
details summary {
    color: #86efac !important;
    font-weight: 600 !important;
    padding: 0.8rem 1rem !important;
}

/* ── Info/success/warning boxes ── */
div[data-testid="stAlert"] { border-radius: 12px !important; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #060a06 !important;
    border-right: 1px solid #166534 !important;
}
section[data-testid="stSidebar"] * { color: #86efac !important; }

/* ── Divider ── */
hr { border-color: #166534 !important; }

/* ── Spinner ── */
div[data-testid="stSpinner"] p { color: #22c55e !important; }
</style>
""", unsafe_allow_html=True)


# ── Header ──
st.markdown("""
<div style='text-align:center;padding:1rem 0 0.5rem;'>
    <div style='font-size:3rem;margin-bottom:6px;'>🏏</div>
    <h1 style='background:linear-gradient(90deg,#22c55e,#86efac,#fbbf24);
               -webkit-background-clip:text;-webkit-text-fill-color:transparent;
               font-size:2.4rem;font-weight:900;margin:0;'>
        Cricket AI Agent
    </h1>
    <p style='color:#4b5563;font-size:0.9rem;margin-top:6px;'>
        Search any international cricketer's career statistics
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Search ──
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    player = st.text_input(
        "Player Name",
        placeholder="e.g. Virat Kohli, Rohit Sharma, MS Dhoni...",
        label_visibility="collapsed"
    )
    search = st.button("🔍 Search Player", use_container_width=True)

st.divider()

# ── Main logic ──
if search:
    if player.strip() == "":
        st.warning("⚠️ Please enter a player name to search.")
        st.stop()

    with st.spinner(f"Fetching stats for **{player}**..."):
        response = requests.post(API_URL, json={"name": player})

    if response.status_code != 200:
        st.error(f"❌ API Error: {response.text}")
        st.stop()

    data = response.json()

    # ── Player name banner ──
    st.markdown(f"""
    <div style='text-align:center;padding:1.5rem;
                background:linear-gradient(135deg,#0f1a0f,#14532d);
                border:1px solid #22c55e;border-radius:18px;
                margin-bottom:1.5rem;
                box-shadow:0 0 32px rgba(34,197,94,0.15);'>
        <div style='font-size:2rem;font-weight:900;
                    background:linear-gradient(90deg,#22c55e,#86efac);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
            🏏 {data["Name"]}
        </div>
        <div style='font-size:0.85rem;color:#4b5563;margin-top:4px;'>
            International Cricket Career Statistics
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats function ──
    def show_stats(title, stats, color):
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,#0a0e0a,#0f1a0f);
                    border-left:3px solid {color};border-radius:0 12px 12px 0;
                    padding:10px 16px;margin-bottom:1rem;'>
            <span style='font-size:1rem;font-weight:700;color:{color};'>
                {title}
            </span>
        </div>
        """, unsafe_allow_html=True)

        r1 = st.columns(3)
        r1[0].metric("🏟️ Matches",     stats["matches"])
        r1[1].metric("🏃 Runs",         stats["runs"])
        r1[2].metric("⬆️ Highest",      stats["highest_score"])

        r2 = st.columns(3)
        r2[0].metric("💯 100s",         stats["hundreads"])
        r2[1].metric("5️⃣0️⃣ 50s",       stats["fifties"])
        r2[2].metric("4️⃣ Fours",        stats["fours"])

        st.metric("6️⃣ Sixes", stats["sixes"])

        with st.expander("📊 Full Stats Table"):
            df = pd.DataFrame({
                "Statistic": list(stats.keys()),
                "Value":     list(stats.values())
            })
            st.dataframe(df, use_container_width=True, hide_index=True)

    # ── Format tabs ──
    tab_odi, tab_t20, tab_test, tab_ipl = st.tabs(["🟢 ODI", "⚡ T20", "🏛️ TEST", "💜 IPL"])

    with tab_odi:
        show_stats("ODI Career", data["ODI"],  "#22c55e")

    with tab_t20:
        show_stats("T20 Career", data["T20"],  "#facc15")

    with tab_test:
        show_stats("Test Career", data["TEST"], "#60a5fa")

    with tab_ipl:
        show_stats("IPL Career", data["IPL"],  "#c084fc")

    # ── Summary ──
    st.markdown("""
    <div style='margin-top:1.5rem;margin-bottom:0.5rem;
                font-size:1.2rem;font-weight:700;color:#86efac;'>
        📝 Player Summary
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background:#0f1a0f;border:1px solid #166534;border-radius:14px;
                padding:1.2rem 1.4rem;color:#d1fae5;font-size:0.95rem;line-height:1.8;'>
        {data["Summary"]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("🔧 Raw JSON Response"):
        st.json(data)