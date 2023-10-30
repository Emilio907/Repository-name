users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
sum_of_numbers= len(users)
count_of_numbers= len(set(users))
describe = {
"Общее количество" : sum_of_numbers,
"Уникальные посещения" : count_of_numbers,
}
print(describe)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
