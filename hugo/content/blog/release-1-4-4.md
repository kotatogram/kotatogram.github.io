+++
title = 'Kotatogram 1.4.4 beta released!'
date = "2021-09-22T21:01:00+03:00"
description = 'Updated sources, better unquoted forward, and option to disable chat themes.'
+++

This update needed to be released as soon as possible because of user IDs update in all Telegram apps. But since there is a huge leap from last source update, some things could break, so it's the beta again to make minimal needed tests. If there will no bugs, or they will be easy to fix, this version will be quickly promoted to steable. But this version also has few new features with fixes.

{{< subheader >}}
## Download 1.4.4 beta
based on Telegram Desktop 3.1
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 16.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-appimage.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.4/1.4.4-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}


## Changes

* **Added option to remember forward mode.** Earlier it was reset after restart. Now default forward mode is saved between restarts, but you can restore Telegram Desktop's behavior, which resets forward mode to default.
* **Added ability to set default forward mode.** Please not that if you have enabled remembering of forward mode, it will be re-written every time when it's changed in forward window. Otherwise this mode will always be selected by default.
* **Replaced unquoted forward method with option to restore the old one.** Old method copied message data on client, while new one doing that on server. Since new method is doing much better than the old one, it is used in most cases. The exception is "Regroup all media" grouping mode, since it's not supported by server. If for any reason you need the old method, you can enable it for all forward modes.
* **Added option to disable per-chat themes.** Since these themes can match bad with custom app themes and can hurt eyes when using custom dark app theme without using night mode switch, this Telegram feature wasn't liked by many users. If you also don't this themes because of the reasons above or any other reason, you can disable them.
* **Removed GTK integration option.** Since GTK integration is no longer needed, option isn't needed anymore too.

## Fixes

* Fixed missing sending inline bot response preview option.
* Fixed missing sending inline bot response preview in comments and scheduled messages.
* Fixed option "Disable edit by Up key" in comments and scheduled messages.

## Replaced by default

* **GIF section in shared media.** In TDesktop it's implemented differently, but there is no point in duplicating sections, so this section is now replace by default.
* **Forwarded sticker info.** It's now shown for all stickers, so there is no point in duplicating code, especially since there are no visual differences here.

## Why this update is important

Starting with making of Telegram, user IDs were stored in signed int32 which could hold up to 2,147,483,647 user IDs (including reserved ones). The problem is that pretty soon this quantity would be expended, so in order to prevent this, Telegram moved server and all its apps to int64 usage, which can hold up to 9,223,372,036,854,775,807 user IDs.

So what will happen on int32 overflow? Currently it's known that new users won't be able to register in Telegram. Also it's possible that old apps wouldn't work at all, if Telegram won't make some kind of reverse compatibility, which, sadly, less likely in this case.

## Few words about poll

Recently I've made the poll about how feature which influences chat themes should be properly named. With a small margin "Disable chat themes" has won, it will stay for now. But I understand what's the problem that started this entire poll: inverted switch logic can be confusing. I have an idea how to make such options more easy to understand, but releasing a new version was more important than re-working settings menu, so it will be done either in stable or after stable, which is more likely.
