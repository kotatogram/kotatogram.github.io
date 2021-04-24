+++
Title = "FAQ"
description = "Frequently asked questions about Kotatogram Desktop."
layout = "single"
+++

Here tackled some questions that asked pretty frequently.

* [When update?](#when-update)
* [Will ghost mode/blocked users ignore be made?](#ghost-mode)
* [Will Android version be made?](#android)
* [My anti-virus detects Kotatogram as a malware!](#antivirus-detect)
* [Is it true that account can be banned because of unofficial client usage?](#alt-client-bans)
* [Do you have any plans to monetize Kotatogram?](#monetize)

#### When update? {#when-update}

I'm trying not to tell exact dates, because usually I fit into them only when everything is ready.

But keep in mind: even there are no updates for time, fork is not abandoned, because I use it every day.

#### Will ghost mode/blocked users ignore be made? {#ghost-mode}

No. I'm not going to make features that violates Telegram API Terms of Service. This may result in problems for both fork and its users.

Following features currently considered as violating Telegram API Terms of Service:

* Ghost mode (hiding online status, read status notifications and so on)
* Ignore blocked users in chat
* Hiding proxy sponsor in chat list
* Un-deletion of messages

It's possible that if Telegram will add ads, its removal will also be considered as Telegram API TOS violation.

#### Will Android version be made? {#android}

I'm not planning to make Android version. Maybe I'll experiment in future, but it's unlikely that I'll make a complete app.

#### My anti-virus detects Kotatogram as a malware! {#antivirus-detect}

Kotatogram has no viruses. If you have any doubts, you can check app source code, and if you don't trust binaries built by me, you can build your own.

I'm not publising only API ID/hash for Telegram API access and private keys for auto-updater. Other than that, Kotatogram is built from exactly same source code on GitHub.

About false positives of anti-viruses: main reason is auto-updater. Since Kotatogram on Windows doesn't have digital signature, anti-viruses predeterminedly have less trust for it. But even signed Telegram Desktop had these problems.

Only thing that can be done here is reporting false positives to anti-virus companies to make them re-check and clean detection manually.

#### Is it true that account can be banned because of unofficial client usage? {#alt-client-bans}

Sadly, there are cases like that, if client uses custom API ID and hash. Risc is bigger for virtual numbers, but many reports came from Russian phone number users.

Currently it happens less often (or I just receive reports less often). But if that happened to your account, you can write to recover@telegram.org or login@stel.com. Also you can open your mail app to send e-mail to login@stel.com with specific template by clicking "Help" button when trying to login to account.

#### Do you have any plans to monetize Kotatogram? {#monetize}

Not at the time. If I'll decide to monetize it, probably it would be donations. But I'm not going to put advertisements to it.
