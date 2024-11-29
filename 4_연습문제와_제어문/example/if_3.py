score = int(input("enter code : "))

if score >= 60:
    message = "success"
else: 
    message = "failure"

print(message)

# 조건부 표현식 -> 가독성에 유리한 한 줄 짜리 코드  
"""
message = "success" if score >= 60 else "failure"
print(message)
"""
