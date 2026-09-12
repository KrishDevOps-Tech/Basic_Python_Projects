# ==========================================
# Kaun Banega Crorepati (KBC) - CLI Game
# ==========================================
import time

print("=" * 50)
print("Welcome to Kaun Banega Crorepati Game (KBC)")
print("=" * 50)

time.sleep(2)
print(
    "Namaskaar Mai hu Amitabh Bachchan, aur aapka yahan haardik swagat hai.\n"
    "Aaj ke is khel mein aapko 5 sawalon ke jawab dene honge.\n"
    "Har sahi jawab ke baad aapko kuch paise milenge, aur agar aap galat\n"
    "jawab dete hain to aapka khel yahin khatam ho jayega."
)

time.sleep(2)
print("=" * 50)
print("Imp Rules: Type 'QUIT' anytime if you want to exit with current money!")
time.sleep(2)
print("\nSaare Questions screen par aane jaa rahe hain.....\n")

question = [
    [
        "Which programming language is known as the backbone of AI and ML?",
        "A. Java",
        "B. Python",
        "C. JavaScript",
        "D. C++",
        "B",  # Python
        1000,
    ],
    [
        "What is the output of 2 ** 3 in Python?",
        "A. 6",
        "B. 8",
        "C. 9",
        "D. 5",
        "B",
        5000,
    ],
    [
        "Which of the following is an immutable data type in Python?",
        "A. List",
        "B. Dictionary",
        "C. Set",
        "D. Tuple",
        "D",
        10000,
    ],
    [
        "Who founded Python programming language?",
        "A. Guido van Rossum",
        "B. Elon Musk",
        "C. Dennis Ritchie",
        "D. James Gosling",
        "A",
        50000,
    ],
    [
        "Which keyword is used to handle exceptions in Python?",
        "A. try",
        "B. catch",
        "C. throw",
        "D. handle",
        "A",
        100000,
    ],
]

total_win_Amount = 0
game_over = False

# Same loop for all questions 
for i, q_data in enumerate(question, start=1):
    ques_text = q_data[0]
    opt_a, opt_b, opt_c, opt_d = q_data[1], q_data[2], q_data[3], q_data[4]
    ques_ans = q_data[5]
    ques_money = q_data[6]

    time.sleep(2)
    print("-" * 50)
    print(f"Question No. {i} for ₹{ques_money:,}")
    print(f"Q: {ques_text}")
    print(f"{opt_a} {opt_b}")
    print(f"{opt_c} {opt_d}")
    print("-" * 50)

    #user input loop for valid answer.
    while True:
        user_choice = (
            input("Enter your Answer (A, B, C, D) or 'QUIT': ").strip().upper()
        )
        if user_choice in ["A", "B", "C", "D", "QUIT"]:
            break
        print("Invalid input! Please choose among A, B, C, D or 'QUIT'.")

    # If you want to Quit
    if user_choice == "QUIT":
        print(f"\nAapne khel chhodne ka faisla kiya!")
        print(f"Congratulations! You are taking home: ₹{total_win_Amount:,}")
        game_over = True
        break

    # If your answer is correct
    elif user_choice == ques_ans:
        total_win_Amount = ques_money
        print(f"\nSahi Jawab! Aap jeet chuke hain ₹{total_win_Amount:,} !!\n")

    # If your answer is wrong
    else:
        print(f"\nAfsos! Galat Jawab. Sahi uttar tha Option {ques_ans}.")
        loss_amount = total_win_Amount // 2 if total_win_Amount > 1000 else 0
        print(f"Aapka khel yahin samapt hota hai. Take-home amount: ₹{loss_amount:,}")
        game_over = True
        break

# Loop khatam hone ke baad final check
if not game_over:
    print("\n" + "=" * 50)
    print("DHAMAKEDAR VICTORY! Aapne saare sawalon ke sahi jawab diye.")
    print(f"Total Amount that you are taking home: ₹{total_win_Amount:,}")
    print("=" * 50)
