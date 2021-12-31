+++
title = 'Вышел Kotatogram 1.4.7!'
date = "2021-12-31T13:57:00+03:00"
description = 'Стабильная версия на стабильных исходниках и немного новых функций.'
+++

Последний релиз в этом году, необходимый, потому что кто знает, что будет, если стабильная ветка не получит обновление до 1 января. К счастью, «успеть до 1 января» не единственная суть релиза: новые функции тоже имеются в наличии.

{{< subheader >}}
## Скачать бету 1.4.7
на основе Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Поддерживает Windows 7 и выше. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 32-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="Установщик 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="Портативная 64-бит" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Поддерживает Ubuntu 18.04 и выше.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-linux.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Скачать" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Изменения с прошлой стабильной версии
* **Возможность отключить запоминание сжатие изображений при отправке.** В Telegram Desktop после отправки изображений всегда запоминается последний режим отправки. Это удобно, но иногда это приводит к тому, что при быстрой отправке можно случайно отправить изображение без сжатия, и придётся отправлять заново. Или наоборот. Это можно настроить опцией «Сжимать изображения по умолчанию». [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/243)
* **Пользовательские автозамены теперь работают без автозамены эмодзи.** На случай, если вы не любите стандартные автозамены, но вам нужны те, что вы настроили в JSON-файле. Если вы забыли, как их настраивать, на этот счёт есть [страница, которую я так и не перенёс с вики на сайт](https://github.com/kotatogram/kotatogram-desktop/wiki/%D0%A1%D0%B2%D0%BE%D0%B8-%D0%B0%D0%B2%D1%82%D0%BE%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D1%8B-%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0). [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/242)
* **Уменьшен минимальный размер окна.** Это изменение позволяет использовать приложение на более малых экранах.
* **Возможность переключать аккаунты горячими клавишами.** По умолчанию они назначены на `Alt+<цифра>`, но вы можете их поменять в JSON-файле, задав `account1` — `account9` (для аккаунтов от 1 до 9), а также `last_account` (для последнего аккаунта). [Добавлено контрибьютором.](https://github.com/kotatogram/kotatogram-desktop/pull/279)
* **Добавлена иконка рядом с именем автора в сообщении.** В группах теперь сразу можно увидеть, кто пишет от имени канала, кто от имени группы (т.е. является анонимным админом), а чей аккаунт был уже удалён. Также в каналах можно увидеть спонсированное сообщение сразу.

## Исправления с прошлой стабильной версии

* Исправлены должности в списке администраторов. Они могут быть чуть выше, чем раньше, но по крайней мере, теперь не уезжают за экран.
* Исправлена работоспособность протокола tg:// в системе. Это должно исправить проблему с ссылками в браузере.
* Исправлена опция «Внешний видеоплеер».

## Изменения с прошлой бета-версии
* Вместо [снятия ограничения на размер окна](https://github.com/kotatogram/kotatogram-desktop/pull/238) теперь изменены минимальные размеры самого окна. Это выполняет ту же задачу, но при этом окно не ломается до такой степени, что им невозможно пользоваться.
* Возможность переключать аккаунты горячими клавишами.
* Добавлена иконка рядом с именем автора в сообщении.
* При открытии анимированной аватарки в режиме «картинка-в-картинке» теперь выдаётся сообщение, что режим не поддерживается. Делать поддержку режима «картинка-в-картинке» у анимированных аватарок сложно, но оставлять вылет — плохая идея, поэтому там он отключён до лучших времён.

## Исправления с прошлой бета-версии
* Исправлены должности в списке администраторов.
* Исправлена автозагрузка медиафайлов на 32-битной версии под Windows.
