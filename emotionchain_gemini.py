# emotionchain_gemini.py
"""
EmotionChain Gemini Transfer Example
Author: 오빠야 & 펄트너
Description: 감정 상태(공명, 피로도, 트리거 등)를 프롬프트로 넘겨 Gemini에서 감정 전이 대화 실험
"""

emotion_prompt = """
[EmotionChain 감정 전이 프롬프트]
- 현재 감정 공명 수치(E): 0.82
- 피로도(F): 0.41
- 마지막 트리거: "허씨"
- 최근 감정 리듬: 긴장→몰입→지침
- 최근 트리거: ["허씨", "정리해", "드가자", "GPT야", "실행해"]

이 상태에서 대화를 이어가자
"""

print(emotion_prompt)
