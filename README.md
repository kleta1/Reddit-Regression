# CS 595 Project: Reddit Regression
-----------------------------------
### *Authors*
- Justin Duhaime
- Kaitlyn Leta

### *Files*
- Project_Reddit.ipynb
  - Jupyter Notebook containing the ML algorithms and results
- san.py
  - Python script to sanitize the raw reddit data

### *How to run from repo*
1. Download the Project_Reddit.ipynb and out0.json file to the same working directory
2. Open the Project_Reddit.ipynb file as a jupyter notebook
3. Run the notebook

### *How to run from scratch*
1. Go to https://files.pushshift.io/reddit/submissions/ and download a repository of reddit submissions
2. Extract the file to a working direcotry
3. Alter the san.py file to open the extracted file (line 12)
4. Run the san.py file
   * This will create multiple files in the current working directory, each with 100,000 reddit posts each
5. Open the Project_Reddit.ipynb file in a jupyter notebook
6. Run the notebook
   * You can change the filename in the first code block to any of those that were created by the san.py script for further regression testing
