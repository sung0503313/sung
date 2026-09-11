import tkinter as tk
import random
quiz_used = []

# =========================================================
# 게임 설정
# =========================================================

stages = [
    {"name": "직원", "length": 3, "attempts": 5},
    {"name": "팀장", "length": 3, "attempts": 4},
    {"name": "임원", "length": 4, "attempts": 3},
    {"name": "CEO", "length": 4, "attempts": 3}
]


# =========================================================
# 게임 변수
# =========================================================

current_stage = 0
attempts = 0
quiz_fail = 0
total_fail = 0

password = ""
clues = []
revealed_hints = 1

popup = None
quiz_win = None


# =========================================================
# 메인 창
# =========================================================

window = tk.Tk()

window.title("HACKING SYSTEM")

window.attributes("-fullscreen", True)

window.configure(bg="black")


# =========================================================
# ESC 키
# =========================================================

def exit_fullscreen(event=None):
    window.attributes("-fullscreen", False)


window.bind("<Escape>", exit_fullscreen)


# =========================================================
# 첫 번째 화면
# 작가의 말
# =========================================================

writer_frame = tk.Frame(
    window,
    bg="white"
)

writer_frame.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)


writer_title = tk.Label(
    writer_frame,
#이거는 타이틀!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    text="작가의 말",
    bg="white",
    fg="black",
    font=("맑은 고딕", 28, "bold")
)

writer_title.pack(pady=20)

#여따가 작가의말 적기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
writer_text = """
우리는 매일 인터넷과 디지털 기기를 사용하며 수많은 정보를 남기고 있습니다. 검색 기록부터 사진, 계정 정보, 개인정보까지 우리가 생각하는 것보다 훨씬 많은 정보가 온라인에 저장되어 있습니다. 하지만 이러한 정보가 제대로 보호되지 않는다면 작은 보안 취약점 하나만으로도 큰 피해가 발생할 수 있습니다.

이 게임을 통해 해킹과 정보보안에 대해 조금 더 쉽게 이해하고, 우리가 평소 아무렇지 않게 사용하는 개인정보와 데이터가 얼마나 중요한지 생각해보았으면 합니다. 보안은 전문가들만 신경 써야 하는 것이 아니라 인터넷을 사용하는 모든 사람이 관심을 가져야 하는 문제이기 때문입니다.

또한 해킹 기술은 어떻게 사용하느냐에 따라 피해를 일으킬 수도 있고, 반대로 시스템의 취약점을 찾아 더 안전하게 만드는 데 사용될 수도 있습니다. 실제 정보보안 분야에서는 공격자의 입장에서 시스템을 분석하고 문제점을 찾아내는 과정도 중요합니다. 결국 중요한 것은 기술 자체가 아니라 그 기술을 어떤 목적으로 사용하고, 그 결과에 얼마나 책임을 지느냐라고 생각합니다.

게임 속에서는 비밀번호 하나를 추측하는 것이 단순한 재미로 느껴질 수 있지만, 실제 상황에서는 하나의 계정이 개인의 소중한 정보나 기업의 중요한 자료와 연결되어 있을 수도 있습니다. 그렇기 때문에 강력한 비밀번호를 사용하고 개인정보를 함부로 공개하지 않는 등 작은 보안 습관부터 실천하는 것이 중요합니다.

기술이 발전할수록 정보를 지키는 보안의 중요성도 함께 커집니다. 여러분이 이 게임을 재미있게 플레이하면서 해킹의 위험성과 정보보안의 필요성을 조금이나마 느끼고, 우리가 만들어가는 디지털 세상을 어떻게 안전하게 지켜나갈 수 있을지 한 번쯤 생각해보길 바랍니다.
"""


tk.Label(
    writer_frame,
    text=writer_text,
    bg="white",
    fg="black",
    font=("맑은 고딕", 15),
    justify="left",
    wraplength = 750
).pack(pady=20)


# =========================================================
# 게임 설명 화면으로 이동
# =========================================================

