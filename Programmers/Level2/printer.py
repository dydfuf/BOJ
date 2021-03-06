def solution(priorities, location):
    answer = 0
    location_priorities = []
    idx = 0
    for aPriorities in priorities:
        location_priorities.append([aPriorities, idx])
        idx += 1

    printed = []

    while len(printed) != len(priorities):
        if location_priorities[0][0] < max(location_priorities)[0]:
            location_priorities.append(location_priorities.pop(0))
        else:
            printed.append(location_priorities.pop(0))

    for i in range(0, len(printed)):
        if printed[i][1] == location:
            answer += i+1
            break

    return answer


def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


if __name__ == "__main__":
    arr_priorities = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
    arr_location = [2, 0]
    for priorities, location in zip(arr_priorities, arr_location):
        print(solution(priorities, location))
