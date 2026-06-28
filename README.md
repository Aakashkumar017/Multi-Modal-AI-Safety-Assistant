# ⚠️ Multi-Modal AI Safety Assistant

A Streamlit app that detects hazards in images using **BLIP** (image captioning) + **Llama 3.3** via Groq (safety analysis).

Upload a photo of a dangerous situation and get a plain-language safety report: what the danger is, why it matters, and what to do about it.

---

## How It Works

```
User uploads image
      ↓
BLIP model reads the image → generates a caption
      ↓
Caption + user question → sent to Llama 3.3 (via Groq)
      ↓
Llama returns a structured hazard report
      ↓
Report displayed in the UI
```

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-safety-assistant.git
cd ai-safety-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free key at [console.groq.com](https://console.groq.com).

### 4. Run the app

```bash
streamlit run app.py
```

---

## Project Structure

```
├── app.py                  # Streamlit UI
├── src/
│   ├── image_capture.py    # BLIP captioning model
│   └── hazard_analysis.py  # Groq / Llama hazard analysis
├── requirements.txt
└── .env                    # Your API key (not committed)
```

---

## Example Scenario

**Image:** Frayed electrical cord next to a puddle of water on concrete.

**Question:** *"What is the primary danger shown in this image?"*

**Output:**

> ⚠️ **Main Danger:** Electrocution risk from a frayed live wire in contact with standing water.
>
> 🔍 **Why It's Dangerous:** Water conducts electricity. If the exposed wire touches the puddle, an electric current can travel through the water and electrocute anyone nearby — even if they're not touching the cord directly.
>
> ✅ **What To Do:**
> 1. Do not touch the cord or step in the water.
> 2. Cut power at the breaker immediately.
> 3. Call a licensed electrician before using the area again.

---

## Tech Stack

| Component | Tool |
|-----------|------|
| UI | Streamlit |
| Image Captioning | BLIP (Salesforce, via HuggingFace) |
| Hazard Analysis | Llama 3.3-70B via Groq API |
| Language | Python 3.10+ |