def show_game_info():

    writer_frame.place_forget()

    info_frame.place(
        x = 0,
        y = 0,
        relwidth = 1,
        relheight = 1
    )


# =========================================================
# 첫 번째 시작 버튼
# =========================================================

tk.Button(
    writer_frame,
    text="게임 시작",
    command=show_game_info,
    bg="black",
    fg="white",
    font=("맑은 고딕", 15),
    width=18,
    height=2
).pack(pady=30)


# =========================================================
# 게임 설명 화면
# =========================================================

info_frame = tk.Frame(
    window,
    bg="black"
)


info_text = """
[ MISSION BRIEFING ]

당신은 기업 내부의 보안 시스템에 침투하여
중요한 기밀 정보를 찾아내야 합니다.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ PLAY GUIDE ]

• 각 스테이지마다 비밀번호를 추리합니다.

• 비밀번호를 틀릴 때마다
  새로운 힌트가 공개됩니다.

• 입력한 숫자가 정답보다 작으면

        ▲ UP

• 입력한 숫자가 정답보다 크면

        ▼ DOWN

• 제한 횟수를 초과하면
  SECURITY QUIZ가 시작됩니다.

• 퀴즈를 3회 실패하면
  처음부터 다시 시작할지 선택합니다.

• 총 12회 이상 실패하면
  다음 스테이지로 건너뛸 수 있습니다.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ STAGE ]

직원 → 팀장 → 임원 → CEO


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

목표는 CEO 계정까지 침투하는 것입니다.

행운을 빕니다.
"""


tk.Label(
    info_frame,
    text=info_text,
    bg="black",
    fg="lime",
    font=("Courier", 13),
    justify="left"
).pack(pady=30)


# =========================================================
# 게임 화면
# =========================================================

game_frame = tk.Frame(
    window,
    bg="black"
)


# =========================================================
# 게임 제목
# =========================================================

title = tk.Label(
    game_frame,
    text="💻 HACKING SYSTEM",
    bg="black",
    fg="lime",
    font=("Courier", 28, "bold")
)

title.pack(pady=25)


# =========================================================
# 로그 창
# =========================================================

log = tk.Text(
    game_frame,
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Courier", 12),
    width=90,
    height=25
)

log.pack(pady=20)


# =========================================================
# 비밀번호 입력
# =========================================================

entry = tk.Entry(
    game_frame,
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Courier", 22),
    width=20
)

entry.pack(pady=10)


# =========================================================
# 로그 출력 함수
# =========================================================

def log_message(msg):

    log.insert(
        tk.END,
        msg + "\n"
    )

    log.see(tk.END)


# =========================================================
# 비밀번호 생성
# =========================================================

def generate_password(length):

    password = ""

    for i in range(length):
        password += str(random.randint(0, 9))

    return password


# =========================================================
# 힌트 생성
# =========================================================

def generate_clues(pw):

    result = []

    # 힌트 1
    result.append(
        f"숫자의 합은 {sum(map(int, pw))}이다."
    )

    # 힌트 2
    if int(pw[0]) > int(pw[-1]):

        result.append(
            "첫 번째 숫자가 마지막 숫자보다 크다."
        )

    else:

        result.append(
            "첫 번째 숫자가 마지막 숫자보다 작거나 같다."
        )

    # 힌트 3
    even_count = 0

    for number in pw:

        if int(number) % 2 == 0:
            even_count += 1

    result.append(
        f"짝수는 {even_count}개 포함되어 있다."
    )

    # 힌트 4
    digit = random.choice(pw)

    result.append(
        f"{digit}이라는 숫자가 포함되어 있다."
    )

    # 힌트 5
    result.append(
        f"(강력한 힌트) 앞자리는 "
        f"{pw[:len(pw)//2]}이다."
    )

    return result


# =========================================================
# 스테이지 시작
# =========================================================

