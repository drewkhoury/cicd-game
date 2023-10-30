def colored_print(msg, color=None, end='\n'):
    color_codes = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'PURPLE': '\033[95m',
        'ENDC': '\033[0m'
    }

    if color and color in color_codes:
        print(f"{color_codes[color]}{msg}{color_codes['ENDC']}", end=end)
    else:
        print(msg, end=end)


def display_options(title, options, colors=None):
    colored_print(title, color='PURPLE')
    for i, option in enumerate(options, 1):
        color = colors[i-1] if colors else None
        colored_print(f"{i}. {option}", color=color)


def handle_choices(prompt, options, costs):
    choices = []
    total_cost = 0

    while True:
        try:
            choices = list(map(int, input(prompt).split(',')))
            for choice in choices:
                if choice < 1 or choice > len(options):
                    raise ValueError
                total_cost += costs[choice-1]
            break
        except ValueError:
            colored_print("Invalid choice! Please try again.", color='RED')

    return choices, total_cost


def setup_pipeline():
    budget = 1000
    choices_made = {}

    colored_print("Welcome to the CI/CD Pipeline Game!", color='PURPLE')
    colored_print("\nYour initial budget is: ${}".format(budget), color='GREEN')
    colored_print("\nCost indicators:")
    colored_print("More expensive options are indicated in ", end='')
    colored_print("RED", color='RED')
    colored_print("Medium priced options are in ", end='')
    colored_print("YELLOW", color='YELLOW')
    colored_print("Cheaper options are in ", end='')
    colored_print("GREEN", color='GREEN')
    colored_print("")

    sections = [
        {
            'title': "\nSelect your Source Control Management tool:",
            'options': ["GitHub", "GitLab", "BitBucket", "Manual"],
            'costs': [150, 100, 100, 0],
            'colors': ['YELLOW', 'YELLOW', 'YELLOW', 'GREEN'],
            'section_name': 'SCM Tool'
        },
        {
            'title': "\nSelect your Build tool:",
            'options': ["TravisCI", "Jenkins", "GitHub Actions", "GitLab CI", "Other"],
            'costs': [100, 120, 90, 90, 80],
            'colors': ['YELLOW', 'RED', 'YELLOW', 'YELLOW', 'GREEN'],
            'section_name': 'Build Tool'
        },
        {
            'title': "\nSelect your Testing methodology:",
            'options': ["None", "Manual", "Automated (Select from next options)"],
            'costs': [0, 50, 0],
            'colors': ['RED', 'GREEN', 'GREEN'],
            'section_name': 'Testing'
        },
        {
            'title': "\nSelect your Deployment environments:",
            'options': ["Dev", "Test", "UAT", "Prod"],
            'costs': [50, 50, 50, 50],
            'colors': ['GREEN', 'YELLOW', 'YELLOW', 'GREEN'],
            'section_name': 'Environments'
        },
        {
            'title': "\nSelect Development PowerUps:",
            'options': ["Feature Flags", "TDD", "BDD", "Pair Programming"],
            'costs': [100, 60, 60, 80],
            'colors': ['RED', 'YELLOW', 'YELLOW', 'RED'],
            'section_name': 'PowerUps'
        }
    ]

    for section in sections:
        display_options(section['title'], section['options'], section['colors'])
        choices, cost = handle_choices("Enter your choice (e.g., 1,2): ", section['options'], section['costs'])
        budget -= cost
        choices_made[section['section_name']] = [section['options'][i-1] for i in choices]

        if section['section_name'] == 'Testing' and "Automated (Select from next options)" in choices_made[section['section_name']]:
            automated_tests_options = ["Unit Tests", "Integration Tests", "Contract Testing", "Other"]
            automated_tests_costs = [70, 80, 60, 50]
            automated_tests_colors = ['YELLOW', 'RED', 'YELLOW', 'GREEN']
            display_options("\nSelect Automated Tests:", automated_tests_options, automated_tests_colors)
            choices, cost = handle_choices("Enter your choice (e.g., 1,2): ", automated_tests_options, automated_tests_costs)
            budget -= cost
            choices_made['Automated Tests'] = [automated_tests_options[i-1] for i in choices]

    # Output
    colored_print("\nResults:", color='PURPLE')
    colored_print("Remaining Budget: ${}".format(budget), color='GREEN' if budget > 0 else 'RED')

    # Choices Summary
    colored_print("\nChoices Summary:", color='PURPLE')
    for key, value in choices_made.items():
        colored_print(f"{key}: {', '.join(value)}", color='GREEN')

    if budget < 0:
        colored_print("Oh no! You've overspent!", color='RED')
    else:
        colored_print("Great job on setting up your pipeline!", color='GREEN')

    # Winner declaration for choosing Pair Programming
    if "Pair Programming" in choices_made.get('PowerUps', []):
        colored_print("Congratulations! You chose Pair Programming. You're a Winner!", color='YELLOW')
        print("""
        / \__
       (    @\___
        /         O
      /  (_____/
    /_____/ U
        """)


if __name__ == "__main__":
    setup_pipeline()
