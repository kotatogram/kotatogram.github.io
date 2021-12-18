+++
title = 'Вышла бета Kotatogram 1.4.3!'
date = "2021-08-26T22:16:00+03:00"
description = 'Немного новых функций и исправлений.'
+++

Это обновление довольно малое по функциям, но содержит внутренню работу над версионированием и обновлениями, которая сокращает пересборку. А ещё в этот раз я не забыл про переводы, и теперь в Котатограм даже есть немецкий язык.

{{< subheader >}}
## Скачать бету 1.4.3
на основе Telegram Desktop 2.8.11
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 16.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.3/1.4.3-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения

* **Переделана опция отправки без метки «via @bot»**. Настройка была убрана, а пункт в контекстном меню теперь отправляет превью инлайн-запроса. Также были добавлены пункты для отправки без звука и отложенной отправки превью.
* **Опциональные сочетания клавиш для перезапуска приложения и перезагрузки перевода Kotatogram.** `restart_app` для перезапуска и `reload_lang` для перезагрузки перевода назначаются там же, где и раньше: `tdata/shortcuts-custom.json`.
* Обновлены переводы, включая фразы с прошлой версии.

## Исправления

* Исправлена блокировка пользователя из «Недавних действий».
* Исправлены ошибки и вылеты в AppImage, связанные с gdk-pixbuf.
