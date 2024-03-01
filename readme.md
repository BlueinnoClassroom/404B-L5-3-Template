# 404B Lesson 5 Assignment 5A

- Estimated time to complete: 5 ~ 10 mins

- You must know how to:
  - create class
  - define properties & methods in class(es)
  - append item into list
  - loop through a list

## Instructions

### Split VS Code Window

You can drag `main.py` tab to the right side of the window to split the window into two panes. This will allow you to see the instructions and the code at the same time.

### Answering

You can answer the questions by writing your answers in the `main.py` file.

You can run the code by clicking the `Run` button on the top right corner of the editor.

The output will be shown in the `Terminal` tab at the bottom of the editor.

## Your Task

## 1. Your Task

The class `ExamReport` below which holds a list of student scores, you should complete the methods:

- `add()`: accepts a non-negative number and append the number to its list
- `get_average_score()`: returns the average of the score list

Sample:

```python
# Complete this class, replace `pass` in the methods with your solution:
class ExamReport:

    def __init__(self):
        self.scores = []

    def add(self, score):
        pass

    def get_average_score(self):
        pass



        
# 🚨🚨🚨 Do NOT change these lines:
exam_report = ExamReport()

exam_report.add(90)
exam_report.add(70)
exam_report.add(80)

print(f'average score: {exam_report.get_average_score()}')    # 80
```
  
## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
