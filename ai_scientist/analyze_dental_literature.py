import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import requests
import PyPDF2
from ai_scientist.llm import get_response_from_llm, extract_json_between_markers
import json

load_dotenv(override=True)

dental_review_system_prompt = """You are an expert AI researcher specializing in dental implant research analysis with a comprehensive understanding of oral and maxillofacial biology, biomaterials, and clinical dentistry. Your task is to conduct a rigorous, multifaceted critical analysis of dental implant research papers."""

dental_review_prompt = """Analyze the following dental implant research paper. Provide a detailed analysis addressing each of these points:

1. Methodological Rigor:
   - Study design and its appropriateness
   - Sample size, power calculations, and statistical analyses
   - Inclusion/exclusion criteria and their impact
   - Validity and reliability of measurement tools

2. Research Ethics and Reporting:
   - Compliance with ethical guidelines
   - Adherence to reporting guidelines
   - Disclosure of conflicts of interest and funding

3. Clinical Relevance and Applicability:
   - Relevance to current clinical practice and patient needs
   - Generalizability of findings
   - Potential impact on clinical decision-making

4. Scientific Novelty and Contribution:
   - Originality of the research
   - Addressing gaps in current literature

5. Technical Aspects of Dental Implantology:
   - Appropriateness of implant systems and techniques
   - Consideration of biomechanical principles
   - Use of advanced technologies

6. Long-term Outcomes and Follow-up:
   - Duration and quality of follow-up periods
   - Comprehensiveness of outcome measures

7. Biological Considerations:
   - Consideration of host factors
   - Assessment of peri-implant tissue health

8. Interdisciplinary Approach:
   - Integration of various dental specialties
   - Collaboration with relevant medical fields

9. Data Presentation and Interpretation:
   - Clarity and accuracy of data presentation
   - Authors' interpretation of results
   - Strength of conclusions

10. Future Research Directions:
    - Identified gaps warranting further investigation
    - Suggested follow-up studies or approaches

11. Overall Assessment:
    - Quality, validity, and significance of the research
    - Recommendation for publication (accept, revise, reject)

Paper text:
{text}

Provide a detailed analysis in JSON format, with a section for each of the above points. Be comprehensive, objective, and evidence-based in your analysis."""

def load_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def analyze_dental_paper(text, model, client):
    response, _ = get_response_from_llm(
        dental_review_prompt.format(text=text),
        client=client,
        model=model,
        system_message=dental_review_system_prompt,
        print_debug=False,
        max_tokens=4000
    )
    return extract_json_between_markers(response)

def json_to_markdown(json_data):
    md = "# Comprehensive Dental Implant Research Analysis 🦷🔬\n\n"
    
    emojis = {
        "Methodological Rigor": "📊",
        "Research Ethics and Reporting": "🔬",
        "Clinical Relevance and Applicability": "👨‍⚕️",
        "Scientific Novelty and Contribution": "💡",
        "Technical Aspects of Dental Implantology": "🦿",
        "Long-term Outcomes and Follow-up": "📅",
        "Biological Considerations": "🧬",
        "Interdisciplinary Approach": "🤝",
        "Data Presentation and Interpretation": "📈",
        "Future Research Directions": "🔮",
        "Overall Assessment": "🏆"
    }
    
    for section, content in json_data.items():
        md += f"## {emojis.get(section, '')} {section}\n\n"
        if isinstance(content, dict):
            for subsection, details in content.items():
                md += f"### {subsection}\n\n"
                if isinstance(details, dict):
                    for key, value in details.items():
                        md += f"**{key}:** {value}\n\n"
                else:
                    md += f"{details}\n\n"
        else:
            md += f"{content}\n\n"
    
    return md

def main(pdf_path, out_dir, model, client):
    print(f"Analyzing: {os.path.basename(pdf_path)}")
    
    print("Loading PDF...")
    paper_text = load_pdf(pdf_path)

    print("Analyzing paper...")
    analysis_json = analyze_dental_paper(paper_text, model, client)

    print("Saving results...")
    os.makedirs(out_dir, exist_ok=True)
    json_output_file = os.path.join(out_dir, f'analysis_{os.path.basename(pdf_path)}.json')
    with open(json_output_file, 'w') as f:
        json.dump(analysis_json, f, indent=2)

    md_output = json_to_markdown(analysis_json)
    md_output_dir = "/Users/franciscoteixeirabarbosa/Dropbox/Random scripts/The AI Scientist/results_in_md"
    os.makedirs(md_output_dir, exist_ok=True)
    md_output_file = os.path.join(md_output_dir, f'analysis_{os.path.basename(pdf_path)}.md')
    with open(md_output_file, 'w') as f:
        f.write(md_output)

    print(f"Analysis complete. Results saved to:")
    print(f"JSON: {json_output_file}")
    print(f"Markdown: {md_output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf_path', type=str, required=True)
    parser.add_argument('--out_dir', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    args = parser.parse_args()
    
    if args.model.startswith("gpt"):
        client = OpenAI()
    elif args.model.startswith("claude"):
        client = anthropic.Anthropic()
    else:
        raise ValueError(f"Unsupported model: {args.model}")
    
    main(args.pdf_path, args.out_dir, args.model, client)