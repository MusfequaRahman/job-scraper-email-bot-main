# 🚀 AI Cold Email Generator

**AI-powered cold email generator that matches job requirements with your portfolio projects**

<img width="1184" height="694" alt="1" src="https://github.com/user-attachments/assets/785d44ba-07ac-47cd-a656-fb41688cbbd3" />
<img width="571" height="218" alt="4" src="https://github.com/user-attachments/assets/b5d514b1-fa0f-4bfb-95e7-603393c0da49" />
<img width="554" height="798" alt="3" src="https://github.com/user-attachments/assets/9677a357-a4a7-4a75-b0e4-96e4b882151b" />
<img width="1149" height="534" alt="2" src="https://github.com/user-attachments/assets/0562f8ef-2004-4eb3-845d-81762a58ef5e" />


![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.0.0-green.svg)
![LangChain](https://img.shields.io/badge/langchain-latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 🔍 **Smart Job Scraping**: Automatically extracts job requirements from any job listing URL
- 🤖 **AI-Powered Analysis**: Uses Groq's LLaMA model to understand job postings and requirements
- 📊 **Portfolio Matching**: Vector database finds your most relevant projects for each job
- ✉️ **Professional Email Generation**: Creates personalized cold emails with proper business formatting
- 🎯 **Tech Stack Alignment**: Matches job requirements with your specific technology experience
- 🌐 **Clean Web Interface**: Modern, responsive UI for easy interaction
- 💾 **Persistent Storage**: ChromaDB vector database for efficient project matching

## 🎥 Demo

```
📧 Input: https://jobs.company.com/python-developer
🤖 AI Analysis: Extracts role, skills, experience requirements
📊 Matching: Finds relevant Python/Flask projects from your portfolio
✉️ Output: Professional cold email with portfolio links
```

## 🛠️ Tech Stack

- **Backend**: Flask, Python 3.8+
- **AI/ML**: LangChain, Groq API (LLaMA 3.3)
- **Database**: ChromaDB (Vector Database)
- **Web Scraping**: WebBaseLoader, BeautifulSoup
- **Data Processing**: Pandas
- **Frontend**: HTML5, CSS3, JavaScript

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get it here](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-cold-email-generator.git
   cd ai-cold-email-generator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup API Key**
   ```python
   # In app.py, replace with your Groq API key
   groq_api_key="your_groq_api_key_here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
ai-cold-email-generator/
├── app.py                  # Main Flask application
├── my_portfolio.csv        # Your portfolio projects data
├── requirements.txt        # Python dependencies
├── vectorstore/           # ChromaDB vector database (auto-created)
├── README.md              # Project documentation
└── static/                # Static files (if any)
```

## 📊 Portfolio Data Format

Your `my_portfolio.csv` should follow this structure:

```csv
Techstack,Links
"Python, Flask, PostgreSQL",https://github.com/yourname/project1
"Java, Spring Boot, MySQL",https://github.com/yourname/project2
"React, Node.js, MongoDB",https://github.com/yourname/project3
```

## 🎯 How It Works

1. **Job URL Input**: Enter any job listing URL
2. **Web Scraping**: Application scrapes the job posting content
3. **AI Analysis**: LLaMA model extracts job requirements (role, skills, experience)
4. **Vector Matching**: ChromaDB finds most relevant portfolio projects
5. **Email Generation**: AI creates personalized cold email with portfolio links
6. **Professional Output**: Clean, business-ready email with call-to-action

## 📝 Example Output

```
Subject: Expert Python Developer Solutions from NovaTech AI

Dear Hiring Manager,

I hope this email finds you well. I'm Md. Al-Mamun Provath, Business Development Executive at NovaTech AI, reaching out regarding your Senior Python Developer position.

NovaTech AI is a leading AI & Software Consulting company dedicated to facilitating seamless integration of business processes through automated tools...

Based on your requirements for Python, Flask, PostgreSQL, here are relevant projects:
1. Flask Application with PostgreSQL - https://portfolio.com/project2
2. Python Data Pipeline - https://portfolio.com/project8

Best regards,
Md. Al-Mamun Provath
```

## ⚙️ Configuration

### Environment Variables
```bash
# Optional: Set via environment variables
export GROQ_API_KEY="your_api_key_here"
export FLASK_ENV="development"
export FLASK_DEBUG=True
```

### Customization
- **Email Template**: Modify the email generation prompt in `app.py`
- **Portfolio Data**: Update `my_portfolio.csv` with your projects
- **Matching Algorithm**: Adjust vector search parameters in ChromaDB queries
- **UI Styling**: Customize the HTML template in the Flask route

## 🔧 API Endpoints

- `GET /` - Main application interface
- `POST /` - Process job URL and generate email

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Roadmap

- [ ] Multiple email templates for different industries
- [ ] Bulk job processing
- [ ] Email scheduling and tracking
- [ ] Integration with job boards APIs
- [ ] Chrome extension for one-click email generation
- [ ] Advanced analytics and success metrics

## 🐛 Troubleshooting

### Common Issues

**ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**API Key Error**
```bash
# Ensure your Groq API key is valid and has credits
# Check at https://console.groq.com
```

**CSV Reading Error**
```bash
# Ensure my_portfolio.csv is in the project root directory
# Check CSV format matches the expected structure
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- [Groq](https://groq.com/) for the powerful LLaMA API
- [LangChain](https://langchain.com/) for the AI framework
- [ChromaDB](https://www.trychroma.com/) for vector database functionality
- [Flask](https://flask.palletsprojects.com/) for the web framework



