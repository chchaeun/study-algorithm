def solution(pb):
    # 사전 순 정렬 -> 길이 정렬
    pb.sort(key=lambda x: (x, len(x)))
    for i in range(len(pb)-1):
        if pb[i]==pb[i+1][:len(pb[i])]:
            return False
    return True

test_pb = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"],
]

print(solution(["119", "97674223", "1195524421"]))