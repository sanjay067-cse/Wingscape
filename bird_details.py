import streamlit as st


def render_bird_details(bird: dict) -> None:
    """Render identifying characteristics, habitat, and observation tips using native Streamlit components."""
    st.markdown("**Identifying Characteristics**")
    traits = bird.get("identifying_characteristics", [])
    if traits:
        bullet_list = "\n".join(f"- {trait}" for trait in traits)
        st.markdown(bullet_list)

    st.markdown("**Typical Habitat**")
    habitat = bird.get("habitat", "")
    if habitat:
        st.write(habitat)

    tip = bird.get("observation_tip", "")
    if tip:
        st.info(f"**Responsible Observation Tip**\n\n{tip}", icon="🌿")

    image_meta = bird.get("image", {})
    if image_meta and image_meta.get("url"):
        photographer = image_meta.get("photographer", "Wikimedia Contributor")
        source_url = image_meta.get("source_url", "#")
        license_name = image_meta.get("license", "Creative Commons")
        st.caption(
            f"📷 **Photograph:** [{photographer}]({source_url}) · Licensed under {license_name}"
        )