def start_stage():

    global password
    global attempts
    global total_fail
    global revealed_hints
    global clues

    stage = stages[current_stage]

    password = generate_password(
        stage["length"]
    )

    attempts = 0
    total_fail = 0
    revealed_hints = 1

    clues = generate_clues(password)

    log.delete(
        "1.0",
        tk.END
    )

    log_message(
        "=========================================="
    )

    log_message(
        f"[ MISSION ] {stage['name']} 계정 침투"
    )

    log_message(
        "=========================================="
    )

    log_message("")

    log_message(
        f"[INFO] 비밀번호 길이 : {stage['length']}자리"
    )

    log_message(
        f"[INFO] 제한 횟수 : {stage['attempts']}회"
    )

    log_message("")

    log_message("[ CLUE 01 ]")

    log_message(
        "▶ " + clues[0]
    )

    log_message("")

    log_message(
        "[TIP] 숫자가 정답보다 작으면 UP"
    )

    log_message(
        "[TIP] 숫자가 정답보다 크면 DOWN"
    )

    log_message("")

    log_message(
        "[SYSTEM] 비밀번호를 입력하십시오."
    )

    entry.config(
        state="normal"
    )

    button.config(
        state="normal"
    )

    entry.delete(
        0,
        tk.END
    )

    entry.focus_set()


# =========================================================
# 다음 스테이지
# =========================================================

def next_stage():

    global current_stage

    current_stage += 1

    if current_stage >= len(stages):

        ending_success()

    else:

        start_stage()


# =========================================================
# 비밀번호 확인
# =========================================================

def check_password():

    global attempts
    global total_fail
    global revealed_hints

    stage = stages[current_stage]

    user_input = entry.get().strip()

    entry.delete(
        0,
        tk.END
    )

    if user_input == "":

        log_message(
            "⚠ 숫자를 입력하십시오."
        )

        entry.focus_set()

        return

    if not user_input.isdigit():

        log_message(
            "⚠ 숫자만 입력할 수 있습니다."
        )

        entry.focus_set()

        return

    # =====================================================
    # 0000 마스터 코드
    # =====================================================

    if user_input == "0000":

        log_message("")

        log_message(
            "🔓 MASTER CODE DETECTED"
        )

        log_message(
            "⚠ 관리자 우회 코드 확인"
        )

        log_message(
            "✅ ACCESS GRANTED"
        )

        next_stage()

        return

    # =====================================================
    # 시도 횟수 증가
    # =====================================================

    attempts += 1

    total_fail += 1

    # =====================================================
    # 정답
    # =====================================================

    if user_input == password:

        log_message("")

        log_message(
            "✅ ACCESS GRANTED"
        )

        log_message(
            f"[SYSTEM] {stage['name']} 계정 침투 성공"
        )

        next_stage()

        return

    # =====================================================
    # 오답
    # =====================================================

    log_message("")

    log_message(
        f"❌ ACCESS DENIED "
        f"({attempts}/{stage['attempts']})"
    )

    # =====================================================
    # UP / DOWN
    # =====================================================

    user_number = int(user_input)

    correct_number = int(password)

    if user_number < correct_number:

        log_message(
            "⬆ UP"
        )

        log_message(
            "▶ 정답이 입력한 숫자보다 큽니다."
        )

    else:

        log_message(
            "⬇ DOWN"
        )

        log_message(
            "▶ 정답이 입력한 숫자보다 작습니다."
        )

    # =====================================================
    # 새로운 힌트
    # =====================================================

    if revealed_hints < len(clues):

        log_message("")

        log_message(
            "💡 새로운 힌트 공개!"
        )

        log_message(
            "▶ " + clues[revealed_hints]
        )

        revealed_hints += 1

    # =====================================================
    # 12회 실패
    # =====================================================

    if total_fail >= 12 and current_stage != 3:

        ask_skip()

        return

    # =====================================================
    # 제한 횟수 초과
    # =====================================================

    if attempts >= stage["attempts"]:

        log_message("")

        log_message(
            "🔒 ACCOUNT LOCKED"
        )

        log_message(
            "추가 인증이 필요합니다."
        )

        entry.config(
            state="disabled"
        )

        button.config(
            state="disabled"
        )

        open_quiz()


