def getOutputText(inputText):
    # 업무 관련
    if inputText == "시작":
        return "인녕하세요! Ted_bot 입니다.레드윗에 온 것을 환영해요~~제가 회사에 궁금한 사항을 자세히 알려드릴테니 걱정마세요!저와 같이 회사에 잘 적응해 봐요!"
    elif inputText == "슬로건":
        return "Prove Your Work!레드윗은 \"모든 과정을 증명하고 그 가치를 보장하는 세상\"을 꿈꿉니다.지금 세상은 과정을 증명하고, 그 가치를 인정받기가 매우 힘듭니다.레드윗은 이러한 문제를 해결하고, 일의 과정이 쉽게 증명되고 그 가치가 인정되기 위해 사람들을 도와주는 서비스를 세상에 선보이고 자 합니다."
    elif inputText == "조직문화":
        return "Respect직급, 나이, 성별에 관계없이 모두가 의견을 낼 수 있고,모든 의견은 존중받습니다.Responsibility개인이 업무에 대한 독립적인 의사결정을 내릴 수 있고,이에 따른 책임을 갖습니다.Contribute모두가 프로젝트의 목표에 기여가 되는 방향으로의사결정을 내립니다.Communication모두가 같은 이해도로 정보를 알 수 있는 효율적인커뮤니케이션을 합니다."
    elif inputText == "호칭":
        return "레드윗은 직급과 님자를 붙이지 않고영어 닉네임으로 부릅니다.예) 테드 이건 어떻게 해야 될까요?레드윗은 상하, 나이 관계없이 모두 존댓말로 소통을 합니다.존댓말은 꼭 해주세요!"
    elif inputText == "회식":
        return "레드윗은 별도의 저녁 회식은 공식적으로 존재하지 않습니다.1주에 한번 팀 점심을 진행하며, 월 1회 \"문화의 날\"행사를 통해 레드윗 직원 모두가 점심을 먹습니다.[팀 별 점심 요일]월요일: 마케팅팀화요일: 개발팀수요일: 기획, 경영팀금요일: 영업"
    elif inputText == "문화의 날":
        return "문화의 날은 분기별로 EM(Event managers)를 뽑아서기획하여 진행합니다.지금까지 진행했던 문화의 날은 아래 링크를 통해 볼 수 있습니다.https://www.notion.so/redwit/ReDWit-a7147057928c4025a40b7ef590d125a5"
    elif inputText == "근무":
        return "레드윗은 주 40시간, 자율 출퇴근고정적인 출/퇴근 시간 없이,주 40시간 기준으로 편한 시간에 출근하셔도 됩니다.(팀마다 core time이 있으니 이건 팀에서 확인해주세요)2.  출퇴근 찍는 법레드윗은 출퇴근을 메신저(slack)을 통해 진행합니다.https://www.notion.so/redwit/5b3bac5487794585b3dc9ec819e171ec사용법을 확인해 주세요!3. 원격근무원격 근무 시, 슬랙을 활용하여 원격 근무 환경에 대해공유만 해주시면, 어디서든 근무 가능합니다.(고정 미팅은 오피스에서 진행)"
    elif inputText == "미팅":
        return "1. Sprint Meeting매주 월요일, 팀별 시간이 다르며 매주 개인 업무 진행 사항과 앞으로 할 일 공유 및 회고, OKR 진척도 체크2. Leader Meeting매주 금요일 오후 2시 각 팀장 + PM 한 주간 이슈 체크 및 협의 필요한 부분 논의3. 테디매월 테드와 선택적으로 하는 1:1 미팅4. Retro매월 첫 주 수요일 11시 전체 레트로 미팅, PM 전체 진행사항 발표, 팀 별 발표"
    elif inputText == "인사명부":
        return "경영지원팀: 세라, 해리, 티나 PM: 테드 개발팀: 티모(팀장), 아이작, 라이카, 조던, 둘리. 아이번 영업팀: 아리아나(팀장), 이든, 레이, 카이 마케팅팀: 알리(팀장), 제이, 릴리 기획팀: 팩맨(팀장),조이, 제리https://www.notion.so/redwit/f78558983fde4d5fbf6f01d6e0e8cb95?v=5d25e47c397f44bd82c0bdc28d3d915e"
    elif inputText == "구노":
        return "구노는 기업/기관 등 내에서 연구 과정을 쉽게 증명할 수 있게 도와주는 전자 연구 노트 입니다.서비스 소개서 보러가기 ->https://www.notion.so/redwit/GOONO-2023-01-859d9a1d479a4920a96e4ae554c5dcaf"
    # 사무실 관련
    elif inputText == "휴지 어딨어" or inputText == "휴지 어딨어?" or inputText == "휴지 어디에 있어?" or inputText == "휴지":
        return "휴지는 3층 싱크대 밑에 서랍을 열어 보시면 있습니다. 자 그럼 싱크대로 출발 해볼까요?"
    elif inputText == "건전지 어딨어" or inputText == "건전지 어딨어?" or inputText == "건전지" or inputText == "건전지 위치":
        return "건전지는 세라방 바로 옆에 있는 책상에 있어요! 만약에 거기에도 없다면 티나, 테드에게 슬랙 보내주세요."
    elif inputText == "회의실 이름":
        return "회의실은 총 4개로 나뉘어져 있습니다. 1. 전체 회의공간(2층, 티비와 책상이 있는곳) 2. 그린룸(그린색 회의실), 3. 블루룸(블루색 회의실), 핑크룸(핑크색 회의실) 회의실 문 색이 회의실에 이름이에요, 참 쉽죠? 자 그럼 이제 회의하러 출발!"
    elif inputText == "수면실" or inputText == "수면실 써도 돼?" or inputText == "수면실 사용":
        return "수면실은 2층에 있으니 자유롭게 써주시고 나오실 때는 꼭 이불 정리를 해주세요. 이불 정리 안 하면 집까지 쫒아갑니다??ㅋㅋ"
    elif inputText == "마케팅팀":
        return "팀장: 알리 팀원: 제이, 릴리"
    elif inputText == "개발팀":
        return "팀장: 티모 팀원: 아이작, 라이카, 조던, 둘리, 아이번, 포든"
    elif inputText == "기획팀":
        return "팀장: 공석 팀원: 조이, 제시, 제리"
    elif inputText == "영업팀":
        return "팀장: 아리아나 팀원: 이든, 레이, 카이"
    elif inputText == "경영팀":
        return "세라, 해리, 티나"
    # 업무 외
    elif inputText == "피곤하다" or inputText == "피곤":
        return "그러니까 어제 일찍 자라고 했어! 안 했어! \n자 커피 한잔 하고 다시 일하자"
    elif inputText == "멍청이":
        return "나한테 멍청이라고 했니?? 똥멍충이야? ㅋㅋㅋ"
    elif inputText == "바보":
        return "나는 말로 안해 ㅋㅋ"
    elif inputText == "안녕":
        return "안녕하세요 저는 테드봇입니다. 무엇을 도와드릴까요?"
    else:
        return "테드봇이 알아들을 수 없는 말입니다 ㅜㅜ"