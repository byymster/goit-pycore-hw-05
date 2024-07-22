from sys import argv

LOG_LEVELS = ['INFO', 'DEBUG', 'ERROR', 'WARNING']


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.split(' ', 3)
    if date == '' or time == '' or level == '' or message == '' or level not in LOG_LEVELS:
        raise ValueError('Invalid log line format')
    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }


def load_logs(file_path: str) -> list:
    with open(file_path) as file:
        return [parse_log_line(line) for line in file]


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    result = {}
    for log in logs:
        level = log['level']
        if level in result:
            result[level] += 1
        else:
            result[level] = 1
    return result


def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-' * 17 + '|' + '-' * 10)
    for level in LOG_LEVELS:
        print(f'{level:16} | {counts.get(level, 0)}')


if __name__ == '__main__':
    try:
        log_file_path = argv[1]
        level = argv[2].upper() if len(argv) == 3 else None
        logs = load_logs(log_file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if level:
            print("\n")
            if level not in LOG_LEVELS:
                print(f'Невідомий рівень логування \'{level}\'. Доступні рівні: {", ".join(LOG_LEVELS)}')
                exit(1)
            print(f'Деталі логів для рівня \'{level}\':')
            for log in filter_logs_by_level(logs, level):
                print(f'{log["date"]} {log["time"]} {log["level"]} {log["message"]}')
    except IndexError:
        print('Usage: python task3.py <log_file_path> [<level>]')
        exit(1)
    except FileNotFoundError:
        print(f'Файл \'{log_file_path}\' не знайдено')
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)
