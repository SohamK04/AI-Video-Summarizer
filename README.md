# AI-Driven Video Summarizer using LaMini-Langchain and TVSum Dataset

## Overview
This project implements an AI-driven video summarization system using **LaMini-Langchain**, a lightweight LangChain model optimized for summarization and natural language processing tasks. The system leverages the **TVSum dataset**, which contains annotated video importance scores, to generate concise yet informative video summaries.

## Features
- **Automated Video Summarization**: Extracts key moments from videos based on their importance.
- **LaMini-Langchain Integration**: Utilizes advanced NLP techniques for content understanding.
- **TVSum Dataset Utilization**: Uses ground truth importance scores for training and evaluation.
- **Customizable Summary Length**: Allows users to control the level of summarization.
- **Efficient Processing**: Optimized for performance and scalability.

## Dataset: TVSum
The **TVSum dataset (Title-Based Video Summarization)** consists of **50 videos** across various categories like news, travel, and sports. Each video has:
- Annotated importance scores from multiple users.
- Shot-level importance labels.
- Metadata related to video content.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip
- GPU (optional but recommended for faster processing)

## Model Pipeline
1. **Video Preprocessing**: Extracts frames and segments the video.
2. **Feature Extraction**: Uses LaMini-Langchain for NLP-based scene understanding.
3. **Score Assignment**: Assigns importance scores based on TVSum annotations.
4. **Summary Generation**: Selects and compiles key moments into a final summary.

## Evaluation Metrics
- **F1-score**: Measures alignment with TVSum ground truth.
- **Compression Ratio**: Evaluates the effectiveness of summarization.
- **User Study**: (Optional) Human evaluation of summary relevance.

## Future Enhancements
- Support for multi-modal summarization (audio + text + video).
- Integration with real-time summarization pipelines.
- Improvements in user interactivity (e.g., adjustable importance weights).

## Contributors
- **Your Name** -  Soham Kolhe 
- **Team Members** - Samagra Gupta

## License
This project is licensed under the MIT License.

## Acknowledgments
- **TVSum Dataset Authors** for providing a well-annotated dataset.
- **LangChain & LaMini Developers** for their contributions to NLP frameworks.
- **OpenAI & Hugging Face** for supporting NLP research.

For any issues or improvements, feel free to open an issue or submit a pull request!
