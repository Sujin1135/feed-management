# 피드 or 댓글 본문을 입력받아 키워드 알람 발송
from app.enums.keyword_type import KeywordType


def alert_keyword(keyword_type: KeywordType, text: str):
    print(f"type is {keyword_type} and text as below")
    print(f"{text}")
