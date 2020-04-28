# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2


def room_people_name(room_name):
    result = ""
    for number in range(len(room_name)-1):
        result += room_name[number] + ', '
        number += 1
    result += room_name[-1]
    return result


print('В комнате room_1 живут: ' + room_people_name(room_1.folks))
print('В комнате room_2 живут: ' + room_people_name(room_2.folks))
