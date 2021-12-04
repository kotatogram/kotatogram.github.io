+++
title = 'Kotatogram 1.4.5 released!'
date = "2021-12-04T15:12:00+03:00"
description = 'Updated sources and some fixes.'
+++

This version is not much different from 1.4.4, apart from some bug fixes and moving to stable branch. Stable branch, besides existing crash because of chats with 1 month auto-deletion, now have new problem. Users can't login in this version anymore, and on the top of that there are constant messages that insist on updating.

{{< subheader >}}
## Download 1.4.5 stable
based on Telegram Desktop 3.1.1
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.5/1.4.5-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.5/1.4.5-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.5/1.4.5-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.5/1.4.5-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.5/1.4.5-linux.tar.xz" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
#### Alternative options
Please note that update can be delayed.
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="FlatHub page" link= "https://flathub.org/apps/details/io.github.kotatogram" >}}
    {{< button title="Repology page" link= "https://repology.org/project/kotatogram-desktop/versions" >}}
{{< /button-group >}}

{{< subheader >}}
### macOS {#stable-macos}
Currently not updated because of error in build process. It will be available as soon as it fixed.
{{</ subheader >}}

## Changes since last stable version

* **Manually choose notification mute time.** Default options (1 hour/4 hours/18 hours/3 days) are replaced by input field, where you can choose notification mute time yourself.
* **Auto-login option for Telegram sites.** Telegram Desktop have it always enabled, but if you don't like it for some reason, you can disable it now.
* **Multi-threaded video decoding option.** When enabled, video may lag less often or don't lag at all, but it will require more CPU and RAM consumption. Also you can limit thread count with `ffmpeg_thread_count` option in JSON settings file. Option has been added by [https://github.com/ilya-fedin](@ilya-fedin).
* **External video player.** This option has been hidded under `videoplayer` cheat code. Now you can switch it in [Kotatogram settings](tg://settings/kotato), so cheat code has been removed. In case you haven't heard about this feature from Telegram Desktop, it allows to play video in system video player instead of internal one. Option has been added by [https://github.com/ilya-fedin](@ilya-fedin).
* **Sending preview of inline query.** Option allows to send inline bot results without "via @bot" mark. It works with media files and stickers. Please note that sending preview will send exactly same file that shown in inline query result, even if bot changes it after sending (which is impossible when sending a preview, since it sends as a copy).
* **Font size JSON option.** `fonts` > `size` allows to set _relative_ font size, i.e. 0 is default, 1 is 1 px bigger, -1 is 1 px less, etc. Option has been added by [https://github.com/ilya-fedin](@ilya-fedin).
* **Unfocused auto-scroll option.** When enabled, opened chat will auto-scroll if your window is unfocused. Option has been added by [https://github.com/ilya-fedin](@ilya-fedin).
* **Added option to remember forward mode.** Earlier it was reset after restart. Now default forward mode is saved between restarts, but you can restore Telegram Desktop's behavior, which resets forward mode to default.
* **Added ability to set default forward mode.** Please not that if you have enabled remembering of forward mode, it will be re-written every time when it's changed in forward window. Otherwise this mode will always be selected by default.
* **Replaced unquoted forward method with option to restore the old one.** Old method copied message data on client, while new one doing that on server. Since new method is doing much better than the old one, it is used in most cases. The exception is "Regroup all media" grouping mode, since it's not supported by server. If for any reason you need the old method, you can enable it for all forward modes.
* **Added option to disable per-chat themes.** Since these themes can match bad with custom app themes and can hurt eyes when using custom dark app theme without using night mode switch, this Telegram feature wasn't liked by many users. If you also don't this themes because of the reasons above or any other reason, you can disable them.
* **Removed GTK integration option.** Since GTK integration is no longer needed, option isn't needed anymore too.
* Localized self-destruct messages button to Russian.

## Fixes since last stable version

* Fixed option "Disable edit by Up key" in comments and scheduled messages.
* Fixed missing "Copy Share Link" in forward window when a single album is selected.
* Fixed applying of some bundled Kotatogram translations.

## Replaced by default

* **GIF section in shared media.** In TDesktop it's implemented differently, but there is no point in duplicating sections, so this section is now replace by default.
* **Forwarded sticker info.** It's now shown for all stickers, so there is no point in duplicating code, especially since there are no visual differences here.

## Fixes since latest beta version

* Fixed caption sending modes in unquoted forward. Fixed by [https://github.com/the-blank-x](@the-blank-x).
* Fixed "Qt scaling" option. Fixed by [https://github.com/ilya-fedin](@ilya-fedin).
* Removed duplicate of GIF button in shared media.
* Fixed animated emoji size.
* Fix custom font size scale. Fixed by [https://github.com/ilya-fedin](@ilya-fedin).
