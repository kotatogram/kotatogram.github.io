+++
Title = "Test versions"
description = "Some information about test versions of Kotatogram Desktop."
layout = "single"
+++

[< Back to FAQ](/faq)

* [What are the test versions?](#about)
* [Will they have auto-updates?](#auto-updates)
* [Can I use my existing Kotatogram Desktop profile?](#existing-profile)
* [How to report a bug in test version?](#bug-report)
* [How to disable debug logs?](#debug-logs)
* [Where to download test version?](#download)

#### What are the test versions? {#about}

Test versions are experimental pre-release versions of Kotatogram Desktop. They needed to test specific changes that can be possibly made in Kotatogram Desktop.

Keep in mind that all changes in the test versions are not final and there is no guarantee that they will be made in Kotatogram stable branch.

#### Will they have auto-updates? {#auto-updates}

Yes, but you can update only to test versions of same branch. Also you can't update to stable or beta, because it's the separate branch.

#### Can I use my existing Kotatogram Desktop profile? {#existing-profile}

Alpha versions in Telegram Desktop and subsequently test versions in Kotatogram Desktop use only `TelegramForcePortable` near executable as profile folder. You certainly can copy your existing profile to it, but it's **highly discouraged** to do so.

Test versions can contain breaking changes and make your profile incompatible with other versions. For example, if Telegram Desktop version in test version will be higher than in stable or beta, using this profile in stable or beta will lead to logout.

Also if new options are introduced, their values will be lost when switching to version without this option.

#### How to report a bug in test version? {#bug-report}

Test version bugs are accepted in [Kotatogram chat](https://t.me/kotatochat) in Telegram. Also you can report directly to [@RadRussianRus](https://t.me/RadRussianRus) in Telegram.

**Please note:** bug reports are accepted only for latest versions. Also it would be helpful to test if bug the bug exists in the corresponding version of Telegram Desktop if it's not about Kotatogram-exclusive feature.

#### How to disable debug logs? {#debug-logs}

Before you'll do it: since test versions are exist to check if features are working, logs can be useful for understanding the causes of the problem.

If you're sure that they're not usefil to you, you can enter cheat code `debugmode` in settings. To enter it you'll need only to open settings and type it on keyboard.

#### Where to download test version? {#download}

**Important:** read test versions FAQ before using them! 

Test versions can be downloaded from [separate Telegram channel](https://t.me/ktgtests). You can find latest test versions in its pinned message.

