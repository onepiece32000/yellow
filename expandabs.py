#!/usr/bin/python3

str_example = "runoob\t12345\tabc"
print('原始字符串:', str_example)

# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号:', str_example.expandtabs())

# 2 个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号:', str_example.expandtabs(2))

# 3 个空格
print('使用 3 个空格:', str_example.expandtabs(3))

# 4 个空格
print('使用 4 个空格:', str_example.expandtabs(4))

# 5 个空格
print('使用 5 个空格:', str_example.expandtabs(5))

# 6 个空格
print('使用 6 个空格:', str_example.expandtabs(6))

