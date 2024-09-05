import os

def generate_mermaid_diagram():
    mermaid_code = """
    graph TD
    A[User runs launch_scientist.py] --> B[Identify PDF files in input folder]
    B --> C[For each PDF file]
    C --> D[Run experiment.py]
    D --> E[Load PDF and extract text]
    E --> F[Analyze paper using AI model]
    F --> G[Generate analysis based on criteria]
    G --> H[Save analysis to text file]
    """

    with open('flow_diagram.mmd', 'w') as f:
        f.write(mermaid_code)

    os.system('mmdc -i flow_diagram.mmd -o flow_diagram.png')

if __name__ == "__main__":
    generate_mermaid_diagram()