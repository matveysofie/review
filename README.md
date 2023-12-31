<h4 align="center"> 
    <samp>💡 REVIEW: Test task for mentor and code reviewer (async)
</samp>
</h4>

<hr>

#### *Решение студента соответствует основным пунктам задания. В коде представлены классы Scheduler и Job, которые описывают планировщик задач и задачи соответственно. Реализация использует корутины и генераторы, что соответствует требованиям задания.*

<hr>
<h3 align="center">✖ Недочеты</h3>
<hr>

#### *1) Следует проверить использование аннотаций типов для аргументов функций и возвращаемых значений. В описании задания требуется использование аннотаций типов*<br>
#### *2) Также следует убедиться, что вся работа с файловой системой и сетью выполняется внутри класса Job, так как это требование задания. В текущей реализации есть вызовы функций get_and_write_data, copy_file и delete_file извне класса Job. Попробуй переместить их внутрь класса Job и вызывай их из метода run внутри соответствующих задач* <br>
#### *3) Вместо использования multiprocessing можно попробовать использовать asyncio для создания асинхронных задач и планировщика (это позволит более эффективно управлять выполнением задач и сделать код более компактным)* <br>
#### *4) Рекомендуется добавить обработку исключений в коде* <br>
#### *5) Для проверки работоспособности кода не забудь написать тесты (они помогут убедиться, что планировщик и задачи выполняются корректно и соответствуют требованиям задания)* <br><hr>

<h3 align="center">❕Общие рекомендации</h3>
<hr>

#### *Добавь аннотации типов в соответствующие места кода, чтобы улучшить понимание типов данных и сделать код более читаемым.*
#### *Удали неиспользуемые переменные, такие как task_list в методе schedule класса Scheduler.*
#### *Убедись, что переменные, такие как condition, определены и инициализированы соответствующим образом.*
#### *Проверь, что все импорты соответствуют ожидаемым модулям и классам.*
<hr>

### А также рекомендации для дополнительного чтения:
<hr>

#### Документация по asyncio в Python (https://docs.python.org/3/library/asyncio.html)
#### Документация по модулю multiprocessing в Python (https://docs.python.org/3/library/multiprocessing.html)
#### PEP 484: Type Hints (https://peps.python.org/pep-0484/)
#### PEP 8: Style Guide for Python Code (https://peps.python.org/pep-0008/)