import json
from pathlib import Path
import streamlit as st
from bird_details import render_bird_details
from balcony_coach import render_balcony_coach
from sightings import render_sightings



st.set_page_config(
    page_title="Wingscape | Discover. Observe. Welcome.",
    page_icon="🌿",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --paper: #f6f4ea;
        --paper-light: #fffdf7;
        --forest: #214b3b;
        --ink: #20372e;
        --body: #35483e;
        --sage: #e1e9de;
        --sage-deep: #c7d5c5;
        --clay: #9b4f35;
        --line: #d7ddd1;
    }

    .stApp {
        background-color: var(--paper);
        background-image: repeating-linear-gradient(
            0deg, rgba(33, 75, 59, 0.018) 0, rgba(33, 75, 59, 0.018) 1px,
            transparent 1px, transparent 6px
        );
        color: var(--ink);
    }

    /* Sidebar styling matching the nature-journal palette */
    [data-testid="stSidebar"] {
        background-color: #f1efe5;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] .stRadio label {
        color: var(--ink) !important;
        font-family: "Trebuchet MS", sans-serif !important;
        font-weight: 500 !important;
    }

    .sidebar-brand {
        padding: 0.5rem 0 1rem;
    }

    .sidebar-footer-note {
        margin-top: 1rem;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 3rem;
        padding-bottom: 2rem;
    }

    .wingscape-page {
        color: var(--body);
        font-family: Georgia, "Times New Roman", serif;
    }

    .eyebrow {
        margin: 0 0 1rem;
        color: var(--clay);
        font: 700 0.76rem/1.4 "Trebuchet MS", sans-serif;
        letter-spacing: 0;
        text-transform: uppercase;
    }

    .hero {
        display: grid;
        grid-template-columns: minmax(0, 1.45fr) minmax(220px, 0.75fr);
        align-items: center;
        gap: clamp(2rem, 7vw, 6rem);
        padding: 2rem 0 3.5rem;
        border-bottom: 1px solid var(--line);
    }

    .hero h1 {
        margin: 0;
        color: var(--forest);
        font-size: clamp(3rem, 7vw, 5.5rem);
        font-weight: 500;
        line-height: 0.98;
    }

    .hero-tagline {
        margin: 1.25rem 0 1rem;
        color: var(--ink);
        font-size: clamp(1.45rem, 3vw, 2.1rem);
        line-height: 1.2;
    }

    .hero-copy {
        max-width: 38rem;
        margin: 0;
        color: var(--body);
        font: 1.05rem/1.7 "Trebuchet MS", sans-serif;
    }

    .cta-link {
        display: inline-flex;
        align-items: center;
        min-height: 48px;
        margin-top: 1.5rem;
        padding: 0.8rem 1.2rem;
        border: 2px solid var(--forest);
        border-radius: 3px;
        background: var(--forest);
        color: var(--paper-light) !important;
        font: 700 0.95rem/1.2 "Trebuchet MS", sans-serif;
        text-decoration: none !important;
        transition: background-color 150ms ease, color 150ms ease;
    }

    .cta-link:hover {
        background: var(--paper-light);
        color: var(--forest) !important;
    }

    .cta-link:focus-visible,
    a:focus-visible,
    button:focus-visible {
        outline: 3px solid var(--clay);
        outline-offset: 4px;
    }

    .field-note {
        padding: 1.5rem 0 1.5rem 1.5rem;
        border-left: 2px solid var(--sage-deep);
    }

    .field-note .note-number {
        display: block;
        margin-bottom: 0.5rem;
        color: var(--forest);
        font-size: 4.5rem;
        line-height: 1;
    }

    .field-note p:last-child {
        margin: 0;
        color: var(--body);
        font: 0.98rem/1.6 "Trebuchet MS", sans-serif;
    }

    .mission {
        margin: 2.5rem 0 3.5rem;
        padding: clamp(1.5rem, 4vw, 3rem);
        border-radius: 4px;
        background: var(--forest);
        color: var(--paper-light);
        scroll-margin-top: 1.5rem;
    }

    .mission .eyebrow {
        color: #e4c5a4;
    }

    .mission h2 {
        margin: 0 0 0.9rem;
        color: var(--paper-light);
        font-size: clamp(1.8rem, 4vw, 2.7rem);
        font-weight: 500;
        line-height: 1.15;
    }

    .mission p:last-child {
        max-width: 52rem;
        margin: 0;
        color: #f1f3e9;
        font: 1.05rem/1.75 "Trebuchet MS", sans-serif;
    }

    .section-heading {
        margin: 0 0 1.25rem;
        color: var(--forest);
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 500;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
    }

    .feature-card {
        min-height: 190px;
        padding: 1.5rem;
        border: 1px solid var(--line);
        border-top: 3px solid var(--sage-deep);
        border-radius: 3px;
        background: var(--paper-light);
    }

    .feature-card .card-number {
        margin: 0 0 1.1rem;
        color: var(--clay);
        font: 700 0.75rem/1.4 Arial, sans-serif;
        letter-spacing: 0;
    }

    .feature-card h3 {
        margin: 0 0 0.55rem;
        color: var(--forest);
        font-size: 1.45rem;
        font-weight: 500;
        line-height: 1.2;
    }

    .feature-card p:last-child {
        margin: 0;
        color: var(--body);
        font: 0.96rem/1.6 "Trebuchet MS", sans-serif;
    }

    /* Discover Birds Header & Search Styling */
    .discover-header {
        padding: 0.5rem 0 2rem;
        border-bottom: 1px solid var(--line);
        margin-bottom: 2rem;
    }

    .discover-header h1 {
        margin: 0 0 0.6rem;
        color: var(--forest);
        font-size: clamp(2.4rem, 5vw, 3.8rem);
        font-weight: 500;
        line-height: 1.05;
        font-family: Georgia, serif;
    }

    .discover-header p.lead {
        max-width: 48rem;
        margin: 0;
        color: var(--body);
        font: 1.05rem/1.65 "Trebuchet MS", sans-serif;
    }

    .search-meta-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.4rem 0 1rem;
        color: var(--body);
        font: 0.92rem "Trebuchet MS", sans-serif;
        border-bottom: 1px solid var(--line);
        margin-bottom: 1.75rem;
    }

    /* Bird Card Styling */
    .bird-card-container {
        background: var(--paper-light);
        border: 1px solid var(--line);
        border-top: 3px solid var(--forest);
        border-radius: 4px;
        padding: 1.35rem 1.35rem 1rem;
        margin-bottom: 0.5rem;
    }

    .bird-card-header {
        display: flex;
        align-items: flex-start;
        gap: 0.9rem;
        margin-bottom: 0.85rem;
    }

    .bird-seal {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: var(--sage);
        border: 1px solid var(--sage-deep);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.45rem;
        flex-shrink: 0;
    }

    .bird-card-titles {
        flex-grow: 1;
    }

    .bird-card-titles .specimen-tag {
        display: block;
        color: var(--clay);
        font: 700 0.72rem/1.2 "Trebuchet MS", sans-serif;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
    }

    .bird-common-name {
        margin: 0;
        color: var(--forest);
        font-size: 1.38rem;
        font-weight: 500;
        line-height: 1.2;
        font-family: Georgia, serif;
    }

    .bird-scientific-name {
        display: block;
        color: var(--clay);
        font-size: 0.92rem;
        font-style: italic;
        font-family: Georgia, serif;
        margin-top: 0.15rem;
    }

    .bird-description {
        color: var(--body);
        font: 0.96rem/1.65 "Trebuchet MS", sans-serif;
        margin: 0.75rem 0 0.85rem;
    }

    .bird-habitat-chip {
        display: inline-flex;
        align-items: center;
        background: var(--sage);
        color: var(--ink);
        padding: 0.3rem 0.65rem;
        border-radius: 3px;
        font: 500 0.82rem/1.2 "Trebuchet MS", sans-serif;
        margin-bottom: 0.25rem;
    }

    /* Bird Photo Plate & Graceful Fallback */
    .bird-photo-plate {
        position: relative;
        width: 100%;
        height: 195px;
        background: var(--sage);
        border: 1px solid var(--line);
        border-radius: 3px;
        overflow: hidden;
        margin: 0.65rem 0 0.35rem;
    }

    .bird-photo-fallback {
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: var(--sage);
        color: var(--forest);
        z-index: 1;
    }

    .fallback-emblem {
        font-size: 2.2rem;
        line-height: 1;
        margin-bottom: 0.25rem;
    }

    .fallback-text {
        font: 700 0.72rem/1.2 "Trebuchet MS", sans-serif;
        color: var(--body);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .bird-photo-img {
        position: relative;
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        z-index: 2;
    }

    .photo-attribution {
        font: 0.75rem/1.3 "Trebuchet MS", sans-serif;
        color: #6a7c72;
        margin-bottom: 0.65rem;
    }

    .photo-attribution a {
        color: var(--forest);
        text-decoration: underline;
    }

    /* Empty search state */
    .empty-search-box {
        background: var(--paper-light);
        border: 1px dashed var(--sage-deep);
        border-radius: 4px;
        padding: 3rem 1.5rem;
        text-align: center;
        margin: 2rem 0;
    }

    .empty-search-box h3 {
        color: var(--forest);
        font-family: Georgia, serif;
        font-size: 1.6rem;
        margin: 0.5rem 0 0.5rem;
    }

    .empty-search-box p {
        color: var(--body);
        font: 0.98rem/1.6 "Trebuchet MS", sans-serif;
        margin: 0 0 0.5rem;
    }

    .page-footer {
        margin-top: 3.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid var(--line);
        color: var(--body);
        font: 0.86rem/1.5 "Trebuchet MS", sans-serif;
    }

    @media (max-width: 720px) {
        .block-container {
            padding-top: 1.25rem;
        }

        .hero {
            grid-template-columns: 1fr;
            gap: 1.5rem;
            padding: 1.5rem 0 2rem;
        }

        .field-note {
            padding: 0.25rem 0 0.25rem 1rem;
        }

        .field-note .note-number {
            font-size: 3rem;
        }

        .mission {
            margin: 1.75rem 0 2.5rem;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }

        .feature-card {
            min-height: 0;
        }
    }

    /* AI Balcony Coach Styling */
    .coach-profile-summary {
        background: var(--paper-light);
        border: 1px solid var(--line);
        border-left: 4px solid var(--forest);
        border-radius: 4px;
        padding: 1rem 1.25rem;
        margin-bottom: 1.5rem;
    }

    .profile-summary-title {
        color: var(--clay);
        font: 700 0.75rem/1.2 "Trebuchet MS", sans-serif;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .profile-chip {
        display: inline-block;
        background: var(--sage);
        color: var(--ink);
        padding: 0.25rem 0.65rem;
        border-radius: 3px;
        font: 500 0.85rem/1.3 "Trebuchet MS", sans-serif;
        margin: 0.2rem 0.3rem 0.2rem 0;
        border: 1px solid var(--sage-deep);
    }

    /* My Sightings Journal Styling */
    .sighting-card {
        background: var(--paper-light);
        border: 1px solid var(--line);
        border-left: 4px solid var(--forest);
        border-radius: 4px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 0.95rem;
    }

    .sighting-card-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.4rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .sighting-date-tag {
        color: var(--clay);
        font: 700 0.78rem/1.2 "Trebuchet MS", sans-serif;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .sighting-count-chip {
        display: inline-flex;
        align-items: center;
        background: var(--sage);
        color: var(--forest);
        padding: 0.2rem 0.6rem;
        border-radius: 3px;
        font: 600 0.82rem/1.2 "Trebuchet MS", sans-serif;
        border: 1px solid var(--sage-deep);
    }

    .sighting-species-name {
        margin: 0;
        color: var(--forest);
        font-family: Georgia, serif;
        font-size: 1.35rem;
        font-weight: 500;
        line-height: 1.25;
    }

    .sighting-scientific-name {
        color: var(--clay);
        font-style: italic;
        font-size: 0.92rem;
        font-family: Georgia, serif;
    }

    .sighting-notes-text {
        margin: 0.65rem 0 0;
        color: var(--body);
        font: 0.95rem/1.6 "Trebuchet MS", sans-serif;
        padding-top: 0.5rem;
        border-top: 1px dashed var(--line);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Botanical and nature emblem fallback seals for birds
BIRD_EMBLEMS = {
    "house-sparrow": "🌾",
    "common-myna": "🌻",
    "rock-pigeon": "🕊️",
    "rose-ringed-parakeet": "🦜",
    "red-vented-bulbul": "🌸",
    "oriental-magpie-robin": "🎶",
    "purple-sunbird": "🌺",
    "indian-peafowl": "🦚",
}


@st.cache_data
def load_bird_data():
    """Load curated bird dataset from data/birds.json."""
    data_file = Path(__file__).parent / "data" / "birds.json"
    if not data_file.exists():
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)


# Navigation state management
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


def navigate_to(page: str) -> None:
    """Synchronize navigation state variables to prevent sidebar radio conflicts."""
    st.session_state.current_page = page
    st.session_state.nav_selection = page


def clear_search() -> None:
    """Clear bird search query in session state before widget instantiation."""
    st.session_state.bird_search_input = ""

PAGES = ["Home", "Discover Birds", "AI Balcony Coach", "My Sightings"]
current_index = PAGES.index(st.session_state.current_page) if st.session_state.current_page in PAGES else 0



# Sidebar Navigation
st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <p class="eyebrow" style="margin-bottom: 0.25rem;">Field Journal</p>
        <h2 style="margin: 0; color: #214b3b; font-family: Georgia, serif; font-size: 1.6rem; font-weight: 500;">🌿 Wingscape</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

selected_nav = st.sidebar.radio(
    "Navigation Menu",
    options=PAGES,
    index=current_index,
    key="nav_selection",
    label_visibility="collapsed",
)

if selected_nav != st.session_state.current_page:
    st.session_state.current_page = selected_nav
    st.rerun()

st.sidebar.markdown(
    """
    <div class="sidebar-footer-note">
        <hr style="border: none; border-top: 1px solid #d7ddd1; margin: 1.5rem 0 1rem;" />
        <p style="margin: 0; font: 0.85rem/1.5 'Trebuchet MS', sans-serif; color: #35483e;">
            <strong>Wingscape</strong> brings city nature closer to home through daily observations and balcony-friendly practices.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================================================================
# Page 1: Home
# ==============================================================================
if st.session_state.current_page == "Home":
    st.markdown(
        """
        <div class="wingscape-page">
          <section class="hero" aria-labelledby="wingscape-title">
            <div>
              <p class="eyebrow">A field guide for city nature</p>
              <h1 id="wingscape-title">Wingscape</h1>
              <p class="hero-tagline">Discover. Observe. Welcome.</p>
              <p class="hero-copy">
                Bring nature closer to home. Get to know the birds around you,
                make your balcony more welcoming, and find a little more time
                to notice the outdoors.
              </p>
              <a class="cta-link" href="#daily-mission">Start observing</a>
            </div>
            <aside class="field-note" aria-label="A note about observing">
              <p class="eyebrow">The practice</p>
              <span class="note-number" aria-hidden="true">01</span>
              <p>Slow down. Look closely. Let the neighborhood come into view.</p>
            </aside>
          </section>

          <section class="mission" id="daily-mission" aria-labelledby="mission-title">
            <p class="eyebrow">Today's outdoor mission · 5 minutes</p>
            <h2 id="mission-title">Notice what is already here.</h2>
            <p>
              Take five minutes to observe your balcony or nearby surroundings.
              Notice any birds you see, listen to their calls, and observe
              without disturbing them.
            </p>
          </section>

          <section aria-labelledby="explore-title">
            <p class="eyebrow">Explore the journal</p>
            <h2 class="section-heading" id="explore-title">Explore Wingscape</h2>
            <div class="feature-grid">
              <article class="feature-card">
                <p class="card-number">01 / FIELD GUIDE</p>
                <h3>Discover Birds</h3>
                <p>Learn about birds commonly found around you.</p>
              </article>
              <article class="feature-card">
                <p class="card-number">02 / HOME HABITAT</p>
                <h3>Balcony Coach</h3>
                <p>Explore practical ways to make your balcony bird-friendly.</p>
              </article>
              <article class="feature-card">
                <p class="card-number">03 / FIELD JOURNAL</p>
                <h3>My Sightings</h3>
                <p>Keep a record of the birds you observe.</p>
              </article>
            </div>
          </section>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # In-page shortcuts to explore features
    st.write("")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])
    with nav_col1:
        st.button(
            "Explore Discover Birds →",
            key="btn_home_to_discover",
            on_click=navigate_to,
            args=("Discover Birds",),
            use_container_width=True,
        )
    with nav_col2:
        st.button(
            "Open AI Balcony Coach →",
            key="btn_home_to_coach",
            on_click=navigate_to,
            args=("AI Balcony Coach",),
            use_container_width=True,
        )
    with nav_col3:
        st.button(
            "Open My Sightings →",
            key="btn_home_to_sightings",
            on_click=navigate_to,
            args=("My Sightings",),
            use_container_width=True,
        )



    st.markdown(
        """
        <footer class="page-footer">
          Wingscape · Small steps towards a more bird-friendly world.
        </footer>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# Page 2: Discover Birds
# ==============================================================================
elif st.session_state.current_page == "Discover Birds":
    birds = load_bird_data()

    top_back_col, _ = st.columns([1, 4])
    with top_back_col:
        st.button(
            "← Back to Home",
            key="btn_back_to_home",
            on_click=navigate_to,
            args=("Home",),
        )

    st.markdown(
        """
        <div class="discover-header">
            <p class="eyebrow">01 / Regional Field Guide · India</p>
            <h1>Discover Birds</h1>
            <p class="lead">
                Explore common urban bird species sharing city trees, balconies, and neighborhood gardens.
                Search by common or scientific name to identify characteristics and learn tips for responsible observation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Search Bar
    search_col, clear_col = st.columns([4, 1])
    with search_col:
        search_query = st.text_input(
            "Search birds",
            value="",
            placeholder="Search by common or scientific name (e.g. Sparrow, Columba, Bulbul...)",
            key="bird_search_input",
            label_visibility="collapsed",
        ).strip()

    with clear_col:
        if search_query:
            st.button(
                "Clear search",
                key="btn_clear_search",
                on_click=clear_search,
            )

    # Case-insensitive filtering
    q_lower = search_query.lower()
    if search_query:
        filtered_birds = [
            b for b in birds
            if q_lower in b.get("common_name", "").lower()
            or q_lower in b.get("scientific_name", "").lower()
        ]
        st.markdown(
            f"""
            <div class="search-meta-bar">
                <span>Showing <strong>{len(filtered_birds)}</strong> of <strong>{len(birds)}</strong> species matching "<em>{search_query}</em>"</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        filtered_birds = birds
        st.markdown(
            f"""
            <div class="search-meta-bar">
                <span>Showing all <strong>{len(birds)}</strong> curated species</span>
                <span>🌿 Fallback field-seal emblems active</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Empty State
    if not filtered_birds:
        st.markdown(
            f"""
            <div class="empty-search-box">
                <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">🔍</div>
                <h3>No birds found</h3>
                <p>No species matched your search for "<strong>{search_query}</strong>".</p>
                <p style="color: #6d7a72; font-size: 0.92rem;">
                    Try searching for common names like <em>Sparrow</em>, <em>Myna</em>, <em>Parakeet</em>, or scientific genera like <em>Passer</em> or <em>Cinnyris</em>.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        # 2-column responsive layout for bird cards
        cols = st.columns(2)
        for i, bird in enumerate(filtered_birds):
            col = cols[i % 2]
            bird_id = bird.get("id", "")
            emblem = BIRD_EMBLEMS.get(bird_id, "🌿")
            bird_index = i + 1
            image_meta = bird.get("image", {})
            img_url = image_meta.get("url", "")
            img_photographer = image_meta.get("photographer", "Wikimedia Commons")
            img_source = image_meta.get("source_url", "#")
            img_license = image_meta.get("license", "Creative Commons")

            img_tag = (
                f'<img class="bird-photo-img" src="{img_url}" alt="{bird.get("common_name", "")} ({bird.get("scientific_name", "")})" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\';" />'
                if img_url
                else ""
            )

            photo_credit_html = (
                f'<div class="photo-attribution">Photo: <a href="{img_source}" target="_blank" rel="noopener noreferrer">{img_photographer}</a> · {img_license}</div>'
                if img_url
                else ""
            )

            with col:
                st.markdown(
                    f"""
                    <div class="bird-card-container">
                        <div class="bird-card-header">
                            <div class="bird-seal" aria-hidden="true">{emblem}</div>
                            <div class="bird-card-titles">
                                <span class="specimen-tag">SPECIES #{bird_index:02d}</span>
                                <h3 class="bird-common-name">{bird.get('common_name', '')}</h3>
                                <span class="bird-scientific-name">{bird.get('scientific_name', '')}</span>
                            </div>
                        </div>
                        <div class="bird-photo-plate">
                            <div class="bird-photo-fallback">
                                <span class="fallback-emblem">{emblem}</span>
                                <span class="fallback-text">{bird.get('common_name', '')}</span>
                            </div>
                            {img_tag}
                        </div>
                        {photo_credit_html}
                        <p class="bird-description">{bird.get('description', '')}</p>
                        <div class="bird-habitat-chip">
                            🏡 <strong>Habitat:</strong>&nbsp;{bird.get('habitat', '').split(',')[0]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Detail expander on each card
                with st.expander(f"📖 Field Details & Tips: {bird.get('common_name', '')}", expanded=False):
                    render_bird_details(bird)

    st.markdown(
        """
        <footer class="page-footer">
          Wingscape · Small steps towards a more bird-friendly world.
        </footer>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# Page 3: AI Balcony Coach
# ==============================================================================
elif st.session_state.current_page == "AI Balcony Coach":
    render_balcony_coach(navigate_to)


# ==============================================================================
# Page 4: My Sightings
# ==============================================================================
elif st.session_state.current_page == "My Sightings":
    birds = load_bird_data()
    render_sightings(navigate_to, birds)
