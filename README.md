# 🚀 Employee Salary Prediction App

Welcome to the **Employee Salary Prediction App**, a dynamic machine learning web application crafted with **Streamlit** that forecasts whether an employee's income falls into the `<=50K` or `>50K` category. Powered by AI and built with passion by [Ashish Verma](https://github.com/AshishVerma10), this tool leverages key attributes like age, education, occupation, weekly work hours, and work sector to deliver insightful predictions.

## ✨ Features
- **Real-Time Predictions**: Get instant salary class predictions with a sleek interface.
- **Interactive Design**: Explore inputs and results with an engaging user experience.
- **AI-Driven Insights**: Built using a trained Gradient Boosting model from the Adult Income dataset.
- **Custom Inputs**: Tweak variables like:
  - Age
  - Education Level
  - Occupation
  - Hours Worked per Week
  - Workclass / Organization Type
- **Visual Flair**: Enjoy a gradient-themed UI with dark/light mode toggles!

## 🛠️ Tech Stack
- **Python**: The backbone of the app.
- **Scikit-learn**: For model training and pipeline creation.
- **Pandas**: Data handling and preprocessing.
- **Streamlit**: Crafting the interactive web interface.
- **Joblib**: Serializing the ML model for deployment.

## 📁 Project Structure
```
├── app.py                  # The magic happens here - Streamlit app interface
├── salary_model.pkl        # Pretrained Gradient Boosting model pipeline
├── Employee_Salary_Prediction.ipynb  # Notebook with model training journey
├── requirements.txt        # Dependencies to get you started
```

## 🖥️ How to Run Locally

1. Clone the repo and dive in:
   ```bash
   git clone https://github.com/AshishVerma10/employee-salary-prediction.git
   cd employee-salary-prediction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app and explore:
   ```bash
   streamlit run app.py
   ```

## 📊 Model Overview

This app harnesses the power of the **Adult Income Dataset**, training on features such as:
- Age
- Education
- Occupation
- Hours-per-week
- Workclass

The journey from data to prediction is detailed in `Employee_Salary_Prediction.ipynb`, where the Gradient Boosting model was fine-tuned and saved using `joblib` for seamless integration.

## 🌟 Contribution

Got ideas to elevate this project? Fork it on [GitHub](https://github.com/AshishVerma10), submit issues, or send pull requests! I’m all ears for feedback—let’s build something amazing together. Connect with me on [LinkedIn](https://www.linkedin.com/in/ashishverma2210/) or drop an email at vashishverma10@gmail.com.

## 🎉 Acknowledgments

A heartfelt thanks to the open-source community and the Adult Income Dataset contributors. This project is a labor of love, and I’m excited to see where it goes next!

## ⚡ Stay Connected
- Follow my GitHub journey: [AshishVerma10](https://github.com/AshishVerma10)
- Check out more projects and updates!

© 2025 Built with 💻 by [Ashish Verma](https://github.com/AshishVerma10) | Powered by AI Magic