import random

class Pipeline:
    def __init__(self):
        self.scm = None
        self.build = None
        self.tests = []
        self.deployment = None
        self.budget = 1000  # Sample starting budget
        self.time_left = 10  # Sample time in days
        
    def add_scm(self, choice):
        if choice == "Git":
            self.scm = "Git"
            self.budget -= 100
            self.time_left -= 1

    def add_build(self, choice):
        if choice == "Jenkins":
            self.build = "Jenkins"
            self.budget -= 200
            self.time_left -= 1

    def add_test(self, test):
        self.tests.append(test)
        self.budget -= 50
        self.time_left -= 0.5

    def add_deployment(self, choice):
        if choice == "AWS":
            self.deployment = "AWS"
            self.budget -= 300
            self.time_left -= 2

    def random_event(self):
        events = ["Major bug found!", "Server downtime!", "Traffic spike!"]
        event = random.choice(events)
        print(f"Random Event: {event}")

        if event == "Major bug found!":
            self.time_left -= 1

    def display_status(self):
        print(f"SCM: {self.scm}")
        print(f"Build: {self.build}")
        print(f"Tests: {', '.join(self.tests)}")
        print(f"Deployment: {self.deployment}")
        print(f"Budget: ${self.budget}")
        print(f"Time Left: {self.time_left} days")


pipeline = Pipeline()

print("Welcome to Pipeline Perfection!")
while pipeline.time_left > 0 and pipeline.budget > 0:
    pipeline.display_status()
    
    action = input("Choose an action (add_scm, add_build, add_test, add_deployment, wait_for_event): ")
    
    if action == "add_scm":
        choice = input("Choose SCM (Git): ")
        pipeline.add_scm(choice)
    elif action == "add_build":
        choice = input("Choose Build System (Jenkins): ")
        pipeline.add_build(choice)
    elif action == "add_test":
        test = input("Enter Test Name: ")
        pipeline.add_test(test)
    elif action == "add_deployment":
        choice = input("Choose Deployment (AWS): ")
        pipeline.add_deployment(choice)
    elif action == "wait_for_event":
        pipeline.random_event()
