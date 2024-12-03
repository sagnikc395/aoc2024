def is_valid_sequence(arr):
    if len(arr) < 2:
        return True

    is_increasing = arr[1] > arr[0]

    for i in range(1,len(arr)):
        diff = arr[i] - arr[i-1]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if is_increasing and diff < 0:
            return False
        if not is_increasing and diff > 0:
            return False

    return True


def part1():
    with open('input.txt') as f:
        reports = f.read().strip().split('\n')

    safe_report_count = 0 
    for report in reports:
        items = [int(i) for i in report.split(' ')]
        if is_valid_sequence(items):
            safe_report_count += 1

    print(safe_report_count)
        
    




def main():
    part1()


if __name__ == '__main__':
    main()
