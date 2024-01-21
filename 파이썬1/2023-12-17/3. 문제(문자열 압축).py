# 문자열 압축 : 주어진 문자열을 압축하는 함수를 작성하시오

# 압축 규칙은 다음과 같습니다.

# aaabbbb는 a3b4로 압축됩니다.

# abcde는 abcde(압축되지 않음)

def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    # 문자열을 순회하면서 각 문자에 대해 처리
    for i in range(1, len(s)):
        if s[i] == s[i - 1]: # 현재 문자가 이전 문자와 같은 경우
            count += 1 # 카운트 증가
        else:
            # 현재 문자가 이전 문자와 다른 경우
            # 연속된 개수가 1보다 큰 경우만 숫자를 추가하여 압축 문자열에 추가
            compressed.append(s[i - 1] + (str(count) if count > 1 else ""))
            # 카운트 초기화
            count = 1

    # 마지막 문자 처리
    compressed.append(s[-1] + (str(count) if count > 1 else ""))
    # 압축된 문자열을 결합하여 반환
    compressed_str = ''.join(compressed)
    return compressed_str


print(compress_string("aabb"))
print(compress_string("abcde"))
print(compress_string("aaabbbb"))








