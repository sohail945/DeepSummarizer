# **DeepSummarizer**

AI-powered tool for summarizing engagement data and providing actionable insights.

## **Table of Contents**
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Input Format](#input-format)
- [Output](#output)
- [License](#license)
- [Contributing](#contributing)

## **Description**
**DeepSummarizer** is an AI-powered tool that uses the **DeepSeek 1.5B** model to analyze engagement data and generate clear summaries and actionable insights. It processes tabular data (e.g., survey or ratings data) and provides summarized key insights along with recommendations for improvement.

## **Features**
- Generates summaries from engagement data.
- Provides actionable insights and recommendations.
- Powered by the **DeepSeek 1.5B** model.
- Easy-to-use interface with **Streamlit**.

## **Requirements**
- Python 3.11
- 8GB+ RAM (minimum)
- Libraries:
  - `transformers`
  - `streamlit`
  - `pandas`
  - `dotenv`
  - `torch`
  - `huggingface_hub`

## **Installation**
1. Clone the repository:
   ```bash
   git clone <repo_link>
   cd DeepSummarizer

Run the application with Streamlit:

    ```bash
    streamlit run app.py

### **Input Format**
The input should be a CSV file containing engagement data (e.g., survey results with dimensions like `Mean` and `SD`).
Example CSV columns: `Dimension`, `Mean`, `SD`.

### **Output**
- **Summary**: Key insights derived from the data.
- **Recommendations**: Actionable suggestions to improve low-performing areas.

## **License**
This project is licensed under the MIT License.

## **Contributing**
Feel free to contribute by opening issues or submitting pull requests. Suggestions for improving performance or adding new features are welcome.

