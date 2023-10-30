# CI/CD Pipeline Game

## Introduction
Welcome to the CI/CD Pipeline Game! In this game, you get to simulate setting up a CI/CD pipeline for a software project. However, there's a catch. You're on a budget! Make wise decisions to ensure your pipeline is effective without overspending.

## Gameplay
1. **Budget**: You start with a budget of $1000. Your goal is to set up a CI/CD pipeline without going over your budget.
2. **Selection**: Throughout the game, you will be prompted to make decisions about tools and practices for your CI/CD pipeline. Different options have different costs associated with them.
3. **Cost Indicators**: Options are color-coded based on their cost.
   - **Red**: More expensive
   - **Yellow**: Medium priced
   - **Green**: Cheaper
4. **PowerUps**: During the game, you will have the opportunity to select various development methodologies which act as PowerUps. Choosing these wisely will yield benefits.
5. **End of Game**: At the end of the game, you'll see a summary of your choices, your remaining budget, and feedback on your decisions.

## Special Features
- If you select **Pair Programming** during the game, something special will happen.

## How to Play
1. Ensure you have `docker` and `docker-compose` installed.
2. Clone the repository.
3. In the root directory, run the command `make run`.

## Sample Output

```
Welcome to the CI/CD Pipeline Game!

Your initial budget is: $1000

Cost indicators:
More expensive options are indicated in RED
Medium priced options are in YELLOW
Cheaper options are in GREEN

...

Results:
Remaining Budget: $500

Choices Summary:
SCM Tool: GitHub
Build Tool: TravisCI
Testing: Manual
Environments: Dev, Prod
PowerUps: Feature Flags

Great job on setting up your pipeline!
```

## Conclusion
Enjoy setting up your pipeline, learn about different tools and practices, and most importantly, have fun!