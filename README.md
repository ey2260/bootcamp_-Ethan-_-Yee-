# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## Homework 5
Within the homework 5 foloder located within homework, there are 4 files, a folder named data, .env, .env example and the homework 5 itself
- .env and .env example are for storage of API keys and secrets
- data has a processed and raw subfolder containing data before and after processing

## Homework 6

Assumptions:
-
Cleaning strategy for median was to identify collums with numbers in them. Then, it would go through these empty collums and calculate the median, before filling it back in
Cleaning stratrgy for dropping rows is simlar with rows containing missing values simply being dropped
Cleaning strategy for the normalizer is to scale numbers using a min max scaler