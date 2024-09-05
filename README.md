# AI Dental Literature Analyzer 🦷📚

This project is an adaptation of the [AI Scientist](https://github.com/SakanaAI/AI-Scientist) project, specifically tailored for analyzing dental research literature. It leverages advanced AI models to provide comprehensive analysis of dental implant research papers.

## 🌟 Key Features

### 1. Specialized Dental Literature Analysis 🔬

We've developed a custom prompt specifically for dental research analysis, covering:

- Methodological Rigor
- Research Ethics and Reporting
- Clinical Relevance and Applicability
- Scientific Novelty and Contribution
- Technical Aspects of Dental Implantology
- Long-term Outcomes and Follow-up
- Biological Considerations
- Interdisciplinary Approach
- Data Presentation and Interpretation
- Future Research Directions
- Overall Assessment

### 2. Multiple Output Formats 📊

- **JSON**: Structured data for programmatic analysis
- **Markdown**: Human-readable reports with emojis for easy comprehension

### 3. Mermaid Diagram Integration 🧜‍♀️

We've added a `mermaid.py` script to generate process flow diagrams, visualizing the analysis workflow.

### 4. Multi-Model Support 🤖

Compatible with various AI models including:
- GPT-4
- Claude
- DeepSeek
- Llama

### 5. Automated PDF Processing 📄

The system can automatically process multiple PDF files in a specified directory, generating analyses for each.

## 📁 Key Files

- `ai_scientist/analyze_dental_literature.py`: Core script for dental paper analysis
- `launch_scientist.py`: Modified to include dental literature review functionality
- `templates/dental_literature_review/experiment.py`: Template for dental literature experiments
- `api_test.py`: Updated to test various AI model APIs
- `mermaid.py`: For generating process flow diagrams

## 🛠 Technical Details

- Utilizes PyPDF2 for PDF text extraction
- Implements error handling and retries for API calls
- Supports multiple AI models through a unified interface
- Generates both JSON and Markdown outputs for flexibility

## 🚀 How to Use

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API keys in a `.env` file
4. Run the analysis: 
   ```
   python launch_scientist.py --model "gpt-4o-2024-05-13" --experiment dental_literature_review --input_folder "/path/to/your/pdf/folder"
   ```

## 📊 Example Output

Here's a snippet of the analysis output for a dental implant study:

markdown

Comprehensive Dental Implant Research Analysis 🦷🔬
📊 Methodological Rigor
Study design and its appropriateness
This study utilizes a retrospective case series design, which is suitable for evaluating the survival rate of dental implants over time. However, a prospective cohort design could provide stronger evidence.
Sample size, power calculations, and statistical analyses
The sample size of 43 patients and 388 implants is substantial. However, there is no mention of power calculations. Statistical analyses, including Kaplan-Meier estimation, log-rank tests, and Cox regression, are appropriately used to analyze survival rates.
... [other sections]
🏆 Overall Assessment
Quality, validity, and significance of the research
The research is of high quality and provides valid, significant contributions to the field of dental implantology.
Recommendation for publication
Accept with minor revisions to address ethical transparency and conflicts of interest.

## 🙏 Acknowledgments

This project is based on the [AI Scientist](https://github.com/SakanaAI/AI-Scientist) by SakanaAI. We have built upon their excellent work to create a specialized tool for dental research analysis.

## 📄 License

This project is licensed under the Apache License 2.0, in compliance with the original AI Scientist project's license.

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to get involved.

## 📞 Contact

- **Name:** Francisco Barbosa
- **Email:** [cisco@periospot.com](mailto:cisco@periospot.com)
- **Twitter/X:** [@cisco_researcher](https://twitter.com/cisco_researcher)


For any questions or concerns, please open an issue on this GitHub repository.