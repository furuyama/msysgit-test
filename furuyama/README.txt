【Google App Engine の XMPPプロトコルを使用してGoogle Talkにメッセージを送信する】

1. XMPPプロトコルを使用するための準備
"from google.appengine.api import xmpp" と入力し、xmppプロトコルをインポートします。

2. XMPP Python APIの使用
get_presence(jid, from_jid=None)
->Google Talkユーザのオンライン・オフライン状況の取得

send_message(jids, body, from_jid=None, message_type=MESSAGE_TYPE_CHAT, raw_xml=False)
->引数に指定したユーザに、引数に指定したメッセージを送信
->返り値は、以下の3つ
  * xmpp.NO_ERROR: 正常に送信完了
  * xmpp.INVALID_JID: 指定したユーザ名が存在しない
  * xmpp.OTHER_ERROR: 上記2つ以外のエラー

3. ソースコードの使用方法
変数 to_addressに送信先のGmailアドレスを入力してください。
ただし、送信先ユーザがこのアプリケーションをチャットに招待している必要があります。
(そうしないとスパム的にメッセージが送れまくってしまうため)

4. このアプリケーションをGoogle App Engineにデプロイしてくだい。
※ローカルで試している時はコンソールにログが出るだけで、GTalkには送れません


[参考]
The XMPP Python API(XMPPの概要やリファレンスがあります)
http://code.google.com/intl/ja/appengine/docs/python/xmpp/


