# 🌿 Wingscape

**Discover. Observe. Welcome.**

Wingscape is an open-source, nature-inspired project designed to help apartment residents discover local birds, make their balconies more bird-friendly, and spend more time observing the natural world.

## The Problem

People living in cities and apartments may have limited access to gardens and green spaces. They can miss the wildlife around them or may not know how to make their balconies safer and more welcoming for birds.

Wingscape aims to make discovering and observing urban birds easier and more accessible.

## Project Goals

- **Discover Birds:** Explore a curated guide to birds found in the selected region.
- **Balcony Coach:** Get personalized, practical suggestions for creating a bird-friendly balcony.
- **My Sightings:** Record and revisit personal bird observations.
- **Touch Grass:** Encourage short, meaningful outdoor observation activities.

## Open-Source AI

Wingscape is being developed with the goal of making open-weight AI a meaningful part of the experience.

The planned AI Balcony Coach will use an open-weight language model to personalize suggestions based on balcony conditions and curated bird-friendly guidance.

The AI integration is under development. Model selection, licensing, performance, and recommendation quality will be evaluated before it is considered complete.

## Technology Stack

- Python
- Streamlit
- Git and GitHub

Planned additions include a local SQLite database and a locally running open-weight AI model.

## Current Status

The initial Streamlit homepage is working. The bird guide, sightings journal, and AI Balcony Coach are planned features and are not yet fully implemented.

## Getting Started

### Prerequisites

- Python 3.13 or another compatible Python version
- Git

### Installation

1. Clone this repository or download the project source.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

5. Start Wingscape:

```powershell
python -m streamlit run app.py
```

6. Open the local URL displayed in your terminal.

## Responsible Bird Observation

Wingscape aims to encourage respectful wildlife observation. Users should avoid disturbing nests, handling wild birds, or using practices that could harm them.

AI-generated guidance will need to be checked against reliable, regionally appropriate sources.

## Project Roadmap

- [x] Initial Streamlit homepage
- [x] Basic project setup
- [ ] Curated regional bird guide
- [ ] Persistent sightings journal
- [ ] Open-weight AI Balcony Coach
- [ ] Testing, documentation, and demonstration

## Contributing

Contributions and suggestions are welcome. Please discuss substantial changes before implementing them.

## License

The project license will be selected and added before public release.
