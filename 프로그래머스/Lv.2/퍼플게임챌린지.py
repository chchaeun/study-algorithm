def solution(diffs, times, limit):
    def calculate_solving_time(time_cur, time_prev, diff, level):
        if diff <= level:
            return time_cur

        if diff > level:
            return (diff - level) * (time_cur + time_prev) + time_cur

    def is_solving_in_limit(level):
        time_prev = 0
        total_solving_time = 0

        for i in range(len(diffs)):
            time_cur = calculate_solving_time(times[i], time_prev, diffs[i], level)

            total_solving_time += time_cur

            if total_solving_time > limit:
                return False

            time_prev = times[i]

        return True

    def binary_search():
        left, right = 1, 100000
        result = 100000

        while left <= right:
            mid = (left + right) // 2

            if result < mid:
                break

            if is_solving_in_limit(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    return binary_search()