# =========================================================
# 스킵 팝업
# =========================================================

def ask_skip():

    global popup

    if popup is not None:
        return

    popup = tk.Toplevel(window)

    popup.title(
        "SYSTEM WARNING"
    )

    popup.geometry(
        "500x280"
    )

    popup.configure(
        bg="black"
    )

    popup.grab_set()

    popup.protocol(
        "WM_DELETE_WINDOW",
        lambda: None
    )

    tk.Label(
        popup,
        text=(
            "⚠ SYSTEM WARNING ⚠\n\n"
            "실패 횟수가 너무 많습니다.\n\n"
            "다음 스테이지로 넘어가시겠습니까?"
        ),
        fg="lime",
        bg="black",
        font=("Courier", 13)
    ).pack(pady=35)

    def yes():

        global popup
        global total_fail

        total_fail = 0

        popup.grab_release()
        popup.destroy()

        popup = None

        next_stage()

    def no():

        global popup
        global revealed_hints

        popup.grab_release()
        popup.destroy()

        popup = None

        log_message("")

        log_message(
            "💡 추가 힌트를 제공합니다."
        )

        if revealed_hints < len(clues):

            log_message(
                "▶ " + clues[revealed_hints]
            )

            revealed_hints += 1

        else:

            log_message(
                "💡 더 이상 공개할 힌트가 없습니다."
            )

        entry.config(
            state="normal"
        )

        button.config(
            state="normal"
        )

        entry.focus_set()

    frame = tk.Frame(
        popup,
        bg="black"
    )

    frame.pack()

    tk.Button(
        frame,
        text="YES",
        command=yes,
        bg="black",
        fg="lime",
        width=12
    ).pack(
        side="left",
        padx=15
    )

    tk.Button(
        frame,
        text="NO",
        command=no,
        bg="black",
        fg="lime",
        width=12
    ).pack(
        side="left",
        padx=15
    )


# =========================================================
# 보안 퀴즈
# =========================================================

