# 🚀 AI Career Copilot

**An AI-powered career guidance platform that helps users analyze their resumes, identify missing skills, create personalized learning roadmaps, and prepare for interviews.**

\<p align="center">
&#x20; \<a href="[https://ai-career-copilot-h2wf.onrender.com/](https://ai-career-copilot-h2wf.onrender.com/)">
&#x20;   \<strong>🌐 Live Application\</strong>
&#x20; \</a>
\</p>

---

## 📌 Overview

AI Career Copilot is a web application designed to help students, freshers, and aspiring professionals understand their current skill sets and plan their career development more effectively.

By combining Artificial Intelligence with resume analysis, the platform evaluates a user's resume against their career goals and provides personalized recommendations to support their professional growth.

The application uses Google's Gemini AI to generate career-oriented insights and provides a web interface for managing user accounts, analyzing resumes, and accessing previous reports.

## ✨ Features

- **📄 Resume Analysis:** Upload a resume or provide resume text for AI-powered analysis.
- **🎯 Career Goal-Based Evaluation:** Analyze skills according to a user's selected career goal or target role.
- **🧠 Skill Identification:** Identify relevant skills already present in the resume.
- **📊 Skill Gap Analysis:** Discover important skills that may be missing for the target role.
- **🛣️ Personalized Learning Roadmap:** Generate a roadmap focused on developing missing skills.
- **🎤 Interview Preparation:** Generate interview questions relevant to the user's career goal.
- **🔐 User Authentication:** Sign-up and login functionality.
- **📚 Report History:** Store and revisit previous resume analysis reports.
- **☁️ Cloud Deployment:** Access the application through its live deployment.

## 🛠️ Technology Stack

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| Python            | Core programming language   |
| Flask             | Web application and routing |
| Google Gemini API | AI-powered resume analysis  |
| SQLAlchemy        | Database ORM                |
| TiDB Cloud        | Cloud-hosted SQL database   |
| PyPDF2            | PDF text extraction         |
| python-docx       | Word document processing    |
| HTML5 & CSS3      | User interface and styling  |
| Gunicorn          | Production WSGI server      |
| Render            | Application hosting         |

## ⚙️ How It Works

1. **Create an account:** Register and log in to the application.
2. **Set a career goal:** Specify the role or career path you want to pursue.
3. **Provide your resume:** Upload a supported resume file or enter resume text.
4. **Analyze your profile:** Gemini AI evaluates your resume in relation to your career goal.
5. **Review the results:** Explore relevant skills, missing skills, a learning roadmap, and interview questions.
6. **Revisit previous reports:** Access saved analysis reports through the application's history functionality.

## 🏗️ Project Structure

```text
ai-career-copilot/
│
├── app.py              # Flask application and routes
├── ai.py               # Gemini AI integration and analysis
├── db.py               # Database engine and session configuration
├── models.py           # SQLAlchemy database models
│
├── base.html            # Shared HTML template
├── login.html           # Login page
├── signup.html          # Registration page
├── dashboard.html       # Resume analysis dashboard
├── history.html         # Previous analysis reports
├── style.css            # Application styling
│
├── requirements.txt     # Python dependencies
├── .gitignore           # Git exclusion rules
└── README.md            # Project documentation
```

## 💻 Installation and Setup

Follow these steps to run the application locally.

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or a compatible version supported by the dependencies
- Git
- A Google Gemini API key
- A MySQL-compatible database, such as TiDB Cloud

### 1. Clone the repository

```bash
git clone https://github.com/sonarhrushikesh08-dot/ai-career-copilot.git
```

Navigate into the project directory:

```bash
cd ai-career-copilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory.

Add your configuration using the following template:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_connection_url
```

Replace the example values with your own credentials.

- Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).
- Configure `DATABASE_URL` using your database provider's connection details, including the required SSL settings where applicable.

**Important:** Never commit your `.env` file, database passwords, API keys, or other secrets to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local URL displayed by Flask in your browser. The default development address is usually:

```text
http://127.0.0.1:5000/
```

*Note: Ensure your database is accessible and the required environment variables are configured before starting the application.*

## ☁️ Live Deployment

The application is deployed using Render and connects to a cloud-hosted database.

🌐 **Live application:** [AI Career Copilot](https://ai-career-copilot-h2wf.onrender.com/)

Deployment configuration requires the appropriate environment variables to be configured in the hosting platform.

## 🔒 Security Considerations

- Store API keys and database credentials in environment variables.
- Do not expose secrets in source code or public repositories.
- Use secure password hashing rather than storing plain-text passwords.
- Configure Flask session secrets using a strong, environment-specific secret key.
- Enable HTTPS and appropriate session security settings in production.
- Validate uploaded files and handle user data securely.

## 🎯 Project Objectives

This project was developed to:

- Apply Generative AI to a practical career-development use case.
- Build an end-to-end web application using Flask and Python.
- Integrate an external AI API into a backend application.
- Work with relational databases and ORM-based data management.
- Gain practical experience in deployment, configuration, and debugging.
- Make personalized career guidance more accessible to students and aspiring professionals.

## 🚀 Future Enhancements

Potential areas for future development include:

- Resume scoring and ATS compatibility analysis.
- Job description matching and skill comparison.
- Resume improvement suggestions tailored to specific roles.
- Interactive mock interviews with AI-generated feedback.
- Downloadable career analysis reports.
- Expanded career paths and personalized learning recommendations.
- Enhanced authentication and user data security.

## 👨‍💻 Author

**Hrushikesh Sonar**

Engineering student | Python Developer | AI & Machine Learning Enthusiast

- GitHub: [@sonarhrushikesh08-dot](https://github.com/sonarhrushikesh08-dot)
- LinkedIn: [Hrushikesh Sonar](https://www.linkedin.com/in/hrushikesh-sonar-93b272345/)

##

---

**Built with Python, Flask, and Gemini AI — turning career goals into actionable learning plans.** 🚀
