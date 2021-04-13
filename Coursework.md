# В работе используются следующие технологии:
## 1. Webmention.
Webmention (веб-упоминание) - это веб-стандарт для упоминаний и коммуникации в сети. Он является одним из базовых блоков общения для растущего дерева комментариев, лайков, репостов и других разнообразных взаимодействий в децентрализованной социальной сети.
### Общий принцип работы.
Веб-упоминания отправляются "от" исходного адреса URL ресурса "к" целевому адресу URL ресурса, чтобы уведомить цель о том, что она была упомянута в исходном адресе URL ресурса по следующему обобщенному алгоритму:

1. Пользователь Миша пишет пост в своем блоге.
2. Пользователь Женя пишет пост в своем блоге, который ссылается на пост Миши.
3. После того, как у поста появляется адрес URL, сервер Миши помечает упоминание сообщения Жени, как часть процесса публикации.
4. Сервер Миши создает упоминание _Webmention_ на посту Жени, чтобы найти конечную точку своего упоминания _Webmention_ (если она не найдена, процесс останавливается).
5. Сервер Миши отправляет уведомление _Webmention_ на конечную точку упоминания _Webmention_ публикации Жени следующим образом:
    * __источник (source)__ назначается на постоянную ссылку сообщения Миши
    * __цель (target)__ назначается на постоянную ссылку сообщения Жени.
6. Сервер Жени получает уведомление _Webmention_.
7. Сервер Жени проверяет, что __target__ в _Webmention_ является допустимой постоянной ссылкой в его блоге (если нет, обработка останавливается).
8. Сервер Жени проверяет, что источник __source__ в упоминании _Webmention_ (при извлечении, после FETCH перенаправлений) содержит гиперссылку на цель __target__ (если нет, обработка останавливается).

## 2. Протокол WebSub.
WebSub - предоставляет общий механизм связи между издателями любого вида веб-контента с их подписчиками, основанный на веб-крюках HTTP-web-hooks. Запросы на подписку повторно передаются через концентраторы, которые валидируют и верифицирют запрос (то есть проверяют то что запросы созданы правильно и то что они созданы такими какими предполагались). Затем концентраторы распространяют новый или обновленный контент среди подписчиков, после того как он становится доступен.

### Основные определения:
1. __Тема__.
    Адрес URL ресурса HTTP (HTTPS). Единица, на изменения которой можно подписаться.
2. __Концентратор__. 
    Сервер (адрес URL), реализующий обе стороны этого протокола. Любой концентратор _МОЖЕТ_ реализовать свои собственные политики в отношении того кто имеет право им пользоваться.
3. __Издатель__.
    Владелец темы. Уведомляет концетратор об обновлении тематической ленты. Издатель не знает подписчиков, если таковые имеются.
4. __Подписчик__.
    Организация (человек/программа), которая хочет получать уведомления об изменениях в теме. Подписчик должен иметь прямой доступ к сети и идентифицироваться по адресу URL обратного вызова себя.
5. __Подписка__.
    Уникальное отношение подписчика к теме, показывающее что он должен получать обновления этой темы. Уникальным ключом подписки является неизменяемый список (кортеж) (адрес URL темы, адрес URL обратного вызова подписчика). Подписки могут (если так решит концентратор) иметь определенное время действия.
6. __Адрес URL обратного вызова подписчика__.
    Адрес URL по которому подписчик желает получать запросы о распространении контента.
7. __Мероприятие__.
    Событие, вызывающее обновления нескольких тем (возможно одной). Каждое происходящее событие (например «Миша опубликовал сообщение в сообществе Linux.») может затронуть несколько тем (здесь «Миша опубликовал сообщение.» и «В сообществе Linux появилось новое сообщение.»). _Мероприятия_ вызывают обновление тем. Затем концентратор просматривает все подписки на затронутые темы, ища и доставляя контент подписчикам.
8. __Уведомление о распространении контента / (запрос на распространение контента)__.
    Полезная нагрузка, содержащая изменения темы или полностью обновленную тему. В зависимости от типа наполнения раздела дельта может быть вычислена концентратором и отправлена всем подписчикам.

### Общий принцип работы:
1. Подписчики обнаруживают концентратор адреса URL темы и отправляют сообщение POST в один или несколько объявленных концентраторов, чтобы получать обновления при изменении раздела.
2. Издатели уведомляют свои адреса URL концентраторов об изменении тем(ы).
3. Когда концентратор идентифицирует изменение в разделе, он отправляет уведомление о распространении контента всем зарегистрированным подписчикам.

## 3. Язык разметки Microformats2.
Microformats2-это последняя версия микроформатов, самый простой способ разметки структурированной информации в HTML. Microformats2 улучшает простоту использования и реализации как для авторов (издателей), так и для разработчиков (разработчиков парсеров) по сравнению с прошлой версией. Главное отличие от других способов разметки файлов HTML состоит в том, что он поддерживает создание дополнительных классов.

### Префиксы для имен классов.
Все имена классов микроформатов используют префиксы. Префиксы-это синтаксис, независимый от словарей, которые разрабатываются отдельно.
1. __h-*__ для имен корневых классов (например h-card)
2. __p-*__ для свойств обычного текста (например p-name)
3. __u-*__ для свойств адреса URL (например u-photo)
4. __dt-*__ для свойств даты/времени (например dt-bday)
5. __e-*__ для встроенных свойств разметки (например e-note)

# Распределенная сеть the solid ecosystem
__Solid__ - это промежуточная итерация от изобретателя всемирной паутины сэра Тима Бернерса-Ли. Она представляет собой оригинальное видение Тима о Сети как средстве безопасного, децентрализованного обмена публичными и частными данными.

## Принципы работы
1. На Solid сервере размещается один или несколько Solid модулей, доступных по протоколу Solid.
2. Модуль, размещенный на Solid сервере, полностью отделен от всех остальных. Он имеет свой собственный набор данных и правил доступа и полностью контролируется тем, кому он принадлежит (то есть вами).
3. Вы сами решаете, где разместить свой модуль. Вы можете выбрать, чтобы он был размещен для вас расширяющейся сетью поставщиков модулей-устройств, или вы можете разместить его самостоятельно.
4. Вы также можете иметь более одного модуля, размещенного в разных местах. Это эффективно прозрачно для приложений и служб, которые вы используете, потому что ваши данные, где бы они ни были размещены, или данные, которыми вы поделились, все связаны через вашу личность.
5. Вы можете хранить любые данные в Solid модуле, и вы можете определить, кто или что может получить доступ к этим данным на детальном уровне, используя системы аутентификации и авторизации Solid.
6. Хранимые вами данные совместимы с другими. Это возможно благодаря открытым стандартам форматов, которые могут быть проверены Solid сервером, для гарантии сохранения целостности данных после взаимодействия с ними разрозненных приложений.

Подводя итог это означает, что вы можете делиться определенными вами частями ваших данных с другими людьми и группами, которым вы доверяете, или с экосистемой приложений и сервисов, которые могут читать и записывать данные в вашем модуле, используя стандартные шаблоны для взаимодействия приложений. И точно так же, как вы можете поделиться своими данными с другими, они могут поделиться своими данными с вами.

# Список литературы.
1. https://www.w3.org/TR/webmention/
2. https://www.w3.org/TR/websub/
3. http://microformats.org/wiki/microformats2
4. https://solidproject.org/