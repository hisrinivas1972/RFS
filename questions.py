import random

questions = [
    # Section A – Verbal Ability
    {"question": "He is known ___ his honesty.", "options": ["for", "of", "about", "to"], "answer": "for"},
    {"question": "The group of dancers ___ performing beautifully.", "options": ["are", "is", "were", "have"], "answer": "is"},
    {"question": "Choose the correctly spelled word:", "options": ["Accomodate", "Acommodate", "Accommodate", "Acomodat"], "answer": "Accommodate"},
    {"question": "Select the synonym of 'benevolent':", "options": ["Harsh", "Kind", "Loud", "Mean"], "answer": "Kind"},
    {"question": "The teacher gave us many examples to ___ her point.", "options": ["illustrate", "imitate", "dictate", "celebrate"], "answer": "illustrate"},
    {"question": "Choose the antonym of 'Scarce':", "options": ["Few", "Plenty", "Rare", "Empty"], "answer": "Plenty"},
    {"question": "Identify the error: She did not went to the party last night.", "options": ["She", "did not", "went", "to the party"], "answer": "went"},
    {"question": "Rearrange: P: a beautiful gift, Q: her mother, R: gave her, S: on her birthday", "options": ["QPSR", "QRPS", "RQSP", "QSRP"], "answer": "QRPS"},
    {"question": "Choose the correct passive voice: They will complete the project by tomorrow.", "options": ["The project completed by tomorrow.", "The project will be completed by them by tomorrow.", "The project was completed by them tomorrow.", "The project is completed by tomorrow."], "answer": "The project will be completed by them by tomorrow."},
    {"question": "Which sentence is grammatically correct?", "options": ["She can sings well.", "She sings well.", "She singing well.", "She sangs well."], "answer": "She sings well."},
    {"question": "He usually ___ to work at 9 am.", "options": ["go", "goes", "going", "gone"], "answer": "goes"},
    {"question": "If I were you, I ___ not do that.", "options": ["will", "would", "shall", "should"], "answer": "would"},
    {"question": "Indirect speech: He said, 'I am tired.'", "options": ["He said he is tired.", "He said he was tired.", "He said I was tired.", "He told he is tired."], "answer": "He said he was tired."},
    {"question": "Choose the synonym of 'elated':", "options": ["Excited", "Sad", "Angry", "Sleepy"], "answer": "Excited"},
    {"question": "Identify the correct sentence:", "options": ["Its raining outside.", "It’s raining outside.", "Its’ raining outside.", "Its raining, outside"], "answer": "It’s raining outside."},
    {"question": "To beat around the bush means:", "options": ["To beat someone", "To avoid the main topic", "To plant trees", "To fight indirectly"], "answer": "To avoid the main topic"},
    {"question": "Choose the correct sentence:", "options": ["Neither of the boys are guilty.", "Neither of the boy is guilty.", "Neither of the boys is guilty.", "Neither boy are guilty."], "answer": "Neither of the boys is guilty."},
    {"question": "Select the antonym of 'expand':", "options": ["Grow", "Contract", "Enlarge", "Develop"], "answer": "Contract"},
    {"question": "Choose the correct article: He is ___ honest man.", "options": ["a", "an", "the", "no article"], "answer": "an"},
    {"question": "Which word is different in meaning?", "options": ["Talkative", "Chatty", "Silent", "Loquacious"], "answer": "Silent"},

    # Section B – Numerical Ability
    {"question": "What is 25% of 640?", "options": ["120", "140", "160", "180"], "answer": "160"},
    {"question": "A train travels 120 km in 2 hours. What is its speed?", "options": ["50 km/h", "60 km/h", "70 km/h", "80 km/h"], "answer": "60 km/h"},
    {"question": "Simplify: (60 ÷ 5) + (45 ÷ 3) = ?", "options": ["17", "25", "27", "30"], "answer": "27"},
    {"question": "A number is 30 more than another. Their sum is 150. Find the smaller number.", "options": ["60", "70", "80", "90"], "answer": "60"},
    {"question": "Average of 12, 18, 24, and 30 = ?", "options": ["18", "21", "24", "27"], "answer": "21"},
    {"question": "Simple Interest on ₹4,000 for 3 years at 5% p.a.?", "options": ["₹400", "₹500", "₹600", "₹700"], "answer": "₹600"},
    {"question": "Volume of a cube with side 5 cm?", "options": ["125 cm³", "150 cm³", "100 cm³", "75 cm³"], "answer": "125 cm³"},
    {"question": "If A:B = 3:4 and B:C = 5:6, then A:C = ?", "options": ["15:24", "3:5", "2:3", "5:8"], "answer": "15:24"},
    {"question": "A man buys a shirt at ₹240 and sells it at ₹300. Find profit %.", "options": ["20%", "25%", "30%", "35%"], "answer": "25%"},
    {"question": "Boat covers 48 km downstream in 2 hrs, upstream in 3 hrs. Speed in still water?", "options": ["10 km/h", "12 km/h", "14 km/h", "16 km/h"], "answer": "12 km/h"},
    {"question": "Find the HCF of 18 and 24.", "options": ["6", "8", "12", "4"], "answer": "6"},
    {"question": "Find the LCM of 4, 6, 8.", "options": ["12", "16", "24", "48"], "answer": "24"},
    {"question": "A man spends 60% of salary. If he saves ₹4,000, what is salary?", "options": ["₹8,000", "₹10,000", "₹12,000", "₹16,000"], "answer": "₹10,000"},
    {"question": "Find the missing number: 5, 9, 17, 33, ?", "options": ["57", "65", "49", "61"], "answer": "65"},
    {"question": "If 3 pens cost ₹45, what will 7 pens cost?", "options": ["₹90", "₹100", "₹105", "₹115"], "answer": "₹105"},
    {"question": "What is the square root of 196?", "options": ["12", "13", "14", "15"], "answer": "14"},
    {"question": "8 men complete a job in 15 days. 10 men will complete it in?", "options": ["10", "12", "14", "16"], "answer": "12"},
    {"question": "Selling price is ₹840, profit is 20%. Find cost price.", "options": ["₹700", "₹800", "₹850", "₹880"], "answer": "₹700"},
    {"question": "Item marked at ₹1,200, 10% discount. Selling price?", "options": ["₹1,080", "₹1,100", "₹1,200", "₹1,240"], "answer": "₹1,080"},
    {"question": "Rectangle: length 12 m, width 8 m. Area?", "options": ["90 m²", "96 m²", "100 m²", "104 m²"], "answer": "96 m²"},

    # Section C – Analytical Ability
    {"question": "Find the missing number: 2, 4, 8, 16, ?", "options": ["24", "30", "32", "36"], "answer": "32"},
    {"question": "If DOG = 4157, CAT = 3120, what is GOD?", "options": ["7415", "7514", "7541", "7451"], "answer": "7514"},
    {"question": "Pointing to a woman, Ajay said, “She is the daughter of my mother’s only son.”", "options": ["Sister", "Niece", "Cousin", "Aunt"], "answer": "Niece"},
    {"question": "Which word is the odd one out?", "options": ["Monday", "Friday", "Sunday", "January"], "answer": "January"},
    {"question": "Which number does not belong?", "options": ["81", "64", "49", "42"], "answer": "42"},
    {"question": "Arrange: 1. Family 2. Child 3. Grandparents 4. Nation", "options": ["2-1-3-4", "3-2-1-4", "1-2-3-4", "4-3-2-1"], "answer": "2-1-3-4"},
    {"question": "Next in pattern: A, C, F, J, O, ?", "options": ["S", "T", "U", "V"], "answer": "U"},
    {"question": "Amit is 15th from left, 20th from right. Total students?", "options": ["34", "35", "36", "33"], "answer": "34"},
    {"question": "Which is different from the rest?", "options": ["Pen", "Pencil", "Eraser", "Chalk"], "answer": "Eraser"},
    {"question": "If APPLE = BQQMF, then MANGO = ?", "options": ["NBOHP", "NBOPH", "NBPHO", "OBPHN"], "answer": "NBPHO"},
    {"question": "Complete the series: 121, 144, 169, 196, ?", "options": ["221", "225", "231", "240"], "answer": "225"},
    {"question": "If vowels are removed from 'EXAMINATION', how many letters are left?", "options": ["6", "7", "8", "9"], "answer": "6"},
    {"question": "Which comes next: 1, 4, 9, 16, 25, ?", "options": ["30", "32", "36", "40"], "answer": "36"},
    {"question": "Find the next number in the series: 3, 6, 12, 24, ?", "options": ["36", "48", "60", "72"], "answer": "48"},
    {"question": "If 5x – 3 = 2x + 12, find x.", "options": ["5", "4", "3", "6"], "answer": "5"},
    {"question": "Find the odd one out: 2, 3, 5, 9, 11", "options": ["2", "3", "5", "9"], "answer": "9"},
    {"question": "If in a code, TABLE is written as YFOQJ, how is CHAIR written?", "options": ["HMFNV", "HMJNV", "HMKNV", "HMFNV"], "answer": "HMFNV"},
    {"question": "Complete the analogy: Apple is to Fruit as Carrot is to ?", "options": ["Vegetable", "Fruit", "Plant", "Root"], "answer": "Vegetable"},
    {"question": "If today is Monday, what day will be after 45 days?", "options": ["Saturday", "Sunday", "Monday", "Tuesday"], "answer": "Wednesday"},
    {"question": "Ramu’s mother has four children: April, May, June and ?", "options": ["July", "Ramu", "August", "September"], "answer": "Ramu"},
]

def shuffle_questions_and_options(questions):
    # Shuffle questions list
    random.shuffle(questions)

    # For each question, shuffle options and keep track of correct answer
    for q in questions:
        options = q["options"]
        correct_answer = q["answer"]

        # Shuffle options
        shuffled_options = options[:]
        random.shuffle(shuffled_options)

        # Update options in question
        q["options"] = shuffled_options

        # Update answer index or keep answer as string (better to keep answer as string)
        # We will check answer by comparing strings later

    return questions

def run_quiz():
    shuffled_questions = shuffle_questions_and_options(questions)

    score = 0
    for i, q in enumerate(shuffled_questions, 1):
        print(f"\nQ{i}: {q['question']}")

        for idx, option in enumerate(q["options"], 1):
            print(f"  {idx}. {option}")

        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= len(q["options"]):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(q['options'])}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        selected_option = q["options"][choice - 1]

        if selected_option == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    print(f"\nQuiz finished! Your score: {score} / {len(shuffled_questions)}")

if __name__ == "__main__":
    run_quiz()
