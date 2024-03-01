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
