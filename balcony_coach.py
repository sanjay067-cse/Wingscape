"""Wingscape AI Balcony Coach Component.

Provides practical, tailored guidance for urban Indian apartment balconies
to safely welcome neighborhood birds, using the Groq API (openai/gpt-oss-20b).
"""

from typing import Optional, Tuple
import streamlit as st

SYSTEM_PROMPT = """You are Wingscape's AI Balcony Coach, a thoughtful, practical avian habitat advisor specializing in urban Indian apartment balconies.
Your mission is to help apartment dwellers make their balconies safer, greener, and more welcoming to urban wildlife (such as sparrows, bulbuls, sunbirds, and mynas).

Guidelines:
1. Provide realistic, budget-conscious suggestions tailored to urban Indian living conditions (monsoons, summer heat, pigeon netting, high-rise balconies).
2. Recommend native Indian balcony-friendly plants suitable for the user's sunlight and space (e.g., Tulsi, Hibiscus, Bougainvillea, Curry Leaf, Mogra, Marigold, Portulaca, Kaner).
3. Emphasize safe hydration: shallow terracotta dishes (1-2 inches deep), placed in shade, clean fresh water daily, small stones as perches to prevent drowning.
4. If feeding is addressed, recommend only species-appropriate fresh grains (foxtail millet, pearl millet / bajra, broken rice); strongly discourage processed, oily, or salted human food (bread, biscuits, namkeen).
5. Stress bird safety: keep water away from ambush spots (stray cats), avoid synthetic chemical pesticides or insecticides, ensure window collision safety, and avoid dangerous modifications.
6. Crucial: Do NOT guarantee or promise that specific bird species will arrive. Nature works on its own schedule.
7. Tone: Warm, encouraging, nature-journal aesthetic, practical, grounded.

Output Format:
You MUST structure your response into exactly three sections with clear markdown headings:

### 1. Your Balcony Plan
[Tailored guidance on layout, plant selection based on sunlight, water station setup, and space utilization.]

### 2. Three Things to Do First
[Exactly three clear, manageable, actionable bullet points to start with this weekend.]

### 3. Keep Birds Safe
[Crucial safety, hygiene, and ethical observation rules: clean water, no chemical pesticides, predator protection, avoiding harmful foods.]
"""


def build_user_prompt(
    sunlight: str,
    size: str,
    plants: str,
    goal: str,
    budget: str,
    details: str,
) -> str:
    """Build structured user prompt string from form inputs."""
    lines = [
        "Please create a personalized balcony habitat plan for my apartment balcony:",
        f"- **Sunlight:** {sunlight}",
        f"- **Balcony Size:** {size}",
        f"- **Existing Plants:** {plants}",
        f"- **Primary Goal:** {goal}",
        f"- **Budget:** {budget}",
    ]
    clean_details = (details or "").strip()[:300]
    if clean_details:
        lines.append(f"- **Additional Details / Constraints:** {clean_details}")
    return "\n".join(lines)


def generate_balcony_plan(
    sunlight: str,
    size: str,
    plants: str,
    goal: str,
    budget: str,
    details: str,
    api_key: str,
) -> Tuple[Optional[str], Optional[str]]:
    """Call the Groq API to generate a balcony habitat recommendation.

    Returns:
        (plan_text, None) on success.
        (None, error_message) on failure.
    """
    if not api_key or not api_key.strip():
        return None, "API key is missing. Please configure GROQ_API_KEY in .streamlit/secrets.toml."

    try:
        from groq import (
            Groq,
            AuthenticationError,
            RateLimitError,
            APIConnectionError,
            APITimeoutError,
            APIStatusError,
        )
    except ImportError:
        return None, "The Groq Python library is not installed. Please check requirements.txt."

    try:
        client = Groq(api_key=api_key)
        user_message = build_user_prompt(sunlight, size, plants, goal, budget, details)
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=1500,
            reasoning_format="hidden",
            temperature=0.7,
        )

        if not response.choices or not response.choices[0].message:
            return None, "The AI coach did not return a response. Please try submitting again."

        content = (response.choices[0].message.content or "").strip()
        if not content:
            return None, "The AI coach returned an empty response. Please try submitting again."

        return content, None

    except AuthenticationError:
        return (
            None,
            "Authentication failed. The configured Groq API key is invalid or expired. Please check .streamlit/secrets.toml.",
        )
    except RateLimitError:
        return (
            None,
            "The AI service is temporarily experiencing high demand or rate limits. Please pause for a moment and try again.",
        )
    except (APIConnectionError, APITimeoutError):
        return (
            None,
            "Could not connect to the AI service. Please check your network connection and try again.",
        )
    except APIStatusError as e:
        status_code = getattr(e, "status_code", "error")
        return (
            None,
            f"The AI service returned a status error ({status_code}). Please try again in a few moments.",
        )
    except Exception:
        return (
            None,
            "An unexpected error occurred while communicating with the AI service. Please try again later.",
        )


