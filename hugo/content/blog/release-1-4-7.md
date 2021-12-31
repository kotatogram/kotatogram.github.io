+++
title = 'Kotatogram 1.4.7 released!'
date = "2021-12-31T13:57:00+03:00"
description = 'Stable version on stable sources with some new features.'
+++

Last release in this year which is needed because who knows what happen if stable branch won't receive update until January 1. Luckily, the "make it before January 1" thing is not the only point of the release: new features are also in stock.

{{< subheader >}}
## Download 1.4.7 stable
based on Telegram Desktop 3.3
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 18.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-linux.tar.xz" class="icon solid fa-download primary" >}}
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
### macOS
Supports macOS 10.15 and higher.
{{</ subheader >}}

{{< button-group class="actions" >}}
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.7/1.4.7-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}


## Changes since last stable version

* **Ability to disable remembering image compression when sending.** Telegram Desktop always remembers last sending mode after images were sent. It's handy, but sometimes it leads to sending images without compression by mistake when sending fast, after which you need to re-send them again. Or the other way around. You can select the mode you need by "Compress images by default" option. [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/243)
* **Custom auto-replaces now work without emoji replacement enabled.** In case if you don't like default auto-replacements but you need those you have set in JSON file. If you forgout how to set them, there is [a page that wasn't moved to site from wiki](https://github.com/kotatogram/kotatogram-desktop/wiki/Custom-text-replaces). [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/242)
* **Lowered minimum window size.** This change allows to use the app on much smaller screens.
* **Ability to switch accounts by hotkeys.** By default they're bound to `Alt+<digit>`, but you can switch them in JSON file by setting `account1` — `account9` (for accounts from 1 to 9) and also by setting `last_account` (for the last account). [Added by contributor.](https://github.com/kotatogram/kotatogram-desktop/pull/279)
* **Added icon near the author name in message.** Now you can easily tell who writes from channel's name, who writes from group's name (i.e. is anonymous admin) and whose account has been already deleted. Also you can easily spot sponsored message in channels.

## Fixes since last stable version

* Fixed ranks in admin list. They can be slightly higher than before, but at least they're staying on screen now.
* Fixed tg:// link protocol in system. It must solve browser links problems.
* Fixed "External video player" option.

## Changes since last beta version
* Instead of [removing window size restiction](https://github.com/kotatogram/kotatogram-desktop/pull/238) minumum window size was changed. It solves the same problem, but at least window is not breaking until the point it's not usable.
* Ability to switch accounts by hotkeys.
* Added icon near the author name in message.
* Message about unsupported mode is now shown when opening animated profile picture in picture-in-picture mode. Implementing PiP for animated profile pictures is hard, but leaving the crash as-is is a bad idea, so it's disabled there until better days.

## Fixes since last beta version
* Fixed ranks in admin list.
* Fixed automatic downloading of media files in 32-bit Windows version.
