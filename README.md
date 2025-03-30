# Stress Detector on AWS

A stress detector model deployed on AWS Lambda that detects stress in specific stress-related Reddit subreddits. I did this project to gain hands-on experience with cloud deployments. This is an old project that I never pushed, so it's been updated to the latest Python version and libraries, and well, here we are.

I wanted the model to be light and suitable enough to be able to run as a Lambda service, so I kept things very simple; I utilized scikit-learn's TF-IDF vectorizer for text preprocessing and trained a logistic regression classifier, achieving an accuracy of 72%. For deployment, I containerized the model with Docker. The image builds are hosted on AWS ECR and automatically deployed to AWS Lambda. At the end, I implemented CI/CD pipelines via GitHub Actions for seamless integration and deployment, along with monitoring capabilities. The model is exposed through an API, allowing for easy access and interaction with the stress detection functionality.

The idea for the project was inspired by the paper "Dreaddit: A Reddit Dataset for Stress Analysis in Social Media" (https://arxiv.org/abs/1911.00133) by Elsbeth Turcan and Kathleen McKeown. You can learn more about the research by reading the paper. The dataset can be found on Papers with Code (https://paperswithcode.com/dataset/dreaddit).

Special thanks to [Wajih Ullah Baig](https://github.com/wajihullahbaig) for not only helping me fix code issues but also for teaching me the underlying concepts behind the problems.

## Table of Contents
- [Installation](#installation)
- [Data](#data)
- [License](#license)

## Installation

Use any Python >= 3.11 version along with the requirements.txt file in the repository. I used 3.12 with the latest versions of all libraries.

```bash
# Use uv for better performance
pip install uv --no-cache-dir

# Installing using repo file
uv pip install -r requirements.txt --no-cache-dir
```

## Data
Link to the original dataset on Papers with Code:
https://paperswithcode.com/dataset/dreaddit

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). See the LICENSE file for details.
