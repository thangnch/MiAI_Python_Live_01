#
# Có thể xóa hết các cặp ngoặc đơn "()" để thu được một chuỗi rỗng.
# Số các cặp "()" là số nguyên dương chẵn.
# Cho một chuỗi str chứa chỉ các dấu '(' và ')'. Trả về true nếu đó là một biểu thức ngoặc đơn đúng, false nếu không.
# Ví dụ:

def check(s): # Tra ra True/False
    so_dem = 0
    so_cap = 0

    for i in range(len(s)):
        if s[i] == "(":
            so_dem = so_dem + 1
        else:
            so_dem = so_dem - 1
            if so_dem >= 0 :
                so_cap = so_cap + 1

    if so_dem ==0 and so_cap%2 ==0:
        return True
    else:
        return False

s = "()()()()("
print("Gia tri check = ", check(s))