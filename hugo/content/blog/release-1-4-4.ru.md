+++
title = 'Вышла бета Kotatogram 1.4.4!'
date = "2021-09-22T21:01:00+03:00"
description = 'Обновление исходников, улучшение пересылки без автора и опция для отключения тем чатов.'
+++

Это обновление необходимо было выпустить как можно скорее из-за обновления пользовательских ID во всех приложениях Telegram. Но так как с предыдущего обновления исходников произошёл довольно внушительный скачок, некоторые вещи могли поломаться, поэтому снова бета, чтобы провести минимальные тесты. Если багов не будет, или они будут легкоисправимые — эта версия быстро уйдёт в стабильную. Но в этой версии также есть и немного новых функций с исправлениями.

{{< subheader >}}
## Скачать бету 1.4.4
на основе Telegram Desktop 3.1
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 16.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-appimage.tar.xz" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
#### Альтернативные способы
Имейте в виду, что они могут быть обновлены не сразу.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Страница на FlatHub" link= "https://flathub.org/apps/details/io.github.kotatogram" >}}
    {{< button title="Страница на Repology" link= "https://repology.org/project/kotatogram-desktop/versions" >}}
{{< /button-group >}}

{{< subheader >}}
### macOS
Поддерживает macOS 10.15 и выше.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения

* **Добавлена опция запоминания режима пересылки.** Раньше запоминание режима сбрасывалось после перезапуска. Теперь же по умолчанию режим пересылки сохраняется между перезапусками, но можно вернуть поведение из Telegram Desktop, при котором режим пересылки сбрасывается до того, что по умолчанию.
* **Добавлена возможность задать режим пересылки по умолчанию.** Имейте в виду, что если у вас включено запоминание режима пересылки, то он будет перезаписываться каждый раз при его изменении в окне пересылки. В ином случае этот режим всегда будет выбран по умолчанию.
* **Заменён метод пересылки без автора с возможность вернуть старый.** Старый метод производил копирование данных сообщения на клиенте, в то время как новый делает это на сервере. Так как новый метод справляется гораздо лучше старого, в большинстве случаев используется он. Исключение — режим группировки «Объединить все медиа», так как он не поддерживается сервером. Если по какой-то причине вам нужен старый метод, вы можете его включить для всех режимов пересылки.
* **Добавлена опция для отключения тем отдельных чатов.** Так как такие темы могут плохо сочетаться с пользовательскими темами, а также могут случайно ударить по глазам при использовании пользовательской тёмной темы без использования переключателя ночного режима, эта функция Telegram многим не понравилась. Если вам не нравятся такие темы по этой или любой другой причине, вы можете отключить их.
* **Убрана опция «GTK-интеграция».** Так как GTK-интеграция больше не требуется, опция также становится не нужна.

## Исправления

* Исправлена пропадающая опция отправки превью ответа от инлайн-бота.
* Исправлена отправка превью ответа от инлайн-бота в комментариях и отложенных сообщениях.
* Исправлена опция «Отключить редактирование по «Вверх»» в комментариях и отложенных сообщениях.

## Заменено стандартным

* **Раздел GIF в общих медиа.** В TDesktop он реализован иначе, но в дублировании разделов смысла нет, поэтому раздел был заменён стандартным.
* **Информация о пересланных стикерах.** Теперь она всегда отображается у всех стикеров, поэтому дублировать код смысла нет, тем более, что внешних различий никаких.

## Почему обновление важно

Начиная с самого создания Telegram, ID пользователя хранились в знаковом int32, который мог вместить 2 147 483 647 пользовательских ID (включая зарезервированные). Проблема в том, что уже довольно скоро это количество будет исчерпано, и чтобы этого не произошло, Telegram перевёл сервер и все клиенты на использование int64, который в себя может вместить 9 223 372 036 854 775 807 ID пользователей.

Что же произойдёт при превышении int32? На данный момент известно, что новые пользователи не смогут зарегистрироваться в Telegram. Также возможно, что старые клиенты будут просто не работать, если Telegram не сделает своего рода обратную совместимость, что, к сожалению, маловероятно в данном случае.

## Немного про опрос

Недавно я проводил опрос, где спрашивал, как лучше называть функцию, влияющую на темы чатов. С небольшим отрывом выиграл вариант «Отключить темы чатов», поэтому пока что остаётся он. Но проблема, из-за которой вообще начался этот опрос, мне понятна: инвертированная логика переключателей может запутать. У меня есть идея, как это можно сделать так, чтобы такие опции были понятнее, но сейчас было важнее выпустить новую версию, чем переделывать меню, поэтому это будет оставлено либо на стабильную, либо, что более вероятно, на версии после стабильной.
