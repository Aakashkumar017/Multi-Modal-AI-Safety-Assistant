import streamlit as st
from PIL import Image
from src.image_capture import generate_caption
from src.hazard_analysis import analyze_hazard

# ─── Page Config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Safety Assistant",
    page_icon="⚠️",
    layout="centered",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────

st.markdown("""
<style>
    /* Overall page background */
    .stApp {
        background-color: #0f1117;
        color: #e8eaf0;
    }

    /* Hide default streamlit header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Hero banner */
    .hero {
        background: linear-gradient(135deg, #1a1d2e 0%, #16213e 60%, #0f3460 100%);
        border: 1px solid #e53935;
        border-radius: 12px;
        padding: 32px 28px 24px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "⚠";
        position: absolute;
        right: 24px;
        top: 16px;
        font-size: 64px;
        opacity: 0.08;
        line-height: 1;
    }
    .hero h1 {
        font-size: 1.9rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 6px;
        letter-spacing: -0.5px;
    }
    .hero p {
        color: #9ea3b5;
        font-size: 0.95rem;
        margin: 0;
        line-height: 1.6;
    }
    .hero .badge {
        display: inline-block;
        background: #e5393522;
        border: 1px solid #e53935;
        color: #ef5350;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 20px;
        margin-bottom: 12px;
    }

    /* Section cards */
    .card {
        background: #161b27;
        border: 1px solid #272d3f;
        border-radius: 10px;
        padding: 20px 22px;
        margin-bottom: 18px;
    }
    .card-title {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 1.1px;
        text-transform: uppercase;
        color: #6c7490;
        margin-bottom: 10px;
    }

    /* Result boxes */
    .result-caption {
        background: #1a2035;
        border-left: 3px solid #3d8eff;
        border-radius: 0 8px 8px 0;
        padding: 14px 16px;
        color: #c5cae9;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 18px;
        font-style: italic;
    }
    .result-analysis {
        background: #1c1a20;
        border-left: 3px solid #e53935;
        border-radius: 0 8px 8px 0;
        padding: 16px 18px;
        color: #e8eaf0;
        font-size: 0.95rem;
        line-height: 1.7;
        white-space: pre-wrap;
    }

    /* Danger tag */
    .danger-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #e5393515;
        border: 1px solid #e53935;
        color: #ef5350;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 12px;
    }

    /* Step labels */
    .step-label {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #3d8eff;
        margin-bottom: 6px;
    }

    /* Streamlit button override */
    .stButton > button {
        background: #e53935;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 10px 28px;
        transition: background 0.2s;
        width: 100%;
    }
    .stButton > button:hover {
        background: #c62828;
        color: white;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #161b27;
        border: 1.5px dashed #272d3f;
        border-radius: 10px;
        padding: 8px;
    }

    /* Text input */
    .stTextInput > div > div > input {
        background: #161b27;
        border: 1px solid #272d3f;
        border-radius: 8px;
        color: #e8eaf0;
        font-size: 0.95rem;
        padding: 10px 14px;
    }

    /* Spinner */
    .stSpinner > div {
        border-top-color: #e53935 !important;
    }

    /* Divider */
    hr {
        border-color: #272d3f;
        margin: 24px 0;
    }

    /* Image display */
    [data-testid="stImage"] img {
        border-radius: 10px;
        border: 1px solid #272d3f;
    }
</style>
""", unsafe_allow_html=True)


# ─── Hero Section ─────────────────────────────────────────────────────────────

st.markdown("""
<div class="hero">
    <div class="badge">⚠ Hazard Detection</div>
    <h1>AI Safety Assistant</h1>
    <p>Upload an image of a potentially dangerous situation. The assistant will
    describe what it sees and give you a clear safety assessment — no jargon,
    just what the real danger is and how to stay safe.</p>
</div>
""", unsafe_allow_html=True)


# ─── Step 1: Upload Image ─────────────────────────────────────────────────────

st.markdown('<div class="step-label">Step 1 — Upload an Image</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    label="Upload Image",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed",
)


# ─── Step 2: Ask Your Question ────────────────────────────────────────────────

st.markdown('<div class="step-label" style="margin-top:18px;">Step 2 — Your Question</div>', unsafe_allow_html=True)

query = st.text_input(
    label="Question",
    value="What is the primary danger shown in this image?",
    label_visibility="collapsed",
    placeholder="e.g. What is the primary danger shown in this image?",
)


# ─── Step 3: Analyze ──────────────────────────────────────────────────────────

if uploaded_file:
    image = Image.open(uploaded_file)

    st.markdown('<div class="step-label" style="margin-top:18px;">Step 3 — Preview</div>', unsafe_allow_html=True)
    st.image(image, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    run = st.button("🔍 Analyze for Danger")

    if run:
        if not query.strip():
            st.warning("Please enter a question before analyzing.")
        else:
            # ── Caption Generation ─────────────────────────────────────────
            with st.spinner("Reading the image..."):
                caption = generate_caption(image)

            st.markdown('<div class="step-label" style="margin-top:22px;">What the AI Sees</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-caption">"{caption}"</div>', unsafe_allow_html=True)

            # ── Hazard Analysis ────────────────────────────────────────────
            with st.spinner("Assessing the danger..."):
                analysis = analyze_hazard(query, caption)

            st.markdown('<div class="danger-tag">🚨 Hazard Report</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-analysis">{analysis}</div>', unsafe_allow_html=True)

else:
    # Friendly empty state
    st.markdown("""
    <div style="text-align:center; padding: 40px 20px; color: #4a5068;">
        <div style="font-size: 2.5rem; margin-bottom: 12px;">📷</div>
        <div style="font-size: 0.95rem;">Upload an image above to get started.</div>
        <div style="font-size: 0.82rem; margin-top: 6px; color: #353b52;">
            Works with electrical hazards, wet floors, sharp objects, structural damage, and more.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── Footer ───────────────────────────────────────────────────────────────────

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color: #3a3f55; font-size: 0.8rem;">
    Powered by BLIP (Salesforce) + Llama 3.3 via Groq &nbsp;|&nbsp; Multi-Modal AI Safety Assistant
</div>
""", unsafe_allow_html=True)