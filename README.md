# 🌿 Wingscape — Discover. Observe. Welcome.

**Bring nature closer to home.**

Wingscape is a nature-inspired web application that encourages people living in cities and apartments to discover local birds, make their balconies more bird-friendly, and build a habit of observing the natural world around them.

🔗 **Live Demo:** [https://wingscape.streamlit.app](https://wingscape.streamlit.app)  
💻 **GitHub Repository:** [sanjay067-cse/Wingscape](https://github.com/sanjay067-cse/Wingscape)

---

## 🌱 About the Project

Living in a city doesn't mean being disconnected from nature. Birds visit balconies, neighborhood gardens, rooftops, and nearby trees every day, but we often overlook them.

Wingscape aims to make these small encounters easier to notice and more meaningful.

It combines a curated guide to common Indian urban birds, an AI-powered balcony planning assistant, and a personal bird-sighting journal in one simple, interactive application.

The goal is simple: **help people discover the wildlife already around them and take small, responsible steps to welcome it.**

## ✨ Features

### 🐦 1. Discover Birds

Explore eight common bird species found in Indian urban environments.

- Browse bird profiles with common and scientific names.
- View photographs with photographer credits and license information.
- Search by common or scientific name.
- Learn identifying characteristics and habitat information.
- Read responsible bird-observation tips.
- Navigate between the homepage and bird guide.

**Species included:**
- House Sparrow (*Passer domesticus*)
- Common Myna (*Acridotheres tristis*)
- Rock Pigeon (*Columba livia*)
- Rose-ringed Parakeet (*Psittacula krameri*)
- Red-vented Bulbul (*Pycnonotus cafer*)
- Oriental Magpie-Robin (*Copsychus saularis*)
- Purple Sunbird (*Cinnyris asiaticus*)
- Indian Peafowl (*Pavo cristatus*)

Bird information and image attribution metadata are maintained in `data/birds.json`. Photographs are credited to their respective contributors, with license details provided in the application.

### 🌿 2. AI Balcony Coach

Get personalized suggestions for making a balcony more welcoming to birds.

The AI Balcony Coach uses a language model accessed through the Groq API to generate a balcony plan based on the user's preferences.

Users can provide details such as:
- Balcony size.
- Sunlight availability.
- Existing plants and balcony conditions.
- Budget and goals.
- Additional preferences for the balcony.

The coach generates a tailored plan and allows users to adjust their preferences or create another plan.

The recommendations aim to encourage bird-friendly practices that are practical for urban living.

**Technology:** Groq API with the `openai/gpt-oss-20b` model.

The AI-generated suggestions are intended as general guidance. Users should verify plant safety, local wildlife guidance, and building rules before making changes.

### 📔 3. My Sightings

Keep a simple record of birds observed during everyday life.

- Select a species from the existing bird dataset.
- Record the observation date.
- Enter the number of birds observed.
- Add optional notes about the observation.
- View recorded sightings in a journal.
- Download observations as a CSV file.

The CSV export can be opened in spreadsheet applications such as Microsoft Excel and Google Sheets.

**Storage note:** The current version stores sightings in Streamlit session state. Records are temporary and may be lost when the session ends or resets. Download the CSV to keep a copy of your observations.

### 🌳 4. Daily Outdoor Mission

The homepage features a short, five-minute outdoor observation mission that encourages users to slow down, look closely, and notice the nature around them.

Wingscape is designed to make nature observation feel approachable, even for people who have limited access to green spaces.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web application and user interface |
| Groq API | Access to the language model for AI balcony planning |
| `openai/gpt-oss-20b` | Model used by the AI Balcony Coach |
| JSON | Structured bird species data and image metadata |
| CSV | Exporting bird-sighting records |
| Git and GitHub | Version control and source-code hosting |
| Streamlit Community Cloud | Public application deployment |

---

## 🚀 Try the Live Application

Visit **[Wingscape](https://wingscape.streamlit.app)** and explore the three main sections:

1. Open **Discover Birds** to explore species and search for a bird.
2. Visit **AI Balcony Coach** to generate a personalized balcony plan.
3. Open **My Sightings** to record an observation and download the journal as a CSV.

No local installation is required to try the deployed application. The AI Balcony Coach depends on the availability and usage limits of the configured API service.

---

## 💻 Run Wingscape Locally

You can run the application on your own computer using Python and Streamlit.

### Prerequisites

- Python 3.13 recommended.
- Git.
- A Groq API key for the AI Balcony Coach.

### 1. Clone the repository

```bash
git clone https://github.com/sanjay067-cse/Wingscape.git
cd Wingscape
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a directory named `.streamlit` in the project root if it doesn't already exist.

Inside that directory, create a file named `secrets.toml`:

```toml
GROQ_API_KEY = "YOUR_ACTUAL_GROQ_API_KEY"
```

Replace the placeholder with your own Groq API key. You can obtain an API key through the [Groq Console](https://console.groq.com/).

**Security:** Never commit your actual API key to GitHub, include it in screenshots, or share it publicly. The repository's `.gitignore` excludes `.streamlit/secrets.toml`.

### 5. Start the application

```bash
python -m streamlit run app.py
```

Open the local URL printed in your terminal, usually:

`http://localhost:8501`

---

## 📁 Project Structure

```text
Wingscape/
├── app.py                  # Main Streamlit application and navigation
├── balcony_coach.py        # AI Balcony Coach functionality
├── bird_details.py         # Bird detail rendering helper
├── sightings.py            # My Sightings journal and CSV export
├── data/
│   └── birds.json          # Bird species information and image metadata
├── requirements.txt        # Python dependencies
├── .gitignore              # Excludes local secrets and generated files
└── README.md               # Project documentation
```

The `.streamlit/secrets.toml` file is created locally and is intentionally excluded from version control.

---

## 🔐 API Configuration and Security

The AI Balcony Coach requires a valid Groq API key.

- Store the key in `.streamlit/secrets.toml` for local development.
- Configure the same secret in the **Secrets** settings of Streamlit Community Cloud for the deployed application.
- Never hardcode the key in Python files.
- Never commit API credentials to the repository.
- Monitor your API provider's usage limits and account settings.

The public application uses the configured API credentials when users request AI-generated balcony plans. API availability and usage limits may affect this feature.

---

## ⚠️ Current Limitations

Wingscape is an evolving project. The current version has the following limitations:

- The bird guide covers eight curated species rather than every bird found in India.
- The AI Balcony Coach provides general suggestions and does not guarantee that every recommendation is suitable for every location or species.
- My Sightings uses temporary session storage; it does not yet provide a permanent, account-based journal.
- The application does not currently identify birds automatically from photographs or audio recordings.
- AI functionality depends on the external API service and its usage limits.

These limitations provide opportunities for future development.

---

## 🗺️ Future Improvements

Potential improvements include:

- Expanding the bird guide with more regional species.
- Adding permanent storage for bird sightings.
- Introducing optional filters and statistics for observation history.
- Improving accessibility and mobile usability.
- Adding more locally relevant, responsible bird-welcoming resources.
- Exploring additional educational activities and observation challenges.

These are possible future directions, not features currently promised by the application.

---

## 🌍 Responsible Bird-Friendly Practices

Wingscape encourages observing birds without disturbing them.

- Keep clean water available where appropriate and safe.
- Choose locally appropriate, bird-friendly plants.
- Avoid pesticides and harmful chemicals.
- Keep water containers clean and refreshed.
- Avoid disturbing nests or handling wild birds.
- Follow local wildlife regulations and residential building rules.

Small, thoughtful actions can help make urban environments more welcoming to wildlife.

---

## 📷 Photo Credits

Bird photographs displayed in Wingscape are sourced from Wikimedia Commons. Photographer names and license information are maintained alongside the image metadata and displayed in the bird guide.

Please refer to the attribution shown in the application for the applicable image and license details.

---

## 👩‍💻 Author

**Sanjay Kumar Mahto**

Wingscape is a personal project exploring how technology can encourage people to connect with the natural world around them.

- **GitHub:** [@sanjay067-cse](https://github.com/sanjay067-cse)
- **Project repository:** [Wingscape](https://github.com/sanjay067-cse/Wingscape)
- **Live application:** [wingscape.streamlit.app](https://wingscape.streamlit.app)

---

## 📄 License

A project-level license has not yet been specified. The licenses for third-party photographs and other external resources remain separate and should be followed according to their individual terms.

---

**Wingscape — Discover. Observe. Welcome.** 🌿