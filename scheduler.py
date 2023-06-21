# Привет! В общем что смог, то сделал. Остальное даже загуглить не могу.
# По факту просто трачу время, сидя и пялясь в экран. На эту реализацию неделя потрачена))
# Я просто не понимаю даже что гуглить, что бы сделать всё задание.
# Не знаю, может после ревью я с мёртвой точки сдвинусь, поэтому отправляю пока так...

# REVIEW: Решение студента соответствует основным пунктам задания. В коде представлены классы Scheduler и Job, которые описывают планировщик задач и задачи соответственно. Реализация использует корутины и генераторы, что соответствует требованиям задания.
# Но присутствуют некоторые недочеты:
# 1) Следует проверить использование аннотаций типов для аргументов функций и возвращаемых значений. В описании задания требуется использование аннотаций типов
# 2) Также следует убедиться, что вся работа с файловой системой и сетью выполняется внутри класса Job, так как это требование задания. В текущей реализации есть вызовы функций get_and_write_data, copy_file и delete_file извне класса Job. Попробуй переместить их внутрь класса Job и вызывай их из метода run внутри соответствующих задач
# 3) Вместо использования multiprocessing можно попробовать использовать asyncio для создания асинхронных задач и планировщика (это позволит более эффективно управлять выполнением задач и сделать код более компактным)
# 4) Рекомендуется добавить обработку исключений в коде
# 5) Для проверки работоспособности кода не забудь написать тесты (они помогут убедиться, что планировщик и задачи выполняются корректно и соответствуют требованиям задания)
from job import Job, get_and_write_data, delete_file, copy_file
from logger import logger
import multiprocessing


def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


class Scheduler(object):
    def __init__(
            self,
            max_working_time=1,
            tries=0,
            dependencies=(),
            start_at=None,
    ):
        super().__init__()
        self.task_list: list[Job] = []
        self.start_at = start_at
        self.max_working_time = max_working_time
        self.tries = tries
        self.dependencies = dependencies if dependencies is not None else None

    @coroutine
    def schedule(self):
        processes = []
        while True:
            task_list = (yield)
            print(task_list)
            for task in task_list:
                logger.info(f'Планировщик: запускаю задачу - {task.name}')
                p = multiprocessing.Process(target=task.run, args=(condition, url),)
                p.start()
                processes.append(p)
            for process in processes:
                logger.info(process)
                process.join()
                logger.info(f' process {process} stopped!')

    def run(self, jobs: tuple):
        gen = self.schedule()
        gen.send(jobs)


if __name__ == '__main__':
    condition = multiprocessing.Condition()
    url = 'https://official-joke-api.appspot.com/random_joke'
    job1 = Job(
        func=get_and_write_data,
        name='Запрос в сеть',
        args=(condition, url),
    )
    job2 = Job(
        func=copy_file,
        name='Удалить файл',
        args=(condition, ),
    )
    job3 = Job(
        func=delete_file,
        name='Скопировать файл',
        args=(condition,),
    )
    g = Scheduler()

# Общие рекомендации:
# Добавь аннотации типов в соответствующие места кода, чтобы улучшить понимание типов данных и сделать код более читаемым.
# Удали неиспользуемые переменные, такие как task_list в методе schedule класса Scheduler.
# Убедись, что переменные, такие как condition, определены и инициализированы соответствующим образом.
# Проверь, что все импорты соответствуют ожидаемым модулям и классам.

# А также рекомендации для дополнительного чтения:
# Документация по asyncio в Python (https://docs.python.org/3/library/asyncio.html)
# Документация по модулю multiprocessing в Python (https://docs.python.org/3/library/multiprocessing.html)
# PEP 484: Type Hints (https://peps.python.org/pep-0484/)
# PEP 8: Style Guide for Python Code (https://peps.python.org/pep-0008/)
