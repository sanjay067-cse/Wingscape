
import streamlit as st

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

    .page-footer {
        margin-top: 3rem;
        padding-top: 1rem;
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
    </style>
    """,
    unsafe_allow_html=True,
)

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

      <footer class="page-footer">
        Wingscape · Small steps towards a more bird-friendly world.
      </footer>
    </div>
    """,
    unsafe_allow_html=True,
)
