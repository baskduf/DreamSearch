import json

from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as genai
import os

# Create your views here.
def process(request):
    try:
        if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            data = json.loads(request.body.decode('utf-8'))  # Decode bytes to string
            content = data.get('input_text')
            # 받아온 데이터 처리 로직
            print(content)  # 콘솔에 출력해보기

            # AI 로직
            genai.configure(api_key=os.environ['API_KEY'])

            model = genai.GenerativeModel('gemini-1.0-pro-latest')
            dream = f"""
            #입력문
너는 꿈을 해몽해주는 로봇이다. 꿈의 내용은 [#꿈]에 있다. 어떻게 대답해야 하는지는 [#출력형식]과 [#예시]를 참고한다. 
#꿈
{content}
#출력형식
-현재 꿈이 어떤지 검색 데이터를 기반으로 해몽해줘
-결과 해석 이외의 다른 말은 하지 않는다. 
#예시
피자를 먹는 꿈은 다음과 같은 의미를 가질 수 있습니다.

* **만족과 즐거움:** 피자는 흔히 즐거움과 편안함을 상징합니다. 꿈에서 피자를 먹는 것은 인생의 좋은 것들을 즐기고 있으며 행복하고 콘텐츠임을 나타낼 수 있습니다.

* **사회적 상호 작용:** 피자는 종종 파티나 모임과 관련이 있습니다. 꿈에서 피자를 먹는 것은 친구와 가족과의 사회적 상호 작용을 원하거나 그것을 즐기고 있음을 나타낼 수 있습니다.

* **영양 요구:** 피자는 단백질, 탄수화물, 치즈와 같은 다양한 영양소를 제공합니다. 꿈에서 피자를 먹는 것은 신체적, 정서적 영양을 찾고 있음을 나타낼 수 있습니다.

* **편안함과 안락함:** 피자는 종종 따뜻하고 포만감을 주는 음식으로 간주됩니다. 꿈에서 피자를 먹는 것은 집이나 친숙한 환경에서 안락함과 편안함을 찾고 있음을 나타낼 수 있습니다.

* **충동적인 결정:** 피자는 종종 빠르게 준비되고 편리한 음식입니다. 꿈에서 피자를 먹는 것은 충동적으로 또는 생각하지 않고 결정을 내리고 있음을 나타낼 수 있습니다.
            """

            response = model.generate_content(dream)
            # 데이터 처리 로직
            return JsonResponse({'message': '데이터 처리 성공', 'response_text': response.text})
        else:
            return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def index(request):
    return render(request, 'index.html')