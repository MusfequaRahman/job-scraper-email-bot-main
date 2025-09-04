from flask import Flask, request, render_template_string
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import uuid
import chromadb

# --- Initialize Flask ---
app = Flask(__name__)

# --- Initialize LLM ---
llm = ChatGroq(
    temperature=0,
    groq_api_key="",   # <-- replace with your Groq API key
    model="llama-3.3-70b-versatile"
)

# --- Setup Chroma VectorDB (Portfolio) ---
df = pd.read_csv("my_portfolio.csv")  # Ensure this file exists in project root
client = chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name="portfolio")

if not collection.count():
    for _, row in df.iterrows():
        collection.add(
            documents=[row["Techstack"]],
            metadatas={"links": row["Links"]},
            ids=[str(uuid.uuid4())]
        )

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    email_content = ""
    portfolio_links = []

    if request.method == "POST":
        url = request.form.get("url")

        # --- Scrape Website ---
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        # --- Extract Job Postings ---
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            Extract the job postings and return JSON with:
            - role
            - experience
            - skills
            - description
            Only return valid JSON.
            """
        )
        chain_extract = prompt_extract | llm
        res = chain_extract.invoke(input={'page_data': page_data})

        json_parser = JsonOutputParser()
        json_res = []
        try:
            json_res = json_parser.parse(res.content)
        except:
            pass

        # --- Find Relevant Portfolio Links ---
        links = []
        if json_res:
            for job in json_res:
                query_text = f"{job.get('role', '')} {job.get('description', '')}".strip()
                if query_text:
                    result = collection.query(query_texts=[query_text], n_results=2).get('metadatas', [])
                    links.extend(result)

            # --- Generate Cold Email ---
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}

                ### INSTRUCTION:
                You are Md. Al-Mamun Provath, a Business Development Executive at NovaTech AI.  
                NovaTech AI is an AI & Software Consulting company dedicated to facilitating 
                seamless integration of business processes through automated tools.  
                We empower enterprises with tailored solutions, fostering scalability, 
                process optimization, cost reduction, and heightened efficiency.

                Write a professional cold email to the client.  
                Include the most relevant portfolio links from {link_list}.  

                Structure:
                - Subject Line
                - Greeting
                - Intro + About NovaTech AI
                - Relevant Experience (with clickable portfolio links)
                - Call to Action
                - Signature
                """
            )
            chain_email = prompt_email | llm

            job = json_res[0]
            res = chain_email.invoke({"job_description": str(job), "link_list": links})
            email_content = res.content
            portfolio_links = links

    # --- Render HTML ---
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cold Email Assistant</title>
        <style>
            body { font-family: Segoe UI, Arial, sans-serif; background:#f4f6f9; margin:0; padding:20px; }
            .container { max-width:900px; margin:auto; background:#fff; padding:20px; border-radius:12px;
                         box-shadow:0 4px 12px rgba(0,0,0,0.1); }
            h1 { color:#007BFF; }
            form { margin-bottom:20px; }
            input[type=text] { width:70%; padding:10px; border:1px solid #ccc; border-radius:6px; }
            button { padding:10px 18px; background:#007BFF; color:white; border:none; border-radius:6px; cursor:pointer; }
            button:hover { background:#0056b3; }
            .email-box { padding:20px; border:1px solid #ddd; border-radius:8px; margin-top:20px; background:#fafafa; }
            .portfolio { display:flex; flex-wrap:wrap; gap:10px; margin-top:10px; }
            .portfolio a { text-decoration:none; }
            .portfolio div { padding:12px 18px; background:#fff; border:1px solid #ddd; border-radius:8px;
                             box-shadow:0 2px 6px rgba(0,0,0,0.05); color:#007BFF; font-weight:bold;
                             transition:all 0.2s; }
            .portfolio div:hover { background:#007BFF; color:white; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Cold Email Assistant</h1>
            <form method="post">
                <input type="text" name="url" placeholder="Enter job listing link" required>
                <button type="submit">Generate Email</button>
            </form>

            {% if email_content %}
            <div class="email-box">
                <h2>📧 Cold Email Draft</h2>
                <p>{{ email_content | safe }}</p>
                <h3>🔗 Portfolio Links</h3>
                <div class="portfolio">
                    {% for group in portfolio_links %}
                        {% for l in group %}
                            {% if "links" in l %}
                                <a href="{{ l['links'] }}" target="_blank">
                                    <div>View Portfolio</div>
                                </a>
                            {% endif %}
                        {% endfor %}
                    {% endfor %}
                </div>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    """
    return render_template_string(template, email_content=email_content, portfolio_links=portfolio_links)


if __name__ == "__main__":
    app.run(debug=True, port=5000)