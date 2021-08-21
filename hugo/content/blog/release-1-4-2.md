+++
title = 'Kotatogram 1.4.2 beta released!'
date = "2021-08-21T21:07:00+03:00"
description = 'Fixes and source update to 2.8.11.'
+++

Since this version caught some beta version commits, the beta has been released. But aside from sources update, there is a few new features and fixes.

{{< subheader >}}
## Download 1.4.2 beta
based on Telegram Desktop 2.8.11
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win32-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win64-setup.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
Supports macOS 10.15 and higher. 
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.2/1.4.2-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Changes

* **Manually choose notification mute time.** Default options (1 hour/4 hours/18 hours/3 days) are replaced by input field, where you can choose notification mute time yourself.
* **Auto-login option for Telegram sites.** Telegram Desktop have it always enabled, but if you don't like it for some reason, you can disable it now.
* **Multi-threaded video decoding option.** When enabled, video may lag less often or don't lag at all, but it will require more CPU and RAM consumption. Also you can limit thread count with `ffmpeg_thread_count` option in JSON settings file. Option has been added by @Shlyupa.
* **External video player.** This option has been hidded under `videoplayer` cheat code. Now you can switch it in [Kotatogram settings](tg://settings/kotato), so cheat code has been removed. In case you haven't heard about this feature from Telegram Desktop, it allows to play video in system video player instead of internal one. Option has been added by @Shlyupa.
* **Sending without "via @bot" mark.** Allows to send inline bot results without their mention. Actually works only with @gif, other will only show that message was send without tag. Option has been added by @Shlyupa.
* **Font size JSON option.** `fonts` > `size` allows to set _relative_ font size, i.e. 0 is default, 1 is 1 px bigger, -1 is 1 px less, etc. Option has been added by @Shlyupa.
* **Unfocused auto-scroll option.** When enabled, opened chat will auto-scroll if your window is unfocused. Option has been added by @Shlyupa.
* **Backported message self-destruct 1 month option.** It also should fix constant crashes when there is at least one chat with 1 month self-destruct option.

## Fixes

* Localized self-destruct messages button to Russian.
* Fixed missing "Copy Share Link" in forward window when a single album is selected.
* Fixed applying of some bundled Kotatogram translations.

---

I've also forgot to apply some translations from Crowdin, sorry. I'll apply them in next release.
