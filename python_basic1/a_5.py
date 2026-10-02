# A-5: 要素へのアクセスとフォーマット
# 次のリストを利用して、"Name: Bob Dylan, Age: 79"と出力してください
bob_info = ["Bob", "Dylan", 79]

bob_fast = bob_info[0]
bob_family = bob_info[1]
bob_age = bob_info[2]

message = f"Name: {bob_fast} {bob_family}, Age: {bob_age}"
print(message)
