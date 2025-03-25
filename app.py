from flask import Flask, render_template, request, flash
import os
from ChatGPT.DeepResearch.deep_research_openai import generate_deep_research_prompt_web
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-for-testing')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        # Get form data
        topic = request.form.get('topic', '').strip()
        report_lang = request.form.get('report_lang', '').strip()
        search_lang = request.form.get('search_lang', '').strip()
        depth = request.form.get('depth', '').strip()
        source_type = request.form.get('source_type', '').strip()
        year_cutoff = request.form.get('year_cutoff', '').strip()
        keywords = request.form.get('keywords', '').strip()
        files_included = request.form.get('files_included', 'no').lower() == 'yes'
        banality = request.form.get('banality', '').strip()
        
        # Form validation
        if not topic:
            flash('Please enter a research topic')
            return render_template('home.html')
        
        # Generate prompt
        prompt = generate_deep_research_prompt_web(
            topic, report_lang, search_lang, depth, source_type, 
            year_cutoff, keywords, files_included, banality
        )
        
        return render_template('home.html', prompt=prompt, 
                              form_data=request.form)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
