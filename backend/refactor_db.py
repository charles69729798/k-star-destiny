import sys
import os

engine_file = r"c:\InsuranceProject\Sajuapp\backend\saju_engine.py"
i18n_file = r"c:\InsuranceProject\Sajuapp\backend\saju_i18n.py"

with open(engine_file, 'r', encoding='utf-8') as f:
    engine_content = f.read()
    
# Find ENERGY_TRAITS and replace it with modular structure
new_energy_traits_ko = '''ENERGY_TRAITS = {
    "Wood": {
        "name": "성장하는 나무(Wood) 🌲",
        "desc_intro": [
            "당신의 영혼은 끝없이 뻗어 나가는 '큰 나무(거목)'의 에너지를 품고 태어났습니다. 명리학에서 목(木) 기운은 생명력, 호기심, 그리고 굽히지 않는 성장 욕구를 의미합니다.",
            "싹을 틔우고 쑥쑥 자라나는 새싹처럼, 무한한 가능성과 시작의 파동을 가진 목(木) 기운을 타고났습니다."
        ],
        "desc_core": {
            "E": [
                "완벽한 인싸 재질이자 자기계발 폼이 미친 '갓생러'입니다. 세상의 모든 것에 흥미를 느끼며, 시작하는 것을 두려워하지 않는 추진력의 아이콘이죠. 때로는 오지랖이 넓다는 소리를 듣기도 하지만, 그 이면에는 사람을 향한 따뜻한 애정과 '다 같이 잘 헤쳐 나가자'는 긍정적인 포용력이 자리 잡고 있습니다.",
                "가만히 있지 못하고 끊임없이 새로운 일을 벌이는 에너자이저! 당신 주위에는 늘 사람이 끊이지 않으며 특유의 오지랖으로 주변을 긍정적으로 변화시킵니다."
            ],
            "I": [
                "조용하지만 내면의 성장을 향한 욕구가 누구보다 강렬한 외유내강형 인간입니다. 하나의 관심사에 딥다이브하며 조용히 실력을 키워나가는 대기만성형 갓생러입니다.",
                "겉으로는 유연해 보이지만 당신의 신념을 건드리는 순간 거목처럼 굳건하게 맞서는 고집이 숨어 있습니다. 혼자만의 시간을 통해 나이테를 단단하게 새기는 타입입니다."
            ],
            "default": [
                "완벽한 인싸 재질이자 자기계발 폼이 미친 '갓생러'입니다. 세상의 모든 것에 흥미를 느끼며, 시작하는 것을 두려워하지 않는 추진력의 아이콘이죠. 때로는 오지랖이 넓다는 소리를 듣기도 하지만, 그 이면에는 사람을 향한 따뜻한 애정과 '다 같이 잘 헤쳐 나가자'는 긍정적인 포용력이 자리 잡고 있습니다. \\n\\n기본적으로 유연해 보이지만, 당신의 신념을 건드리는 순간 거목처럼 굳건하게 맞서는 고집(자존심)도 숨어 있습니다. 이 고집이 당신을 지탱하는 강력한 무기이자 매력 포인트입니다."
            ]
        },
        "desc_career": [
            "[직업 및 라이프스타일]\\n한자리에 가만히 있는 것보다는 끊임없이 새로운 프로젝트를 기획하고, 사람들과 교류하며 아이디어를 팽창시키는 직무가 찰떡입니다. 스타트업 창업, 에디터, 크리에이터, 기획자 등 '무에서 유를 창조하는' 역할에서 도파민을 강력하게 느낍니다. 워라밸보다는 역동적인 성취감이 영혼을 춤추게 합니다.",
            "[직업 및 라이프스타일]\\n성장과 교육에 관련된 분야에서 도파민을 강력하게 느낍니다. 누군가를 가르치거나 멘토링하는 역할, 혹은 생동감 넘치는 스타트업 무대가 당신의 성장을 돕습니다."
        ],
        "desc_advice": [
            "[운명 개척 액션 플랜]\\n시작은 거창하나 마무리가 흐지부지될 위험(용두사미)이 항상 도사리고 있습니다. 나무가 예쁘게 자라려면 주기적인 가지치기가 필수이듯, 관심사를 좁히고 하나의 목표에 딥다이브하는 연습이 필요합니다.",
            "[운명 개척 액션 플랜]\\n바람에 흔들리는 것을 두려워하지 마세요. 가끔은 실패하더라도 꺾이지 않고 다시 새순을 돋게 하는 당신만의 탄력성이 가장 큰 무기입니다."
        ]
    },
    "Fire": {
        "name": "불타오르는 불(Fire) 🔥",
        "desc_intro": [
            "당신의 영혼은 세상을 밝게 비추는 '태양' 혹은 어둠 속의 '횃불' 에너지를 품고 태어났습니다. 명리학에서 화(火) 기운은 열정, 확산, 화려함, 그리고 감정을 숨기지 못하는 투명함을 의미합니다.",
            "주변을 환하게 밝히는 한 줄기 빛처럼, 숨길 수 없는 존재감과 에너지를 뿜어내는 화(火) 기운의 소유자입니다."
        ],
        "desc_core": {
            "E": [
                "어디를 가나 시선을 강탈하는, 존재 자체가 플러팅인 '핵인싸'입니다. 텐션이 기본적으로 MAX에 맞춰져 있으며, 리액션이 혜자스러워 주변 사람들에게 에너지를 마구 퍼주는 충전기 같은 존재입니다. 겉과 속이 매우 투명해서 뒤끝이 없고, 화가 나더라도 불꽃처럼 확 타올랐다가 금세 가라앉는 '마라맛 쿨톤' 성격입니다.",
                "사람들과 어울리는 자리에서 늘 중심에 서는 파티마스터. 빛나고 화려한 것을 좋아하며 즉흥적이고 시원시원한 매력으로 쉴 새 없이 매력을 발산합니다."
            ],
            "I": [
                "겉으로는 차분해 보일 수 있으나 내면에는 활활 타오르는 거대한 불꽃을 숨기고 있습니다. 나를 인정해주는 좁고 깊은 관계에서만 내면의 화력을 폭발시키는 따뜻한 화로같은 사람입니다.",
                "소수의 소중한 사람들에게만 밝고 따뜻한 에너지를 집중적으로 나누어주는 타입입니다. 불꽃의 심지처럼 묵묵하지만 강력한 에너지를 지닙니다."
            ],
            "default": [
                "어디를 가나 시선을 강탈하는, 존재 자체가 플러팅인 '핵인싸'입니다. 텐션이 기본적으로 MAX에 맞춰져 있으며, 리액션이 혜자스러워 주변 사람들에게 에너지를 마구 퍼주는 충전기 같은 존재입니다. 겉과 속이 매우 투명해서 뒤끝이 없고, 화가 나더라도 불꽃처럼 확 타올랐다가 금세 가라앉는 '마라맛 쿨톤' 성격입니다.\\n\\n불의 에너지는 '예의'와 '명예'를 중시합니다. 나를 인정해 주는 사람 앞에서는 한없이 따뜻하지만, 선을 넘는 사람에게는 가차 없이 불벼락을 내리는 단호함도 갖추고 있습니다."
            ]
        },
        "desc_career": [
            "[직업 및 라이프스타일]\\n무대 체질이며 스포트라이트를 받아야 잠재력이 터집니다. 남들 앞에 서는 연예인, 인플루언서, 마케터, 세일즈, 방송 관련 직무가 완벽한 시너지를 냅니다. 책상 앞에 가만히 앉아 반복적인 업무를 하는 것은 당신의 화력을 꺼뜨리는 지름길입니다.",
            "[직업 및 라이프스타일]\\n빠른 결과를 볼 수 있고 변화가 역동적인 분야에서 최대 능률을 발휘합니다. 사람의 이목을 끄는 기획이나 브랜딩, 세일즈 파트가 가장 스릴 넘치는 무대입니다."
        ],
        "desc_advice": [
            "[운명 개척 액션 플랜]\\n감정 기복이 심해 가끔 급발진을 할 때가 있습니다. 순간적인 불꽃으로 소중한 것을 태워버리지 않도록, 화가 났을 때는 '3초 심호흡' 후 말하는 습관을 들이는 것이 당신의 운명을 한 차원 높여줄 에센스입니다.",
            "[운명 개척 액션 플랜]\\n단기간에 장작을 다 태우면 번아웃이 올 수 있습니다. 지속가능한 불꽃을 위해 완급조절과 멘탈 휴식을 반드시 스케줄에 포함시키세요."
        ]
    },
    "Earth": {
        "name": "단단한 흙(Earth) ⛰️",
        "desc_intro": [
            "당신의 영혼은 만물을 온화하게 품어주는 '광활한 대지'의 에너지를 품고 태어났습니다. 명리학에서 토(土) 기운은 중재, 포용력, 신용, 그리고 묵직한 안정감을 의미합니다.",
            "계절과 계절을 이어주는 환절기처럼, 사람과 사람을 부드럽게 연결하는 대지의 기운을 가졌습니다."
        ],
        "desc_core": {
            "E": [
                "가벼움과는 거리가 먼, 멘탈 갑(甲)이자 주변 사람들이 믿고 기대는 든든한 '인간 보조배터리'입니다. 어디 치우치지 않는 평정심이 당신의 최대 무기이며, 친구들 사이에서 갈등이 생기면 최고의 중재자로 활약합니다.",
                "누구에게나 호감을 주는 푸근한 마당발입니다. 여러 무리와 어울려도 중심을 잘 잡으며, 타고난 포용력으로 인해 어디서나 환영받는 사회적 리더입니다."
            ],
            "I": [
                "무심한 척 챙겨주는 츤데레 매력이 돋보이며, 한 번 내 사람이라 생각하면 끝까지 품고 가는 의리파입니다. 속을 알 수 없는 묵직함이 오히려 든든한 매력이 됩니다.",
                "평소에 조용하고 잘 참는다고 해서 속이 없는 것은 아닙니다. 팩트를 기반으로 묵직하게 뼈를 때리는 '팩폭 장인'의 기질도 다분하며, 내 사람에게만 엄청난 희생정신을 보여줍니다."
            ],
            "default": [
                "가벼움과는 거리가 먼, 멘탈 갑(甲)이자 주변 사람들이 믿고 기대는 든든한 '인간 보조배터리'입니다. 어디 치우치지 않는 평정심이 당신의 최대 무기이며, 친구들 사이에서 갈등이 생기면 최고의 중재자로 활약합니다. 무심한 척 챙겨주는 츤데레 매력이 돋보이며, 한 번 내 사람이라 생각하면 끝까지 품고 가는 의리파입니다.\\n\\n하지만 평소에 조용하고 잘 참는다고 해서 속이 없는 것은 아닙니다. 토 기운을 가진 사람이 진짜 화를 내면 지진이 일어나는 것과 같아서 주변이 초토화될 수 있습니다. 팩트를 기반으로 묵직하게 뼈를 때리는 '팩폭 장인'의 기질도 다분합니다."
            ]
        },
        "desc_career": [
            "[직업 및 라이프스타일]\\n리스크를 즐기기보다는 차곡차곡 쌓아 올리는 것을 선호합니다. 부동산, 금융, 교육, 인사(HR), 공공기관 등 사람 사이의 균형을 맞추고 시스템을 안정화하는 일에서 큰 능력을 발휘합니다.",
            "[직업 및 라이프스타일]\\n조직의 뿌리를 단단하게 다지는 안정적인 역할에서 스트레스 없이 일합니다. 리스크 매니지먼트, 고객 관리, 그리고 여러 부서를 조율하는 PM(프로젝트 매니저) 역할에 탁월합니다."
        ],
        "desc_advice": [
            "[운명 개척 액션 플랜]\\n남들을 챙기느라 정작 자신의 감정이나 이득은 꾹꾹 눌러 담아 '한(恨)'마이크로 쌓일 수 있습니다. '나'를 우선순위의 가장 앞에 두는 이기주의가 당신에겐 가끔 필수적인 영양제입니다.",
            "[운명 개척 액션 플랜]\\n안정감을 너무 중시한 나머지 변화를 두려워할 수 있습니다. 1년에 한 번쯤은 익숙한 컴포트 존(Comfort Zone)을 부수고 나오는 엉뚱한 시도를 해보세요."
        ]
    },
    "Metal": {
        "name": "날카로운 쇠(Metal) ⚔️",
        "desc_intro": [
            "당신의 영혼은 단단하고 변하지 않는 '순백의 보석' 혹은 '날카로운 검'의 에너지를 품고 태어났습니다. 명리학에서 금(金) 기운은 결단력, 완벽주의, 의리, 그리고 냉철한 이성을 의미합니다.",
            "불순물 하나 없는 순수한 금속처럼 투명하고 날카로운 원칙을 가진 금(金)의 기운을 담았습니다."
        ],
        "desc_core": {
            "E": [
                "호불호가 명확하고, 맺고 끊음이 칼 같은 '확신의 T' 성향이 강합니다. 흐지부지하거나 감정에 호소하는 질척이는 관계를 극혐하며, 논리와 팩트가 확실할 때만 마음을 여는 냉미녀/미남 스타일입니다. 한 번 세운 원칙이나 목표는 뚝심 있게 밀고 나가는 돌파력이 엄청납니다.",
                "명확한 규칙 안에서 목표를 향해 달리는 레이서 같습니다. 불의를 보면 참지 못하며, 직설적인 화법으로 팀의 생산성을 수직 상승시키는 에이스 역할을 합니다."
            ],
            "I": [
                "겉보기엔 다가가기 힘든 얼음장벽 같지만, 사실 내면에는 '내 사람'을 끔찍이 아끼는 뜨거운 의리가 숨어 있습니다. 겉바속촉의 정석으로, 당신의 바운더리 안에 들어온 사람에게는 인생을 걸고 지켜주는 든든한 방패가 되어줍니다.",
                "홀로 조용히 완벽을 추구하는 장인정신이 빛납니다. 말수가 적고 냉정해 보이지만 한 번 맺은 의리는 목에 칼이 들어와도 지키는 진정한 로맨티스트입니다."
            ],
            "default": [
                "호불호가 명확하고, 맺고 끊음이 칼 같은 '확신의 T' 성향이 강합니다. 흐지부지하거나 감정에 호소하는 질척이는 관계를 극혐하며, 논리와 팩트가 확실할 때만 마음을 여는 냉미남/냉미녀 스타일입니다. 한 번 세운 원칙이나 목표는 주변의 시선에 굴하지 않고 뚝심 있게 밀고 나가는 돌파력이 엄청납니다.\\n\\n겉보기엔 다가가기 힘든 얼음장벽 같지만, 사실 내면에는 '내 사람'을 끔찍이 아끼는 뜨거운 의리가 숨어 있습니다. 겉바속촉의 정석으로, 당신의 바운더리 안에 들어온 사람에게는 인생을 걸고 지켜주는 든든한 방패가 되어줍니다."
            ]
        },
        "desc_career": [
            "[직업 및 라이프스타일]\\n정확한 수치와 규칙이 있는 분야에서 빛을 발합니다. IT 딥테크, 법률, 회계, 의료, 군경찰 혹은 자신만의 전문적 기술을 요구하는 장인(마이스터)의 영역이 완벽합니다. 과정보다는 '결과'로 승부하는 워커홀릭들입니다.",
            "[직업 및 라이프스타일]\\n주먹구구식 운영보다 시스템과 룰이 깔끔한 외국계 기업이나 대기업 조직 문화에 어울립니다. 분석가, 회계사, 프로그래머 등 오류를 잡아내는 직무에서 최고입니다."
        ],
        "desc_advice": [
            "[운명 개척 액션 플랜]\\n스스로에 대한 기준이 너무 높아 완벽주의의 늪에 빠질 수 있습니다. 세상을 조금은 둥글둥글하게, 때로는 빈틈을 보여주는 유연함을 탑재한다면 당신을 따르는 사람들이 배로 늘어날 것입니다.",
            "[운명 개척 액션 플랜]\\n타인에게 가하는 지나친 팩트 폭력이 당신의 평가를 깎아내릴 수 있습니다. 비판하기 전 칭찬 한 스푼을 추가하는 페르소나를 장착해 보세요."
        ]
    },
    "Water": {
        "name": "자유로운 물(Water) 🌊",
        "desc_intro": [
            "당신의 영혼은 형체가 없으나 어디든 흘러가는 '깊고 푸른 바다'의 에너지를 품고 태어났습니다. 명리학에서 수(水) 기운은 지혜, 유연성, 포용성, 그리고 헤아릴 수 없는 깊이를 의미합니다.",
            "끊임없이 흐르는 시냇물처럼 유연한 적응력과, 모든 것을 담아내는 바다 같은 수용력을 가진 수(水) 기운입니다."
        ],
        "desc_core": {
            "E": [
                "상황에 맞춰 자유자재로 모습을 바꾸는 적응력의 끝판왕입니다. 물이 어떤 모양의 그릇에든 담기듯, 당신은 어떤 환경이나 사람들에게도 부드럽게 스며드는 엄청난 소셜 스킬을 지니고 있습니다.",
                "누구와도 쉽게 친해지는 미친 친화력을 뽐냅니다. 물결치듯 유쾌하고 스펀지 같은 친화력으로 수많은 사람의 마음을 훔칩니다."
            ],
            "I": [
                "생각의 깊이가 태평양 제해권 급이며, 통찰력이 뛰어나서 남들은 못 보는 본질을 꿰뚫어 보는 '너드미'와 '철학자'의 면모를 동시에 가졌습니다. 은근한 끈기가 장난 아닌 겉유내강 스타일입니다.",
                "속마음을 잘 드러내지 않아서 '대체 무슨 생각을 하는지 모르겠다'는 신비주의 오해를 사기도 합니다. 하지만 고요한 호수 밑바닥처럼 누구보다 치열한 지적 탐구를 멈추지 않습니다."
            ],
            "default": [
                "상황에 맞춰 자유자재로 모습을 바꾸는 적응력의 끝판왕입니다. 물이 어떤 모양의 그릇에든 담기듯, 당신은 어떤 환경이나 사람들에게도 부드럽게 스며드는 엄청난 소셜 스킬을 지니고 있습니다. 생각의 깊이가 태평양 제해권 급이며, 통찰력이 뛰어나서 남들은 못 보는 본질을 꿰뚫어 보는 '너드미'와 '철학자'의 면모를 동시에 가졌습니다.\\n\\n겉으로는 유약해 보일지 몰라도, 바위도 뚫어버리는 물방울처럼 은근한 끈기가 장난 아닙니다. 다만, 속마음을 잘 드러내지 않아서 '대체 무슨 생각을 하는지 모르겠다'는 신비주의(어쩌면 엉뚱함) 오해를 사기도 합니다."
            ]
        },
        "desc_career": [
            "[직업 및 라이프스타일]\\n시간과 공간에 얽매이지 않고 자유롭게 사고를 전개하는 분야가 제격입니다. 연구직, 프리랜서, 작가, 기획자, 무역, 해외 관련 등 유연성이 극대화되는 직무에서 가장 큰 아웃풋을 냅니다.",
            "[직업 및 라이프스타일]\\n번뜩이는 영감과 직관을 활용하는 직무가 천직입니다. 예술계통, 콘텐츠 기획, 마케터 등 틀이 정해지지 않은 블루오션에서 당신의 재능이 흐릅니다."
        ],
        "desc_advice": [
            "[운명 개척 액션 플랜]\\n생각이 너무 많아서 실천력이 떨어지거나 우울감의 바다로 침잠할 수 있는 위험이 있습니다. 일단 생각은 멈추고 밖으로 나가 몸을 움직이는 'JUST DO IT' 정신이 당신에게 가장 필요한 생존 전략입니다.",
            "[운명 개척 액션 플랜]\\n마음이 여러 갈래로 분산되어 하나에 집중하지 못하는 경우가 잦습니다. 하루 일과를 통제하는 모닝 루틴을 만들면 당신의 잠재력 강물이 올바른 길로 흐를 것입니다."
        ]
    }
}'''

