"""Wingscape My Sightings Component.

Provides a field journal for urban birdwatchers to record, review,
and export bird observations during their Streamlit session.
"""

import csv
import datetime
import html
import io
from typing import Any, Dict, List, Optional
import streamlit as st

# Botanical and bird seals matching Wingscape theme
DEFAULT_EMBLEMS = {
    "house-sparrow": "🌾",
    "common-myna": "🌻",
    "rock-pigeon": "🕊️",
    "rose-ringed-parakeet": "🦜",
    "red-vented-bulbul": "🌸",
    "oriental-magpie-robin": "🎶",
    "purple-sunbird": "🌺",
    "indian-peafowl": "🦚",
}


def init_sightings_state() -> None:
    """Ensure sightings state exists in st.session_state."""
    if "sightings" not in st.session_state:
        st.session_state.sightings = []


def clear_all_sightings() -> None:
    """Callback to reset sightings list before next rerun."""
    st.session_state.sightings = []


def generate_sightings_csv(sightings: List[Dict[str, Any]]) -> str:
    """Generate an RFC-4180 compliant CSV string from sightings list.

    Columns: Common Name, Scientific Name, Date Observed, Count, Observation Notes.
    """
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow([
        "Common Name",
        "Scientific Name",
        "Date Observed",
        "Count",
        "Observation Notes",
    ])
    for s in sightings:
        writer.writerow([
            s.get("common_name", ""),
            s.get("scientific_name", ""),
            s.get("date", ""),
            s.get("count", 1),
            s.get("notes", ""),
        ])
    return output.getvalue()


