import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import requests
import PyPDF2

load_dotenv(override=True)

def load_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def analyze_paper(text, model, client):
    prompt = """
    Analyze the following dental implant research paper. Identify:
    1. Potential gaps in the research
    2. Controversies or conflicting results
    3. Possible conflicts of interest
    4. Biases in the study design or interpretation
    5. Methodological weaknesses
    6. Misinterpretation of data
    7. Overall strengths and weaknesses of the study

    Paper text:
    {text}

    Provide a detailed analysis addressing each of the above points.
    """

    if isinstance(client, OpenAI):
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert in dental implant research analysis."},
                {"role": "user", "content": prompt.format(text=text)}
            ]
        )
        return response.choices[0].message.content
    elif isinstance(client, anthropic.Anthropic):
        response = client.messages.create(
            model=model,
            max_tokens=4000,
            messages=[
                {"role": "user", "content": prompt.format(text=text)}
            ]
        )
        return response.content[0].text
    else:
        raise ValueError("Unsupported client type")

def main(pdf_path, out_dir, model, client):
    paper_text = load_pdf(pdf_path)
    analysis = analyze_paper(paper_text, model, client)
    
    os.makedirs(out_dir, exist_ok=True)
    output_file = os.path.join(out_dir, f'analysis_{os.path.basename(pdf_path)}.txt')
    with open(output_file, 'w') as f:
        f.write(analysis)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf_path', type=str, nargs='+', required=True)
    parser.add_argument('--out_dir', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    args = parser.parse_args()
    
    pdf_path = ' '.join(args.pdf_path)  # Join the path parts if they were split
    
    if args.model.startswith("gpt"):
        client = OpenAI()
    elif args.model.startswith("claude"):
        client = anthropic.Anthropic()
    else:
        raise ValueError(f"Unsupported model: {args.model}")
    
    main(pdf_path, args.out_dir, args.model, client)