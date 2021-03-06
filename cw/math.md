# Математическая модель децентрализованной системы

В предыдущем разделе был рассмотрен набор технологий, используемых при создании децентрализованных систем. Для дальнейших построений и исследований нужно создать абстрактную модель, описывающую поведение новой системы в различных ситуациях. В данной работе эта модель будет упрощенной. В последующих работах предполагается развитие модели, предусматривающее введение новых объектов и ограничений. Для описания основных объектов и взаимодействий используется язык теории графов. Строгое определение новых понятий необходимо для более четкого представления модели.

## Определения

1. Пучок $-$ связный неориентированный граф со структурой, зависящей от времени.

1. Источник (сообщения) $-$ одна из вершин отправляющего сообщение пучка.

1. Приемник (сообщения) $-$ одна из вершин получающего сообщение пучка.

1. Сообщение $-$ функция от времени, источника и приемника.

1. Поток (сообщений) $-$ последовательный набор сообщений.

1. Путь $-$ последовательность ребер и вершин, где 2 соседних ребра объединены общей вершиной.

1. Лист (пучка) $-$ вершина пучка. Может служить только приемником или источником сообщений. Идентифицируется путем от корня владеющего им пучка.

1. Функция идентификации $-$ функция от времени и количества уже появлявшихся в системе пучков с областью значений в не более чем счетном множестве имен (множестве идентификаторов).

1. Корень (пучка) $-$ вершина пучка, не являющаяся листом, через которую проходят все потоки сообщений от других пучков к листьям этого пучка и от его листьев к другим пучкам. Имеет уникальный идентификатор, определяемый функцией идентификации.

1. Система $-$ функция от времени и существующих пучков, где область значений это граф изображающий пучки точками, а существующие в данный момент пути между ними кривыми. При этом какие-то точки могут быть, в некоторые моменты времени, не связаны путями ни с какой-либо другой точкой.

Объекты взаимодействуют друг с другом путем отправления сообщений по путям. При этом, если они направлены от одного пучка к другому, то их сообщения обязаны проходить через корни по путям, определенным системой и внутренней структурой пучков. Приемник и источник узнаются используя дополнительные сообщения.

Далее представлены примеры, иллюстрирующие абстрактные определения
понятиями из области приложения. Пучок $-$ это научное учреждение или любая другая организация, обладающая центром (сервером для приема и отправки сообщений) и листьями (веб-страница публикации, сотрудника или организации). Примером системы является веб-система, объединяющая все существующие пучки, даже те которые в данный момент к ней не подсоединены (то есть нет пути который соединяет "отсоединенный" пучок с другими пучками), но были таковыми ранее. Она не позволяет напрямую менять одному корню листья другого. Сообщение же является ничем иным как запросом по протоколу HTTP или набором HTTP-запросов со специальными полями источник, цель. Ребро $-$ это какая-либо связь между корнями, листьями (сетевые маршруты по которым проходит сигнал, беспроводные адаптеры).

В такой постановке пусть у нас есть текущее состояние системы $S(t, P)$, где $t$ - дискретное время, а $P = (p_1(t), p_2(t), ..., p_n(t))$ набор пучков подключенных к системе в данный момент. 
Рассмотрим пример. ![](g)

Здесь # это главный сервер системы (центр), к которому подключаются корни пучков. Система может обходиться без главного сервера, например в случае если каждый корень связан с другими корнями (то есть образуется полный граф на корнях пучков). В общем же случае важно чтобы бы существовал путь от одного корня к другому (возможно проходящий через другие корни). Числа 1,2,3... это корни. Комбинации начинающиеся с \* обозначают страницы авторов, а с s публикации данных авторов. Данный граф отображает дерево адресов, так например, в листе s3 может быть упомянуто несколько авторов (соответствующих авторам листьев), но перейти при этом можно будет только на страницы тех кто подключен к системе в данный момент. В данном примере это \*1, \*2, ..., \*5.

## Изменение модели
Модель пока статична, но в реальной системе постоянно происходят изменения. В рамках настоящей работы изменения моделируются в терминах двух команд. Одна проверяет есть ли какие-либо изменения в упомянутых на листе адресах, а другая меняет указанный лист, удаляя, добавляя нужные URL адреса. 

Команда обновления уведомляет все адреса текущего узла. Это делается функцией сообщения, где источник адрес текущего узла, а цель поочередно все адреса указанные в узле.

Команда проверки исследует текущий узел на предмет того, что он являлся целью чьей-то функции сообщения. Если это так, то он добавляет в свой перечень адресов источники сообщений.

Для проведения дальнейших исследований и проверки результатов стоит реализовать построенный макет на компьютере. На нем будет осуществляться проверка функционирования всей системы и в случае недостаточности модели, исправление ее.