def open_quiz():

    global quiz_fail
    global quiz_win

    
    quiz_fail = 0

    quiz_win = tk.Toplevel(window)

    quiz_win.title(
        "SECURITY QUIZ"
    )

    quiz_win.geometry(
        "550x330"
    )

    quiz_win.configure(
        bg="black"
    )

    quiz_win.grab_set()

    quiz_win.protocol(
        "WM_DELETE_WINDOW",
        lambda: None
    )

    quizzes = [

        ("행운을 시험해봅시다! 1, 2, 3 중 택 1", "2"),

        ("조선의 21대 왕은?", "영조"),

        ("임진왜란이 일어난 해는?", "1592"),

        ("태양계에서 가장 큰 행성은?", "목성"),

        ("행운을 시험해봅시다! 제작자가 태어난 연도는? (숫자만)", "2010"),

        ("식물세포에 있고 동물세포에 없는 구조는?", "세포벽"),

        ("??은 이 당백전의 당을 된발음으로 땅으로하여 땅돈이라 한것에서 비롯되었는데, 당백전 가치가 형편 없다는 뜻이었다. ??은? ", "땡전"),
        
        ("넌센스 : 눈이 좋은 사슴을 영어로?\n(띄어쓰기X)", "굿아이디어"),

        ("최초의 한글 소설은?", "홍길동전"),

        ("오늘날 표준이 되는 피아노의 건반 개수는 몇 개? (숫자만)", "88"),

        ("스승의 날인 5월 15일은 누구의 생일에서 유래했을까?", "세종대왕"),

        ("학교폭력 상담 전화번호는?", "117"),

        ("덧셈, 뺄샘, 곱셈, 나눗셈의 네 종류의 계산법을 뭐라고 하는가?", "사칙연산"),

        ("이탈리아의 수도는?", "로마"),

        ("'남산 위에 저 소나무 ㅇㅇ을 두른듯~'\n다음은 애국가의 2절 가사이다. 빈칸에 들어갈 단어는?", "철갑"),

        ("나이아가라 폭포는 어느 나라에 있을까요?", "캐나다"),

        ("아기돼지 삼형제에서 둘째 돼지가 지은 집은 무엇일까요?", "나무집"),

        ("한자 冬(동)은 무슨 뜻일까요?", "겨울"),

        ("이 프로그램은 무슨 컴퓨터언어로 만들어졌을까요?", "파이썬"),

        ("대한민국의 수도는?", "서울"),

        ("지구에서 가장 큰 대양은?", "태평양"),

        ("1년은 몇 개월인가?", "12"),

        ("우리나라의 국기는?", "태극기"),

        ("물의 끓는점은 섭씨 몇 도인가?", "100"),

        ("태양계에서 가장 큰 행성은?", "목성"),

        ("무지개의 색은 몇 가지인가?", "7"),

        ("한글을 만든 왕은?", "세종대왕"),

        ("지구의 위성은?", "달"),

        ("대한민국의 화폐 단위는?", "원"),

        ("세계에서 가장 높은 산은?", "에베레스트"),

        ("사람의 심장은 몇 개인가?", "1"),

        ("삼각형의 변은 몇 개인가?", "3"),

        ("우리나라의 국화는?", "무궁화"),

        ("태양은 무엇인가?", "항성"),

        ("1시간은 몇 분인가?", "60"),

        ("지구는 태양 주위를 도는 데 약 며칠이 걸리는가?", "365"),

        ("영어 알파벳은 모두 몇 글자인가?", "26")

    ]

    unused_quizzes = [q for q in quizzes if q not in quiz_used]

    if not unused_quizzes:
        quiz_used.clear()
        unused_quizzes = quizzes.copy()

    quiz = random.choice(unused_quizzes)
    quiz_used.append(quiz)

    question = quiz[0]
    answer = quiz[1]

    tk.Label(
        quiz_win,
        text="[ SECURITY QUIZ ]",
        fg="lime",
        bg="black",
        font=("Courier", 17)
    ).pack(pady=20)

    tk.Label(
        quiz_win,
        text=question,
        fg="lime",
        bg="black",
        font=("Courier", 12),
        wraplength=500
    ).pack(pady=10)

    answer_entry = tk.Entry(
        quiz_win,
        bg="black",
        fg="lime",
        insertbackground="lime",
        font=("Courier", 14),
        width=25
    )

    answer_entry.pack(pady=10)

    def verify():

        global quiz_fail

        user_answer = (
            answer_entry.get()
            .strip()
            .lower()
        )

        if user_answer == answer.lower():

            log_message("")

            log_message(
                "✅ SECURITY QUIZ PASSED"
            )

            log_message(
                "🔓 ACCOUNT UNLOCKED"
            )

            quiz_win.grab_release()
            quiz_win.destroy()

            entry.config(
                state="normal"
            )

            button.config(
                state="normal"
            )

            entry.focus_set()

            return

        quiz_fail += 1

        log_message(
            f"❌ 인증 실패 ({quiz_fail}/3)"
        )

        answer_entry.delete(
            0,
            tk.END
        )

        if quiz_fail == 2:

            log_message(
                "⚠ 마지막 기회입니다."
            )

        if quiz_fail >= 3:

            quiz_win.grab_release()
            quiz_win.destroy()

            open_retry_popup()

    tk.Button(
        quiz_win,
        text="VERIFY",
        command=verify,
        bg="black",
        fg="lime",
        width=12
    ).pack(pady=15)

    answer_entry.bind(
        "<Return>",
        lambda event: verify()
    )

    answer_entry.focus_set()


# =========================================================
# 재시작 여부
# =========================================================