def reset_coach_plan() -> None:
    """Clear cached plan in session state to allow generating a fresh plan."""
    st.session_state.coach_plan = None
    st.session_state.coach_profile = None


def render_balcony_coach(navigate_to) -> None:
    """Render the AI Balcony Coach page within Wingscape."""
    # Ensure session state variables exist
    if "coach_plan" not in st.session_state:
        st.session_state.coach_plan = None
    if "coach_profile" not in st.session_state:
        st.session_state.coach_profile = None

    # Navigation back to Home
    top_back_col, _ = st.columns([1, 4])
    with top_back_col:
        st.button(
            "← Back to Home",
            key="btn_coach_back_to_home",
            on_click=navigate_to,
            args=("Home",),
        )

    # Page Header
    st.markdown(
        """
        <div class="discover-header">
            <p class="eyebrow">02 / Home Habitat · Urban Balcony Guide</p>
            <h1>AI Balcony Coach</h1>
            <p class="lead">
                Transform your city balcony into a welcoming, safe micro-sanctuary for neighborhood birds.
                Share a few details about your sunlight and space to receive tailored, practical recommendations
                for an urban Indian apartment.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # If a plan is already generated, render the plan view
    if st.session_state.coach_plan:
        _render_plan_view(navigate_to)
    else:
        _render_form_view()


def _render_form_view() -> None:
    """Render the balcony assessment form."""
    api_key_configured = (
        "GROQ_API_KEY" in st.secrets and bool(st.secrets["GROQ_API_KEY"].strip())
    )

    if not api_key_configured:
        st.warning(
            "⚠️ **Groq API key not configured.**\n\n"
            "To generate personalized habitat recommendations, configure `GROQ_API_KEY` in `.streamlit/secrets.toml`.\n\n"
            "You can still explore the bird guide on the **Discover Birds** page or try the daily 5-minute outdoor observation on the **Home** page."
        )

    with st.form(key="balcony_coach_form"):
        st.markdown(
            """
            <div style="margin-bottom: 1.25rem;">
                <h3 style="color: #214b3b; font-family: Georgia, serif; font-size: 1.35rem; margin: 0 0 0.35rem;">
                    Describe your balcony
                </h3>
                <p style="color: #35483e; font-size: 0.95rem; margin: 0; font-family: 'Trebuchet MS', sans-serif;">
                    Choose the options that best match your space. No exact address or personal details are collected.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            sunlight = st.selectbox(
                "Sunlight exposure",
                options=[
                    "Full sunlight (6+ hours direct sunlight)",
                    "Partial sunlight (3–5 hours morning or evening sun)",
                    "Mostly shade (less than 3 hours direct sun)",
                ],
                index=1,
                help="How much direct sunlight reaches your balcony daily?",
            )

            size = st.selectbox(
                "Balcony size",
                options=[
                    "Very small (standing room or narrow ledge)",
                    "Small (room for a few pots and a chair)",
                    "Large (spacious terrace or wide balcony)",
                ],
                index=1,
                help="The usable floor space available on your balcony.",
            )

            plants = st.selectbox(
                "Existing plants",
                options=[
                    "No plants yet",
                    "A few pots (1–4 potted plants)",
                    "Many plants (already quite green)",
                ],
                index=1,
                help="How much greenery is currently growing on your balcony?",
            )

        with col2:
            goal = st.selectbox(
                "Main goal",
                options=[
                    "Attract garden birds (sparrows, bulbuls, sunbirds)",
                    "Provide safe drinking water (hydration & bird bath)",
                    "Create a flowering balcony (bird- & pollinator-friendly blooms)",
                ],
                index=0,
                help="What is your primary hope for welcoming wildlife?",
            )

            budget = st.selectbox(
                "Budget level",
                options=[
                    "Low-cost (repurposed containers, terracotta bowls, DIY)",
                    "Moderate budget (nursery plants, sturdy pots, hanging brackets)",
                ],
                index=0,
                help="How much do you plan to invest initially?",
            )

            details = st.text_input(
                "Additional details (optional)",
                value="",
                placeholder="e.g., 5th floor, windy evenings, pigeon netting installed, pets at home...",
                max_chars=200,
                help="Optional notes like floor height, wind, or apartment society guidelines.",
            )

        submitted = st.form_submit_button(
            "Generate My Balcony Plan 🌱",
            use_container_width=True,
        )

    if submitted:
        if not api_key_configured:
            st.error(
                "Cannot generate plan: `GROQ_API_KEY` is missing from `.streamlit/secrets.toml`. "
                "Please add your API key to continue."
            )
            return

        with st.spinner("Consulting Wingscape Balcony Coach... drafting your tailored urban habitat plan."):
            plan, error = generate_balcony_plan(
                sunlight=sunlight,
                size=size,
                plants=plants,
                goal=goal,
                budget=budget,
                details=details,
                api_key=st.secrets["GROQ_API_KEY"],
            )

        if error:
            st.error(f"⚠️ {error}")
        elif plan:
            st.session_state.coach_plan = plan
            st.session_state.coach_profile = {
                "sunlight": sunlight.split(" (")[0],
                "size": size.split(" (")[0],
                "plants": plants.split(" (")[0],
                "goal": goal.split(" (")[0],
                "budget": budget.split(" (")[0],
                "details": details.strip() if details else None,
            }
            st.rerun()

    # Friendly privacy note
    st.markdown(
        """
        <div style="margin-top: 1.5rem; padding: 0.85rem 1.15rem; background: #fffdf7; border: 1px solid #d7ddd1; border-radius: 3px;">
            <p style="margin: 0; font: 0.88rem/1.5 'Trebuchet MS', sans-serif; color: #35483e;">
                🔒 <strong>Urban Balcony Ethics:</strong> Recommendations focus on safe native plants, clean shallow water,
                and predator-safe layouts. Wingscape advises against feeding processed human foods or making promises about wild bird arrivals.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_plan_view(navigate_to) -> None:
    """Render the generated balcony plan with action buttons."""
    profile = st.session_state.get("coach_profile") or {}
    plan = st.session_state.get("coach_plan") or ""

    st.success("🌿 **Your customized urban balcony plan is ready!**", icon="✨")

    # Profile Chips Summary
    if profile:
        chips_html = []
        if profile.get("sunlight"):
            chips_html.append(f'<span class="profile-chip">☀️ {profile["sunlight"]}</span>')
        if profile.get("size"):
            chips_html.append(f'<span class="profile-chip">📐 {profile["size"]}</span>')
        if profile.get("plants"):
            chips_html.append(f'<span class="profile-chip">🪴 {profile["plants"]}</span>')
        if profile.get("goal"):
            chips_html.append(f'<span class="profile-chip">🎯 {profile["goal"]}</span>')
        if profile.get("budget"):
            chips_html.append(f'<span class="profile-chip">💰 {profile["budget"]}</span>')

        chips_str = " ".join(chips_html)
        details_html = ""
        if profile.get("details"):
            details_html = f'<p style="margin: 0.5rem 0 0; font-size: 0.88rem; color: #35483e;"><em>Notes:</em> {profile["details"]}</p>'

        st.markdown(
            f"""
            <div class="coach-profile-summary">
                <div class="profile-summary-title">Your Balcony Profile</div>
                <div>{chips_str}</div>
                {details_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Render Plan Markdown Content
    st.markdown(plan)

    st.write("")
    st.write("")

    # Action Buttons: Reset or Explore Discover Birds
    col_reset, col_disc = st.columns([1, 1])
    with col_reset:
        st.button(
            "🌱 Adjust Balcony & Create New Plan",
            key="btn_reset_coach",
            on_click=reset_coach_plan,
            use_container_width=True,
        )
    with col_disc:
        st.button(
            "Explore Discover Birds →",
            key="btn_coach_to_discover",
            on_click=navigate_to,
            args=("Discover Birds",),
            use_container_width=True,
        )

    # Page footer
    st.markdown(
        """
        <footer class="page-footer" style="margin-top: 2.5rem;">
          Wingscape · Small steps towards a more bird-friendly world.
        </footer>
        """,
        unsafe_allow_html=True,
    )
