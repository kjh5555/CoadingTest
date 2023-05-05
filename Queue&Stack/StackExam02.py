'''temperatures일일 온도를 나타내는 정수 배열이 주어 지면 더 따뜻한 온도를 얻기 위해 하루 이후에 기다려야 하는 일 수와 같은 배열을 반환합니다 . 
    이것이 가능한 미래의 날이 없다면 대신 유지하십시오.answer answer[i] ith answer[i] == 0

 
예 1:

입력: 온도 = [73,74,75,71,69,72,76,73]
 출력: [1,1,4,2,1,1,0,0]
예 2:

입력: 온도 = [30,40,50,60]
 출력: [1,1,1,0]
예 3:

입력: 온도 = [30,60,90]
 출력: [1,1,0]
 

제약:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100'''
def checkTempt(tempt):
    ans = [0] * len(tempt)
    stack = []
    for cur_day, cur_temp in enumerate(tempt):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return print(ans)    
       
checkTempt([73,74,75,71,69,72,76,73])         



