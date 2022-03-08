+++
title = 'Kotatogram 1.4.9 released!'
date = "2022-03-09T00:12:00+03:00"
description = 'Updated sources, internal rework of settings, and new features.'
+++

This version is released even though isn't fully ready, but there is no other way in current situation.

{{< subheader >}}
## Download 1.4.9 beta
based on Telegram Desktop 3.5.2
{{< /subheader >}}

{{< subheader >}}
### Windows
Supports Windows 7 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="32-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-win32-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="32-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-win32-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< button-group class="actions" >}}
    {{< button title="64-bit installer" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-win64-installer.exe" class="icon solid fa-download primary" >}}
    {{< button title="64-bit portable" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-win64-portable.zip" class="icon solid fa-download primary" >}}
{{< /button-group >}}

{{< subheader >}}
### Linux
Supports Ubuntu 18.04 and higher. 
{{< /subheader >}}

{{< button-group class="actions" >}}
    {{< button title="AppImage" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-linux.tar.xz" class="icon solid fa-download primary" >}}
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
    {{< button title="Download" link= "https://github.com/kotatogram/kotatogram-desktop/releases/download/k1.4.9/1.4.9-macos.dmg" class="icon solid fa-download primary" >}}
{{< /button-group >}}

## Changes
* **Internal rework of Kotatogram Settings.** This change that user won't notice allows to easier adding of new settings. I've even wrote a small developer reference: https://github.com/kotatogram/kotatogram-desktop/wiki/Kotatogram-Settings:-Quick-developer-reference
* **Restart to save settings now can be delayed.** You don't need to restart the app for ten times anymore: you can set up everything you need and restart after that.
* **Select time when jumping to date in chat.** Feature will be handy for chats that have so many messages per day that scrolling them from the start of the day is too long. Deleting chat history for selected days hasn't gone anywhere: choose "three dots" button in time and date select window, and then "Show calendar".
* **Experimental settings from Telegram Desktop now are always shown.** Recently Telegram Desktop implemented its own experimental settings, that can be found in Settings > Advanced. But sadly, in TDesktop they're shown only when autoupdate and beta versions enabled. Also it strips experimental settings away in builds without autoupdater. Kotatogram shows them always. Bonus: I've added an ability to translate them to different languages.
* **Name icon colors are now same as name colors.** I didn't like the idea of duplicating icons 8 times, and honestly, I still don't like it, But looking at how icons in 1.4.8 work, I've thought that visual part is more important. Nevertheless, since every one of them has separate color, nobody will stop you from making them same color.
* **Fixed profile picture cropping in native Windows notifications.** Sadly, native Windows notifications support only circle/square, but at least they're applied correctly.
* **"Emoji panel by hover" option replaced by default one.** Since experimental settings have own version of this option, I've decided to remove my own. Instead of it I've added two new options that allow to tune emoji panel more granulary: "Enable emoji sidebar" and "Emoji sidebar on right click".
* **"Show profile" as first menu item option.** After context menus update "Show profile" item was removed. At first I've restored it, moving it to the top, but later Telegram Desktop made its own option to return it. But since "Show profile" as first menu item may be more convenient, I've decided to make it as setting.

## Changes by the-blank-x

A lot of changes has been brought by **the-blank-x**. Among them:

* **Go to chat on Shift+Enter in Forward window.** Telegram Desktop, and subsequently, Kotatogram frequently lacks keyboard controls or hotkeys. So now Kotatogram has one more.
* **Warning when forwarding quiz unquoted.** Since unquoted forward doesn't work on quizzes that have no votes, now there's a message shown about it.
* "Copy callback data" menu item now shown on callback buttons only.
* Fixed useless message author name trimming when it has an icon.
* Fixed tg://user?id links for 64-bit IDs.
* Fixed useless "Mention user" menu item for channels.
* Fixed profile picture rounding in invite link window and calls window.
* Fixed filters in folders by administrator rights.

## New icon for macOS

For macOS version **gershik** drawn new icon in Big Sur style. I hope it will work correctly.

![](/blog/release-1-4-9/new_macos_icon_by_gershik_en.png)

---

And now few words about Kotatogram's future.

There are talks circling around for several days that Russia can disconnect from global internet. Since I live in Russia, disconnecting from global internet means that I physically won't be able to continue Kotatogram's development. I hope it's not true, and I'll be happy if it's not true. But if it will happen, I don't know how _soon_ I can return to Kotatogram's development (and will I return to it at all).

So I'm suspending Kotatogram's development until it will be clear what will be next. Sadly, I haven't implemented all things I wanted in this version, but source code is updated, so I don't want to leave it hanging. But I'll leave this version as beta, so you can use stable if you don't like reactions, for example.

> Important: **don't use the profile from new Telegram Desktop version on old one, it will lead to automatic logout on all sessions in profile!** Same applies to Kotatogram if TD versions are different. In other words: don't use profile from beta version on stable version.

Also I want to apologize to translators for not giving time to translation, but sadly, it's risky in current situation.

I hope this madness will end sooner.
