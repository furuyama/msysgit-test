1. Google Docs APIを試す方法
プログラムを実行する前に，createNewDoc.py, showAllTitle.pyそれぞれのソース中のメールアドレスとパスワードを自身の技芸ドメイン（または単にgmailアカウント）に変更する．
ローカルな環境であればこれだけでプログラムは動作する．
http://localhost:8080以下に/showを付け足すと現在のドキュメント一覧が表示され，/createを付け足すとGoogleDocumentsに３種類の新規ファイルを作成．

2. Datastore のアップロード／ダウンロードを試す方法
・バイナリファイルでアップロード／ダウンロードする場合
　端末でTestディレクトリ直下まで移動し，以下のコマンドを実行する
[Download]
appcfg.py download_data --application=<対象としたいアプリケーション名> --kind=<kind> --url=http://<アプリケーション名>.appspot.com/_ah/remote_api --filename=<保存したいファイル名>

<保存したいファイル名>とはMacなら例えば/Users/s.yamazaki/Documents/data.dumpなど．--kind==<kind>はオプションで，ダウンロードしたいモデルを指定できる．

[Upload]
appcfg.py upload_data --application=<アプリケーション名> --kind=<kind> --filename=<保存したいファイル名> <おそらくapp.yamlがあるフォルダを指定．src/など>

ただし，この方法でアップロード／ダウンロードできるのはバイナリファイルのみなので，あくまでバックアップにしかならない．

・テキストファイル(csv)でアップロード／ダウンロードする方法
　同じくTestディレクトリ直下にて以下のコマンドを実行
[Download]
appcfg.py download_data --config_file=bulkloader.yaml --filename=<保存したいファイル名.csv> --kind=Account --url=http://<アプリケーション名>.appspot.com/_ah/remote_api

[Upload]
appcfg.py upload_data --config_file=bulkloader.yaml --filename=<アップロードしたいファイル名.csv> --kind=Account --url=http://<アプリケーション名>.appspot.com/_ah/remote_api