def render_sightings(navigate_to, birds: Optional[List[Dict[str, Any]]] = None) -> None:
    """Render the My Sightings field journal page."""
    init_sightings_state()

    # In-page navigation: Back to Home
    top_back_col, _ = st.columns([1, 4])
    with top_back_col:
        st.button(
            "← Back to Home",
            key="btn_sightings_back_to_home",
            on_click=navigate_to,
            args=("Home",),
        )

    # Page Header
    st.markdown(
        """
        <div class="discover-header">
            <p class="eyebrow">03 / Field Journal · Personal Observations</p>
            <h1>My Sightings</h1>
            <p class="lead">
                Keep a personal record of the birds you spot from your balcony, window, or neighborhood.
                Log species, counts, dates, and behavioral notes to build your nature journal.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Informational notice about session-based storage
    st.markdown(
        """
        <div style="background: #fffdf7; border: 1px solid #d7ddd1; border-left: 3px solid #9b4f35; border-radius: 3px; padding: 0.85rem 1.15rem; margin-bottom: 1.5rem;">
            <p style="margin: 0; font: 0.88rem/1.5 'Trebuchet MS', sans-serif; color: #35483e;">
                📌 <strong>Session Journal Notice:</strong> For this preview, your observations are stored in your current browser session (<code>st.session_state</code>).
                To keep a permanent copy of your records, click <strong>Download My Sightings (CSV)</strong> below before ending your session.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Prepare species options from data/birds.json
    species_list = birds or []
    species_map: Dict[str, Dict[str, str]] = {}
    for b in species_list:
        common = b.get("common_name", "")
        sci = b.get("scientific_name", "")
        bird_id = b.get("id", "")
        label = f"{common} ({sci})" if sci else common
        species_map[label] = {
            "common_name": common,
            "scientific_name": sci,
            "bird_id": bird_id,
        }

    # Add option for other species not in the curated 8
    species_map["Other / Unidentified Bird"] = {
        "common_name": "Other / Unidentified Bird",
        "scientific_name": "",
        "bird_id": "",
    }
    species_options = list(species_map.keys())

    # Form to record a new sighting
    st.markdown(
        """
        <div style="margin-bottom: 0.75rem;">
            <h3 style="color: #214b3b; font-family: Georgia, serif; font-size: 1.35rem; margin: 0 0 0.25rem;">
                Log a Bird Sighting
            </h3>
            <p style="color: #35483e; font-size: 0.93rem; margin: 0; font-family: 'Trebuchet MS', sans-serif;">
                Record details of your recent bird encounter. No exact home address is required.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form(key="record_sighting_form", clear_on_submit=True):
        col_species, col_date = st.columns([3, 2])
        with col_species:
            selected_species_label = st.selectbox(
                "Bird species",
                options=species_options,
                index=0,
                key="sighting_species_select",
                help="Choose a species from the regional bird guide or select 'Other'.",
            )

        with col_date:
            date_observed = st.date_input(
                "Date observed",
                value=datetime.date.today(),
                max_value=datetime.date.today(),
                key="sighting_date_input",
                help="Date when you observed this bird.",
            )

        col_count, col_notes = st.columns([1, 3])
        with col_count:
            count_observed = st.number_input(
                "Number observed",
                min_value=1,
                value=1,
                step=1,
                key="sighting_count_input",
                help="Number of individual birds spotted (positive whole number).",
            )

        with col_notes:
            notes_observed = st.text_area(
                "Observation notes (optional)",
                value="",
                placeholder="e.g., Pair feeding on balcony railing, visited shallow water dish at dawn, singing from nearby neem tree...",
                max_chars=350,
                key="sighting_notes_input",
                help="Note behaviors, perch spots, time of day, or weather in general terms.",
            )

        submitted = st.form_submit_button(
            "Save Sighting",
            use_container_width=True,
        )

    # Process Form Submission
    if submitted:
        if not selected_species_label:
            st.error("Please select a bird species.")
        elif count_observed < 1:
            st.error("Please enter a valid count of at least 1 bird.")
        else:
            meta = species_map.get(selected_species_label, {
                "common_name": selected_species_label,
                "scientific_name": "",
                "bird_id": "",
            })
            new_sighting = {
                "id": f"obs-{len(st.session_state.sightings) + 1}-{int(datetime.datetime.now().timestamp())}",
                "common_name": meta["common_name"],
                "scientific_name": meta["scientific_name"],
                "bird_id": meta["bird_id"],
                "date": date_observed.strftime("%Y-%m-%d"),
                "count": int(count_observed),
                "notes": notes_observed.strip() if notes_observed else "",
                "recorded_at": datetime.datetime.now().isoformat(),
            }
            st.session_state.sightings.append(new_sighting)
            st.success(
                f"🌿 **Saved sighting:** {int(count_observed)} × {meta['common_name']} "
                f"on {date_observed.strftime('%d %b %Y')} recorded in your field journal!"
            )

    st.write("")
    st.write("")

    # ==========================================================================
    # View the Sightings Journal
    # ==========================================================================
    sightings = st.session_state.sightings
    total_count = len(sightings)

    # Sort most recent first: by observation date, then recorded_at timestamp
    sorted_sightings = sorted(
        sightings,
        key=lambda s: (s.get("date", ""), s.get("recorded_at", "")),
        reverse=True,
    )

    # Journal Bar: Heading & CSV Export Button
    col_journal_title, col_journal_export = st.columns([3, 2])
    with col_journal_title:
        st.markdown(
            f"""
            <div style="padding-top: 0.35rem;">
                <h2 style="color: #214b3b; font-family: Georgia, serif; font-size: 1.55rem; margin: 0;">
                    Journal Observations ({total_count})
                </h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_journal_export:
        if total_count > 0:
            csv_data = generate_sightings_csv(sorted_sightings)
            st.download_button(
                label="📥 Download My Sightings (CSV)",
                data=csv_data,
                file_name="wingscape_sightings.csv",
                mime="text/csv",
                key="btn_download_sightings_csv",
                use_container_width=True,
            )
        else:
            st.download_button(
                label="📥 Download My Sightings (CSV)",
                data="",
                file_name="wingscape_sightings.csv",
                mime="text/csv",
                key="btn_download_sightings_csv_disabled",
                disabled=True,
                help="Log at least one sighting to enable CSV export.",
                use_container_width=True,
            )

    st.write("")

    # Display Sightings or Empty State
    if total_count == 0:
        st.markdown(
            """
            <div class="empty-search-box">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📖</div>
                <h3>Your Field Journal is Empty</h3>
                <p>You haven't recorded any bird sightings yet in this session.</p>
                <p style="color: #6d7a72; font-size: 0.92rem;">
                    Step out on your balcony, take five minutes to notice the birds around you,
                    and log your first observation above!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        for item in sorted_sightings:
            common = html.escape(item.get("common_name", "Unknown Bird"))
            sci = html.escape(item.get("scientific_name", ""))
            date_raw = item.get("date", "")
            try:
                dt = datetime.datetime.strptime(date_raw, "%Y-%m-%d")
                formatted_date = dt.strftime("%d %b %Y")
            except Exception:
                formatted_date = html.escape(date_raw)

            count = item.get("count", 1)
            bird_id = item.get("bird_id", "")
            emblem = DEFAULT_EMBLEMS.get(bird_id, "🌿")
            count_label = f"{count} {'bird' if count == 1 else 'birds'}"
            notes = item.get("notes", "")

            sci_html = (
                f'<span class="sighting-scientific-name">({sci})</span>'
                if sci
                else ""
            )

            notes_html = (
                f'<div class="sighting-notes-text">📝 <em>"{html.escape(notes)}"</em></div>'
                if notes
                else ""
            )

            st.markdown(
                f"""
                <div class="sighting-card">
                    <div class="sighting-card-top">
                        <span class="sighting-date-tag">📅 {formatted_date}</span>
                        <span class="sighting-count-chip">{emblem} {count_label}</span>
                    </div>
                    <h3 class="sighting-species-name">
                        {common} {sci_html}
                    </h3>
                    {notes_html}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Clear session journal option in an expander at the bottom
        with st.expander("⚙️ Journal Management", expanded=False):
            st.caption("Resetting will clear observations recorded during this session.")
            st.button(
                "Clear all session sightings",
                key="btn_clear_all_sightings",
                on_click=clear_all_sightings,
            )

    # Footer
    st.markdown(
        """
        <footer class="page-footer" style="margin-top: 2.5rem;">
          Wingscape · Small steps towards a more bird-friendly world.
        </footer>
        """,
        unsafe_allow_html=True,
    )