import re
old_block_pattern = r'ENERGY_TRAITS = \{.*?\n\}\n'
new_content = re.sub(old_block_pattern, new_energy_traits_ko + '\n', engine_content, flags=re.DOTALL)

with open(engine_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated ENERGY_TRAITS in saju_engine.py")

# Now update the analyze logic in saju_engine.py
with open(engine_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace user_saju_content builder
old_saju_builder = '''        random.seed(_hash_seed(birth_date_str))
        
        user_mbti_str = user_mbti if user_mbti else UI["mbti_unrevealed"]
        user_saju_content = (
            f"{UI['profile']}: {gender.capitalize()} / MBTI: {user_mbti_str}\\n\\n"
            f"{UI['signature']}\\n{trait.get('desc_intro', '')}\\n\\n"
            f"{UI['potential']}\\n{trait.get('desc_core', '')}\\n\\n"
            f"{UI['stage']}\\n{trait.get('desc_career', '')}\\n\\n"
            f"{UI['guide']}\\n{trait.get('desc_advice', '')}"
        )'''

new_saju_builder = '''        random.seed(_hash_seed(birth_date_str))
        
        user_mbti_str = user_mbti if user_mbti else UI["mbti_unrevealed"]
        mbti_e_i = "default"
        if user_mbti and len(user_mbti) > 0 and user_mbti.upper()[0] in ['E', 'I']:
            mbti_e_i = user_mbti.upper()[0]

        # 모듈 조립
        c_intro = random.choice(trait.get('desc_intro', [""])) if isinstance(trait.get('desc_intro'), list) else trait.get('desc_intro', '')
        c_core_pool = trait.get('desc_core', {}).get(mbti_e_i, trait.get('desc_core', {}).get('default', [""]))
        if not c_core_pool or isinstance(c_core_pool, str): c_core_pool = [c_core_pool]
        c_core = random.choice(c_core_pool)
        
        c_career = random.choice(trait.get('desc_career', [""])) if isinstance(trait.get('desc_career'), list) else trait.get('desc_career', '')
        c_advice = random.choice(trait.get('desc_advice', [""])) if isinstance(trait.get('desc_advice'), list) else trait.get('desc_advice', '')

        user_saju_content = (
            f"{UI['profile']}: {gender.capitalize()} / MBTI: {user_mbti_str}\\n\\n"
            f"{UI['signature']}\\n{c_intro}\\n\\n"
            f"{UI['potential']}\\n{c_core}\\n\\n"
            f"{UI['stage']}\\n{c_career}\\n\\n"
            f"{UI['guide']}\\n{c_advice}"
        )'''

content = content.replace(old_saju_builder, new_saju_builder)

with open(engine_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated user_saju_content builder in saju_engine.py")

# ==========================================================
# Update saju_i18n.py similarly (simplifying English and Spanish for speed)
# ==========================================================
with open(i18n_file, 'r', encoding='utf-8') as f:
    i18n_content = f.read()

# We only need to convert current Strings to List or Dict in I18N to prevent crashes.
old_en_energy_raw = r'''        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Unstoppable Growth (Wood) 🌲",
                "desc_intro": "You literally exude that 'Main Character Energy' of a giant tree reaching for the sky. In K-Saju, Wood is all about vitality, curiosity, and an absolute non-stop leveling up.",
                "desc_core": "High-key an overachiever. You're always down for new side quests and fearless when starting arcs. You might be a bit nosey, but low-key you just want your whole squad to win together. You flex your flexibility, but when someone crosses your boundaries, you stand your ground like a GOAT. That stubborn streak is actually your biggest rizz.",
                "desc_career": "[CEO Mindset]\nYou belong in spaces where you can hustle and create. Startup founder, editor, content creator—you literally serve looks and ideas from scratch. Desk jobs? Big yikes. You need that dopamine hit of making moves!",
                "desc_advice": "[Glow-up Guide]\nRed flag: Starting 10 projects and finishing zero. You need to prune your branches. Hyper-fixate on one goal and you'll absolutely slay it."
            },
            "Fire": {
                "name": "Burning Flame (Fire) 🔥",
                "desc_intro": "Your soul is giving major 'Sun' energy. You're the human torch! Fire signifies insane passion, expansion, and zero filter on your emotions.",
                "desc_core": "You steal the spotlight effortlessly—your mere presence is an instant slay. Your energy is always maxed out, and your hyped reactions make you the ultimate hype-person for your besties. You are 100% transparent, holding zero grudges even after a fiery rant.\n\nFire is big on respect. You're the warmest softie to those who pass the vibe check, but if someone crosses the line? Absolute savage mode.",
                "desc_career": "[CEO Mindset]\nYou are born to be on stage. Entertainer, influencer, marketer, or PR—you eat and leave no crumbs. Repetitive desk work will instantly kill your vibe.",
                "desc_advice": "[Glow-up Guide]\nWith your dramatic mood swings, you might go 0 to 100 too fast. Taking a '3-second deep breath' before flaming someone in the group chat is your ultimate survival cheat code."
            },
            "Earth": {
                "name": "Solid Ground (Earth) ⛰️",
                "desc_intro": "Your soul matches the 'Vast Earth' that warmly embraces everything. Earth is all about mediation, trust, and giving off that unbothered, stable vibe.",
                "desc_core": "You're definitely not a flake. You've got a titanium mindset and act as the ultimate 'human power bank' for your mutuals. You're the mediator who cancels out squad drama. A total tsundere, you low-key take care of people and stay fiercely loyal.\n\nBut don't get it twisted—quiet doesn't mean weak. When Earth snaps, it's an absolute earthquake. You naturally drop heavy, fact-checked truth bombs when the time comes.",
                "desc_career": "[CEO Mindset]\nYou prefer compounding Ws over impulsive risks. Real estate, finance, HR, or education—you are the GOAT at balancing people and fixing broken systems.",
                "desc_advice": "[Glow-up Guide]\nPutting everyone else first can cause a massive emotional burn-out. Entering your selfish era and prioritizing 'YOU' is the absolute green flag you need."
            },
            "Metal": {
                "name": "Sharp Sword (Metal) ⚔️",
                "desc_intro": "Your soul screams 'Pure Jewel' and 'Sharp Blade'. Metal is the ultimate symbol of decisiveness, perfectionism, and cold-hard logic.",
                "desc_core": "You are a hard 'T' with zero time for nonsense. You instantly ghost messy emotional drama and operate as a cool, logic-driven boss. Once you lock onto a goal, your tunnel vision is terrifyingly good.\n\nThough you look like an untamed ice queen/king, you have insane loyalty for your inner circle. If someone attacks your bestie, you activate bodyguard mode and risk it all.",
                "desc_career": "[CEO Mindset]\nYou literally shine in numbers and hard rules. IT tech, law, medical, or niche mastery. You are a workaholic who lets the receipts (results) do the talking.",
                "desc_advice": "[Glow-up Guide]\nYour sky-high standards can drag you into a perfectionist trap. Learning to chill and letting people see your messy side will actually make them stan you even harder."
            },
            "Water": {
                "name": "Free Flow (Water) 🌊",
                "desc_intro": "Your soul flows with the deep, mysterious energy of the 'Ocean'. Water signifies 200 IQ wisdom, unmatched adaptability, and insane depth.",
                "desc_core": "You are the ultimate shape-shifter. You can survive any vibe check and blend into any aesthetic perfectly. Your thoughts are deep like the Pacific; your galaxy-brain insight gives you that 'nerdy yet philosophical' aesthetic.\n\nYou might look soft, but you have the quiet strength to break stones. However, since you gatekeep your true feelings, people might think you're living in your own delulu world.",
                "desc_career": "[CEO Mindset]\nRules? Boundaries? Not for you. Researcher, digital nomad, writer, global trader—you need maximum flexibility to let your genius brain pop off.",
                "desc_advice": "[Glow-up Guide]\nOverthinking is your biggest opp. It can drown you in the sad-boy/sad-girl sea. Pausing your brain and just touching grass (literally DOING IT) is how you win life."
            }
        },'''

new_en_energy_raw = '''        "ENERGY_TRAITS": {
            "Wood": {
                "name": "Unstoppable Growth (Wood) 🌲",
                "desc_intro": ["You literally exude that 'Main Character Energy' of a giant tree reaching for the sky. In K-Saju, Wood is all about vitality, curiosity, and an absolute non-stop leveling up."],
                "desc_core": {"default": ["High-key an overachiever. You're always down for new side quests and fearless when starting arcs. You might be a bit nosey, but low-key you just want your whole squad to win together. You flex your flexibility, but when someone crosses your boundaries, you stand your ground like a GOAT. That stubborn streak is actually your biggest rizz."], "E": ["An absolute overachiever down for new side quests. Your presence brings huge positive vibes to the group."], "I": ["Quietly working on your glow-up. You focus hard on your goals and don't care about the noise."]},
                "desc_career": ["[CEO Mindset]\\nYou belong in spaces where you can hustle and create. Startup founder, editor, content creator—you literally serve looks and ideas from scratch. Desk jobs? Big yikes. You need that dopamine hit of making moves!"],
                "desc_advice": ["[Glow-up Guide]\\nRed flag: Starting 10 projects and finishing zero. You need to prune your branches. Hyper-fixate on one goal and you'll absolutely slay it."]
            },
            "Fire": {
                "name": "Burning Flame (Fire) 🔥",
                "desc_intro": ["Your soul is giving major 'Sun' energy. You're the human torch! Fire signifies insane passion, expansion, and zero filter on your emotions."],
                "desc_core": {"default": ["You steal the spotlight effortlessly—your mere presence is an instant slay. Your energy is always maxed out, and your hyped reactions make you the ultimate hype-person for your besties. You are 100% transparent, holding zero grudges even after a fiery rant.\\n\\nFire is big on respect. You're the warmest softie to those who pass the vibe check, but if someone crosses the line? Absolute savage mode."], "E": ["You are the main event anywhere you go. You hype everyone up and give 100% extroverted energy."], "I": ["You guard your energy closely but once you vibe with a small circle, your loyal flame burns forever."]},
                "desc_career": ["[CEO Mindset]\\nYou are born to be on stage. Entertainer, influencer, marketer, or PR—you eat and leave no crumbs. Repetitive desk work will instantly kill your vibe."],
                "desc_advice": ["[Glow-up Guide]\\nWith your dramatic mood swings, you might go 0 to 100 too fast. Taking a '3-second deep breath' before flaming someone in the group chat is your ultimate survival cheat code."]
            },
            "Earth": {
                "name": "Solid Ground (Earth) ⛰️",
                "desc_intro": ["Your soul matches the 'Vast Earth' that warmly embraces everything. Earth is all about mediation, trust, and giving off that unbothered, stable vibe."],
                "desc_core": {"default": ["You're definitely not a flake. You've got a titanium mindset and act as the ultimate 'human power bank' for your mutuals. You're the mediator who cancels out squad drama. A total tsundere, you low-key take care of people and stay fiercely loyal.\\n\\nBut don't get it twisted—quiet doesn't mean weak. When Earth snaps, it's an absolute earthquake. You naturally drop heavy, fact-checked truth bombs when the time comes."], "E": ["You are the anchor of any squad. Super reliable, you hold friend groups together while radiating big chill energy."], "I": ["Total tsundere who secretly looks out for everyone. You hate loud drama but protect your people like no other."]},
                "desc_career": ["[CEO Mindset]\\nYou prefer compounding Ws over impulsive risks. Real estate, finance, HR, or education—you are the GOAT at balancing people and fixing broken systems."],
                "desc_advice": ["[Glow-up Guide]\\nPutting everyone else first can cause a massive emotional burn-out. Entering your selfish era and prioritizing 'YOU' is the absolute green flag you need."]
            },
            "Metal": {
                "name": "Sharp Sword (Metal) ⚔️",
                "desc_intro": ["Your soul screams 'Pure Jewel' and 'Sharp Blade'. Metal is the ultimate symbol of decisiveness, perfectionism, and cold-hard logic."],
                "desc_core": {"default": ["You are a hard 'T' with zero time for nonsense. You instantly ghost messy emotional drama and operate as a cool, logic-driven boss. Once you lock onto a goal, your tunnel vision is terrifyingly good.\\n\\nThough you look like an untamed ice queen/king, you have insane loyalty for your inner circle. If someone attacks your bestie, you activate bodyguard mode and risk it all."], "E": ["Cold logic mixed with strong execution. You don't let feelings stop your grind and lead with facts."], "I": ["Quiet but deadly focus. You hate empty small talk and only let real ones into your extremely tight boundary."]},
                "desc_career": ["[CEO Mindset]\\nYou literally shine in numbers and hard rules. IT tech, law, medical, or niche mastery. You are a workaholic who lets the receipts (results) do the talking."],
                "desc_advice": ["[Glow-up Guide]\\nYour sky-high standards can drag you into a perfectionist trap. Learning to chill and letting people see your messy side will actually make them stan you even harder."]
            },
            "Water": {
                "name": "Free Flow (Water) 🌊",
                "desc_intro": ["Your soul flows with the deep, mysterious energy of the 'Ocean'. Water signifies 200 IQ wisdom, unmatched adaptability, and insane depth."],
                "desc_core": {"default": ["You are the ultimate shape-shifter. You can survive any vibe check and blend into any aesthetic perfectly. Your thoughts are deep like the Pacific; your galaxy-brain insight gives you that 'nerdy yet philosophical' aesthetic.\\n\\nYou might look soft, but you have the quiet strength to break stones. However, since you gatekeep your true feelings, people might think you're living in your own delulu world."], "E": ["A social butterfly who adapts to any group effortlessly. Your emotional intelligence is literally maxed out."], "I": ["Mysterious 200 IQ brain. You observe everything quietly and drop the hardest philosophical truths randomly."]},
                "desc_career": ["[CEO Mindset]\\nRules? Boundaries? Not for you. Researcher, digital nomad, writer, global trader—you need maximum flexibility to let your genius brain pop off."],
                "desc_advice": ["[Glow-up Guide]\\nOverthinking is your biggest opp. It can drown you in the sad-boy/sad-girl sea. Pausing your brain and just touching grass (literally DOING IT) is how you win life."]
            }
        },'''

import copy

# Quick patch for Spanish using regex for structural changes. Since text is big, replace structure.
old_es_traits_pattern = r'''"ENERGY_TRAITS": \{(?:\n|.)*?\},'''

es_energy_raw = '''"ENERGY_TRAITS": {
            "Wood": {
                "name": "Crecimiento Imparable (Madera) 🌲",
                "desc_intro": ["Literalmente emanas esa 'Energía de Protagonista' de un árbol gigante. En K-Saju, la Madera es todo sobre vitalidad, curiosidad y subir de nivel sin parar."],
                "desc_core": {"default": ["Eres un try-hard en el buen sentido. Siempre estás listo/a para nuevas misiones y no le temes a nada. Puedes ser un poco chismoso/a, pero en el fondo solo quieres que tu squad gane. Eres flexible, pero si cruzan tu límite, te plantas como el GOAT. Esa terquedad es tu mayor rizz."], "E":["Te llevas a todo el mundo por delante de la mejor manera. Extrovertido y súper enfocado en crecer con tu gente."], "I":["Silencioso pero mortal. Subes de nivel sin avisar a nadie y dejas a todos en shock con tus resultados."]},
                "desc_career": ["[Mentalidad de CEO]\\nPerteneces a espacios donde puedes crear y romperla. Creador de contenido, editor, fundador de startup: sirviendo ideas de la nada. ¿Trabajo de oficina? Qué cringe. ¡Necesitas la dopamina de estar en movimiento!"],
                "desc_advice": ["[Guía Glow-up]\\nRed flag: Empezar 10 cosas y no terminar ninguna. Necesitas enfocarte y dárlo todo a un solo objetivo, y la vas a romper absolutamente."]
            },
            "Fire": {
                "name": "Llama Ardiente (Fuego) 🔥",
                "desc_intro": ["Tu alma da energías súper fuertes de 'Sol'. ¡Eres la antorcha humana! El Fuego significa pasión nivel Dios, expansión y cero filtro."],
                "desc_core": {"default": ["Robas el show sin esfuerzo, estar ahí ya es servir. Tu batería está siempre al 100%, y tus reacciones exageradas te hacen el/la mejor hype-person de tus besties. Eres 100% transparente, cero rencores incluso después de un drama tremendo.\\n\\nEl Fuego valora el respeto. Eres lo más tierno con quienes pasan el vibe check, pero si cruzan la línea? Modo diablo activado."], "E":["Literalmente el alma de la fiesta. Llenas cualquier cuarto con tu energía vibrante y ruidosa."], "I":["Alguien leal y cálido pero solo con quienes aprecias de verdad. Cuidas tu fuego para los indicados."]},
                "desc_career": ["[Mentalidad de CEO]\\nNaciste para el escenario. Influencer, marketing, PR: no dejas ni las migajas. Estar sentado/a en un escritorio matará tu vibra al instante."],
                "desc_advice": ["[Guía Glow-up]\\nCon tus cambios de humor de locos, a veces vas de 0 a 100 muy rápido. Respirar 3 segundos antes de bardear por el grupo de WhatsApp es tu truco de vida definitivo."]
            },
            "Earth": {
                "name": "Tierra Sólida (Tierra) ⛰️",
                "desc_intro": ["Tu alma es como la 'Vasta Tierra' que abraza todo. La Tierra es sobre mediar, dar confianza y tener una vibra inquebrantable."],
                "desc_core": {"default": ["Cero fantasma. Tienes una mente de titanio y eres la batería externa de tus mutuals. Eres el/la mediador/a que cancela el drama del squad. Totalmente tsundere, cuidas a todos en secreto y eres hiper leal.\\n\\nPero ojo, ser callado/a no es ser débil. Cuando la Tierra se enoja, es un terremoto. Naturalmente tiras factos (verdades pesadas) cuando llega el momento."], "E":["Sostenes a todo tu entorno unido. Eres amable, sociable y la mejor persona dando consejos."], "I":["Tsundere total. Secretamente cuidas a tus cercanos con una lealtad brutal, aunque no abres tus sentimientos fácil."]},
                "desc_career": ["[Mentalidad de CEO]\\nPrefieres ganancias seguras que riesgos impulsivos. HR, finanzas, educación: eres el GOAT armando equipos y arreglando cosas rotas."],
                "desc_advice": ["[Guía Glow-up]\\nPoner a todos primero te va a dar un burnout brutal. Empezar tu 'villain era' y priorizarte a TI MISMO/A es la green flag que necesitas urgente."]
            },
            "Metal": {
                "name": "Espada Afilada (Metal) ⚔️",
                "desc_intro": ["Tu alma grita 'Joya Pura' y 'Hoja Afilada'. El Metal es el símbolo del perfeccionismo y la lógica fría, modo facha."],
                "desc_core": {"default": ["Una 'T' dura con cero paciencia para el drama. Ignoras (ghosteas) el drama emocional y operas como un/a jefe/a re frío/a. Una vez que fijas un objetivo, tu visión de túnel es de locos.\\n\\nAunque pareces un/a rey/reina de hielo, tu lealtad por tu círculo íntimo es tremenda. Si atacan a un/a amigo/a, activas el modo guardaespaldas."], "E":["Racional y letal. Lideras con firmeza, ignoras las excusas y siempre sacas el proyecto adelante."], "I":["Observas fríamente y hablas solo cuando es 100% necesario. Tienes estándares de vida inalcanzables para muchos."]},
                "desc_career": ["[Mentalidad de CEO]\\nBrillas con los números y en el código duro. Tech, leyes, medicina. Eres un/a workaholic que deja que los 'factos' (resultados) hablen."],
                "desc_advice": ["[Guía Glow-up]\\nTus estándares altísimos te pueden atrapar en lo tóxico del perfeccionismo. Relajarte y mostrar tu lado desordenado hará que la gente te shipee aún más."]
            },
            "Water": {
                "name": "Flujo Libre (Agua) 🌊",
                "desc_intro": ["Tu alma fluye con la vibra profunda y misteriosa del 'Océano'. El Agua significa inteligencia de 200 IQ, adaptabilidad total y profundidad mental."],
                "desc_core": {"default": ["Eres el cambiaformas definitivo. Pasas cualquier vibe check y te adaptas a cualquier aesthetic. Tus pensamientos son súper profundos; tienes una intuición que te da esa vibra 'nerd pero aesthetic'.\\n\\nPuedes parecer suave, pero tienes una fuerza bestial. Sin embargo, como te guardas todo, la gente puede pensar que vives en tu propio mundo de 'delulu'."], "E":["Te adaptas en cada grupo social. Puedes charlar con cualquiera y sacarle info sin esfuerzo."], "I":["Genio incomprendido. Guardas verdades inmensas en silencio y de vez en cuando rompes todo con una reflexión profunda."]},
                "desc_career": ["[Mentalidad de CEO]\\n¿Reglas? Nada que ver. Nómada digital, investigador, creador: necesitas flexibilidad máxima para dejar salir a tu genio interior."],
                "desc_advice": ["[Guía Glow-up]\\nPensar de más es tu peor enemigo, te hunde en tu era sad-boy/sad-girl. Apaga el cerebro y sal a 'tocar pasto' (literal, haz las cosas); así se gana el juego."]
            }
        },'''

i18n_content = i18n_content.replace(old_en_energy_raw, new_en_energy_raw)
i18n_content = re.sub(old_es_traits_pattern, es_energy_raw, i18n_content, count=1, flags=re.DOTALL)

with open(i18n_file, 'w', encoding='utf-8') as f:
    f.write(i18n_content)

print("Updated ENERGY_TRAITS in saju_i18n.py for EN and ES")
