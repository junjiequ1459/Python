def groups_per_user(group_dictionary):
	user_groups = {}
	for group,users in group_dictionary.items():
		for user in users:
			list = []
			if user not in user_groups:
				list.append(group)
				user_groups[user] = list
			else:
				for x in user_groups[user]:
					list.append(x)
				list.append(group)
				user_groups[user] = list

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"]}))

def main():
    pass
if __name__ == '__main__':
    main()


