import re

# stations = "@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|"
# results = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', stations)
# print(results)


# abc=[('北京北', 'VAP'), ('北京东', 'BOP'), ('北京', 'BJP')]
# d=dict(abc)
# print(d)

id = [1, 2, 3, 4]
username = ['xiaoming', 'xh', 'xq', 'xx']

users = []
for i in range(len(id)):
    user = {}
    user['id'] = id[i]
    user['username'] = username[i]
    users.append(user)
print(users)