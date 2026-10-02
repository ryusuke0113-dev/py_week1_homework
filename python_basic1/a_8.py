# A-8: リストを要素に持つリスト
# users_info を使って次のような出力をしてください
users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

# users_info_b = f"Name: {users_info[0][0]}, Age: {users_info[0][1]}"
# users_info_t = f"Name: {users_info[1][0]}, Age: {users_info[1][1]}"
# users_info_k = f"Name: {users_info[2][0]}, Age: {users_info[2][1]}"

# print(users_info_b)
# print(users_info_t)
# print(users_info_k)

for name, age in users_info:
    print(f"Name: {name}, Age: {age}")
