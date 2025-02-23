CONTENT = """
Machine learning has transformed numerous industries, from healthcare to finance, by enabling automated decision-making. It relies on statistical techniques and computational power to derive insights from vast amounts of data.

**2. Types of Machine Learning**
- **Supervised Learning:** The model learns from labeled data, where each training example has an associated output. Example algorithms: Linear Regression, Decision Trees, Support Vector Machines (SVM).
- **Unsupervised Learning:** The model learns patterns from unlabeled data, discovering inherent structures. Example algorithms: K-Means Clustering, Principal Component Analysis (PCA).
- **Reinforcement Learning:** The model interacts with an environment to learn optimal actions based on rewards and penalties. Example algorithms: Q-Learning, Deep Q Networks (DQN).

**3. Model Evaluation Metrics**
- **Accuracy:** The proportion of correct predictions in classification tasks.
- **Precision & Recall:** Metrics used for imbalanced datasets, particularly in classification problems.
- **Mean Squared Error (MSE):** A common metric for evaluating regression models.
- **Confusion Matrix:** A table that summarizes classification performance by comparing predicted and actual labels.

**4. Common Machine Learning Algorithms**
- **Linear Regression:** A statistical method for modeling relationships between a dependent variable and one or more independent variables.
- **Decision Trees:** A model that splits data based on feature values, forming a tree-like structure.
- **Random Forest:** An ensemble learning method that builds multiple decision trees to improve prediction accuracy.
- **Neural Networks:** Deep learning architectures inspired by biological neural systems, used for complex pattern recognition tasks.

**5. Challenges in Machine Learning**
- **Overfitting:** When a model learns noise rather than the true pattern, leading to poor generalization.
- **Bias-Variance Tradeoff:** A fundamental challenge in machine learning where models must balance complexity and generalizability.
- **Data Quality:** The performance of machine learning models heavily depends on the quality and quantity of data available.

**6. Conclusion**
Machine learning continues to advance rapidly, impacting diverse fields. Understanding its fundamental principles, algorithms, and challenges is crucial for developing effective AI applications.

"""

FLASHCARD = """
Output: The value for each key should be short - one or a few word answer. The output should be related to the text in the CONTENT section.
Ex: "Question":"This is a sample Answer"

{ 
    "What type of data does supervised learning use?": "Labeled", 
    "Which learning type finds patterns in unlabeled data?": "Unsupervised",
    "What metric measures the correctness of a classification model?": "Accuracy", 
    "Which metric balances precision and recall?": "F1-score", 
    "What issue arises when a model learns noise?": "Overfitting", 
    "Which technique prevents overfitting?": "Regularization", 
    "Which algorithm is common for regression?": "Linear", 
    "What summarizes classification performance?": "ConfusionMatrix" 
}
"""

QUIZ = """
Given CONTENT OUTPUT should be

{
    "questions": [
        {
            "question":"question",
            "A": "choice1_question1",
            "B": "choice2_question1",
            "C": "choice3_question1",
            "D": "choice4_question1",
            "correct_option": "A/B/C/D", 
            "response_if_wrong": "response_if_wrong_question1"
        },
        {
            "question":"question",
            "A": "choice1_question1",
            "B": "choice2_question1",
            "C": "choice3_question1",
            "D": "choice4_question1",
            "correct_option": "A/B/C/D", 
            "response_if_wrong": "response_if_wrong_question1"
        }
    ]
}


EXAMPLE: 
CONTENT

""" 

QUIZ += CONTENT

QUIZ+= """
OUTPUT:
{
    "What is machine learning?": "A method for manually programming systems\vA subfield of AI that enables systems to learn from data\vA type of computer hardware\vA way to increase internet speed\vA subfield of AI that enables systems to learn from data\vThat's not correct. Machine learning is a subfield of artificial intelligence that enables systems to learn patterns from data and make predictions or decisions without being explicitly programmed.",
    "Which type of learning uses labeled data?": "Unsupervised Learning\vSupervised Learning\vReinforcement Learning\vSemi-Supervised Learning\vSupervised Learning\vThat's not correct. Supervised learning is when the model learns from labeled data where each training example has an associated output.",
    "What is the purpose of a confusion matrix?": "To evaluate regression models\vTo summarize classification performance\vTo improve data quality\vTo increase computational power\vTo summarize classification performance\vThat's not correct. A confusion matrix is a table that summarizes classification performance by comparing predicted and actual labels.",
    "What is overfitting in machine learning?": "When a model learns noise rather than the true pattern\vWhen a model generalizes well to new data\vA technique for improving data quality\vA method for simplifying algorithms\vWhen a model learns noise rather than the true pattern\vThat's not correct. Overfitting occurs when a model learns noise rather than the true pattern leading to poor generalization.",
    "Which machine learning algorithm is commonly used for regression tasks?": "Decision Trees\vLinear Regression\vK-Means Clustering\vNeural Networks\vLinear Regression\vThat's not correct. Linear Regression is a statistical method for modeling relationships between a dependent variable and one or more independent variables."
}
CONTENT:

"""


SUMMARY = f"""
Create a structured summary for the give content 
"""