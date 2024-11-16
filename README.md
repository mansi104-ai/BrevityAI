<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mansi104-ai/BrevityAI">
    <img src="/logo_2.png" alt="Logo" height="80">
  </a>

  <h3 align="center">BrevityAI</h3>

  <p align="center">
    AI-powered Document Summarization
    <br />
    <br />
    <a href="https://your-demo-link.com">View Demo</a>
    ·
    <a href="https://github.com/mansi104-ai/BrevityAI/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/mansi104-ai/BrevityAI/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
  <h2>Table of Contents</h2>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Keywords">Keywords</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
  </ol>

<!-- ABOUT THE PROJECT -->
## About The Project

BrevityAI is an AI-powered document summarization tool that helps you quickly understand and summarize long documents. With the integration of the T5 model and a user-friendly interface, it generates concise, accurate, and context-aware summaries in multiple languages.

Key Features:

- **Multilingual Summarization**: Automatically generates summaries in multiple languages.
- **Document Upload & Management**: Securely upload and manage documents for summarization.
- **Detailed Summaries**: View and download summaries in a clean and readable format.
- **Export Results**: Export your document summaries and logs as PDFs for easy sharing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* ![T5](https://img.shields.io/badge/T5-2D3A3A?style=for-the-badge&logo=TensorFlow&logoColor=white)
*  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
* ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
* ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=GoogleCloud&logoColor=white)
* ![Vertex AI](https://img.shields.io/badge/Vertex%20AI-1288E5?style=for-the-badge&logo=Google&logoColor=white)
* ![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This section explains how to set up the project locally.

### Keywords
- **Maximum Summary Length**: Sets the maximum word count for the summary (Range: 50–500).
- **Minimum Summary Length**: Sets the minimum word count (Range: 10–100).
- **Length Penalty**: Adjusts brevity vs. coverage:
  - **< 1.0**: Produces concise summaries.
  - **> 1.0**: Generates longer summaries.
  - **1.0**: Neutral balance.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/mansi104-ai/BrevityAI.git

   cd BrevityAI
   ```

2. Setup the environment:
   ```sh
  python -m venv env

  source env/bin/activate  ( For Linux/MacOS )
  
  env\Scripts\activate     ( For Windows )

   ```

3. Install the dependencies :
  ```sh
  pip install -r requirements.txt
  ```

4. Run the application : 
  ```sh
  streamlit run main.py
  ```
5. Access the App: Open your browser and navigate to http://localhost:8501.

## Usage

Follow these steps to use the **Text Summarization App**:

1. **Launch the App**:
   - Start the app by running the following command:
     ```bash
     streamlit run app.py
     ```
   - Open your browser and navigate to `http://localhost:8501`.

2. **Choose Input Method**:
   - **File Upload**: 
     - Click on "Upload a file" to upload a PDF or JSON file.
     - The app extracts text from the uploaded file.
   - **Manual Input**: 
     - Enter or paste text directly into the provided text area.

3. **Customize Summary Settings**:
   - Use the sliders to adjust:
     - Maximum summary length.
     - Minimum summary length.
     - Length penalty (controls brevity).
   - Default values are set for quick summarization.

4. **Generate Summary**:
   - Click the **"Generate Summary"** button.
   - Wait for the app to process and display the summary.

5. **Download Summary**:
   - After the summary is generated, click on the **"Download Summary as PDF"** button to save the summary locally.

---

## Contributing

We welcome contributions to enhance the **Text Summarization App**! Here's how you can contribute:

### Steps to Contribute
1. **Fork the Repository**:
   - Navigate to the GitHub repository and click **Fork**.

2. **Clone the Forked Repository**:
   - Clone the repository to your local system:
     ```bash
     git clone https://github.com/mansi104-ai/BrevityAI
     
     ```

3. **Create a Branch**:
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature-or-bugfix-name
     ```

4. **Make Your Changes**:
   - Modify the code or documentation as needed.

5. **Test Your Changes**:
   - Run the app locally and ensure all changes work as expected.

6. **Commit and Push**:
   - Commit your changes with a descriptive message:
     ```bash
     git add .
     git commit -m "Description of changes"
     ```
   - Push the changes to your forked repository:
     ```bash
     git push origin feature-or-bugfix-name
     ```

7. **Create a Pull Request**:
   - Open a pull request from your forked repository to the original repository.
   - Provide a clear description of your changes and the problem they solve.

---

### Contribution Guidelines
- Adhere to the existing code style and conventions.
- Ensure that all dependencies are up to date.
- Document your changes clearly in the `README` file if applicable.
- Test your changes thoroughly before submitting a pull request.

---

We appreciate your contributions and look forward to building this app together!