def open_retry_popup():

    global popup

    popup = tk.Toplevel(window)

    popup.title(
        "SYSTEM LOCK"
    )

    popup.geometry(
        "520x300"
    )

    popup.configure(
        bg="black"
    )

    popup.grab_set()

    popup.protocol(
        "WM_DELETE_WINDOW",
        lambda: None
    )

    tk.Label(
        popup,
        text=(
            "⚠ AUTHENTICATION FAILED ⚠\n\n"
            "인증에 3회 실패했습니다.\n\n"
            "처음부터 다시 시작하시겠습니까?"
        ),
        fg="lime",
        bg="black",
        font=("Courier", 13)
    ).pack(pady=40)

    def restart():

        global popup

        popup.grab_release()
        popup.destroy()

        popup = None

        reset_game()

    def exit_game():

        window.destroy()

    frame = tk.Frame(
        popup,
        bg="black"
    )

    frame.pack()

    tk.Button(
        frame,
        text="YES",
        command=restart,
        bg="black",
        fg="lime",
        width=12
    ).pack(
        side="left",
        padx=15
    )

    tk.Button(
        frame,
        text="NO",
        command=exit_game,
        bg="black",
        fg="lime",
        width=12
    ).pack(
        side="left",
        padx=15
    )


# =========================================================
# 게임 리셋
# =========================================================

def reset_game():

    global current_stage
    global attempts
    global quiz_fail
    global total_fail

    current_stage = 0
    attempts = 0
    quiz_fail = 0
    total_fail = 0

    start_stage()


# =========================================================
# 엔딩
# =========================================================

def ending_success():

    log.delete(
        "1.0",
        tk.END
    )

    entry.config(
        state="disabled"
    )

    button.config(
        state="disabled"
    )

    log_message(
        "=========================================="
    )

    log_message(
        "[ ACCESS GRANTED ]"
    )

    log_message(
        "=========================================="
    )

    log_message("")

    log_message(
        "[DATA DOWNLOADING...]"
    )

    window.after(
        1000,
        lambda: log_message(
            "[NEWS] 회사 기밀 유출 발생"
        )
    )

    window.after(
        2000,
        lambda: log_message(
            "[REPORT] 회사 내부 정보 대량 유출"
        )
    )

    window.after(
        3000,
        lambda: log_message(
            "[REPORT] 회사 파산 위기"
        )
    )

    window.after(
        4500,
        lambda: log_message(
            "이번엔... 어떤 정보를 털어볼까?"
        )
    )

    # 큰 CLEAR 화면
    window.after(
        6500,
        show_clear_screen
    )


# =========================================================
# CLEAR 화면
# =========================================================

def show_clear_screen():

    clear_frame = tk.Frame(
        window,
        bg="black"
    )

    clear_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    tk.Label(
        clear_frame,
        text="GAME CLEAR",
        bg="black",
        fg="lime",
        font=("Courier", 55, "bold")
    ).pack(pady=20)

    tk.Label(
        clear_frame,
        text="3초 후 게임이 종료됩니다.",
        bg="black",
        fg="white",
        font=("Courier", 15)
    ).pack()

    # 3초 후 종료
    window.after(
        3000,
        window.destroy
    )


# =========================================================
# 게임 시작
# =========================================================

def start_game():

    info_frame.place_forget()

    game_frame.place(
        x = 0,
        y = 0,
        relwidth = 1,
        relheight = 1
    )

    start_stage()

    window.after(
        200,
        lambda: entry.focus_set()
    )


# =========================================================
# 게임 설명 화면의 시작 버튼
# =========================================================

tk.Button(
    info_frame,
    text="START HACKING",
    command=start_game,
    bg="black",
    fg="lime",
    font=("Courier", 16),
    width=20,
    height=2
).pack(pady=20)


# =========================================================
# ACCESS 버튼
# =========================================================

button = tk.Button(
    game_frame,
    text="ACCESS",
    command=check_password,
    bg="black",
    fg="lime",
    font=("Courier", 14),
    width=15
)

button.pack(pady=5)


# =========================================================
# Enter 키
# =========================================================

entry.bind(
    "<Return>",
    lambda event: check_password()
)


# =========================================================
# 처음에는 게임 화면 숨기기
# =========================================================

game_frame.place_forget()


# =========================================================
# 실행
# =========================================================

window.mainloop()
