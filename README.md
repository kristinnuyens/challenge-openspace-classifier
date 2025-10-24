# OpenSpace Organizer

## 🏢 Description

BeCode ARAI 8 moved to a new office at CEVI Ghent.

The office is an open space with 6 tables, each with 4 seats.

As new colleagues, we want to rotate seats every day to get to know each other better and work side by side with different team members.

The intent of this script, when finalized, was for it to run every day assigning everyone to new seats randomly.

The `dev_notebook.ipynb` includes code programmed so far.
The `table.py` and `openspace.py` may be final, but without finalizing the `main.py`, I am not certain of it.

## 🧩 Installation

Clone this repository:

```
git clone https://github.com/kristinnuyens/challenge-openspace-classifier
cd challenge-openspace-classifier
```

## 📦 Repo structure

```
.
├── utils/
│   ├── file_utils.py
│   ├── openspace.py
│   ├── table.py
├── .gitignore
├── dev_notebook.ipynb
├── main.py
├── new_colleagues.csv
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine

2. In the future, when the script would be finalized: to run the script, execute the `main.py` file from the command line

```
   python main.py
```

   Eventually the script would read your input file `new_colleagues.csv`, and organizes all colleagues to random seat assignments. The resulting seating plan would be displayed in the console and also saved to an "output.csv" file in your root directory. Currently we are only creating a tables.txt file.

## ⏱️ Timeline

I worked on this project for two days.

## 👩‍💻 Contributors

- Kristin Nuyens

## 📌 Personal Situation
This project was done as part of the AI & Data Science Bootcamp at BeCode.org.

Connect with me on [LinkedIn](https://www.linkedin.com/in/kristinnuyens/).