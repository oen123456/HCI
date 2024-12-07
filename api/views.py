from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
import openai
import json
import logging

logging.basicConfig(level=logging.DEBUG)

openai.api_key = "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"  # 여기에 자신의 OpenAI API 키를 입력하세요

@csrf_exempt
def check_credibility(request):
    print("1")
    if request.method == 'POST':
        # JSON 데이터 파싱
        try:
            data = json.loads(request.body)
            print("2")
            url = data.get('url', None)
            print("3")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        if not url:
            return JsonResponse({"error": "URL is required"}, status=400)

        # 기사 내용 크롤링
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            content = ' '.join([p.text for p in soup.find_all("p")])
            print("4")
            if not content:
                print("Error: No content extracted")
                return JsonResponse({"error": "Failed to extract content from URL."}, status=400)
        except Exception as e:
            print(f"Error: Failed to fetch URL - {e}")
            return JsonResponse({"error": f"Failed to fetch URL: {str(e)}"}, status=500)

        # GPT-4o-mini 모델 호출: 신뢰도와 요약 생성
        try:
            prompt = (
                "너는 내가 주는 url이 진짜 기사일 확률을 판별하고 나에게 요약본을 제공하는 비서야.\n"
                "###instruction1.### The probability (70-100%) that the article is real news.\n"
                "###instruction2.### A concise summary of the article (within 100 words).\n\n"
                "너의 답변은 첫쨋줄에는 instruction1,즉 숫자만 그리고 줄바꿔서 둘째줄부터는 instrucion2.즉 요약을 나한테 반환해.\n"
                "만약 한번에 내 요구사항 대로 답변이 오지않은 경우 다시 내가 보낸형식대로 답변하기를 시도해"
                
                f"{content}"
            )
            print("Step 4: Prompt created")
            print(f"Prompt: {prompt}")
            gpt_response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=300,
                temperature=0  # 안정적이고 반복 가능한 결과를 위해
            )

            if 'choices' not in gpt_response or not gpt_response['choices']:
                raise ValueError("No choices returned in GPT response.")

            logging.debug(f"GPT Response: {gpt_response}")

            # GPT 응답에서 신뢰 점수와 요약 추출
            response_content = gpt_response['choices'][0]['message']['content']
            lines = response_content.strip().split("\n")
            credibility_score = float(lines[0].strip())  # 첫 번째 줄은 신뢰 점수
            summary = "\n".join(lines[1:]).strip()  # 나머지 줄은 요약
        except ValueError:
            return JsonResponse({"error": "Invalid response from GPT."}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Failed to analyze article: {str(e)}"}, status=500)

        # 결과 반환
        return JsonResponse({
            "url": url,
            "credibility_score": credibility_score,
            "summary": summary if summary else "No summary available."
        })

    return JsonResponse({"error": "Invalid request method"}, status=405)
