# 워드 임베딩 -> RNN 함수 -> 고차원의 벡터 값 -> 3D 좌표로 띄움 -> 거리게산(cos유사도) -> 유사도
import math
h_t = [0.0]
def RNN(n,data):
    result = math.tanh(0.88 * n + 1*data + 0.5)
    return result

# 3x3 벡터형태의 글자 자료
input_data = [0.97, 0.45, 0.12]


for i,data in enumerate(input_data):
    h_prev = h_t[-1]
    result = RNN(h_prev,data)
    h_t.append(result)


    print(f"Step {i+1} | 입력: {data:.2f} | 업데이트된 State: {result:.4f}")
print("\n전체 State 누적 기록:", h_t)
