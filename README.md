# systemproject
# ラズパイGUI(クライアント)
ラズパイのGUIはsystemproject.zipとして配布している．
## 下準備
systemproject.zipを解凍する．
ラズパイのGUIを使うためにはまずPythonのライブラリをインストールする必要がある．
Python,pipはすでにインストールされている前提として
プラットフォームに合わせて，必要なライブラリをインストールする．
### Linuxの場合
Linuxの場合は端末を起動してコマンドラインから以下のコマンドを実行する．
```shell
# レポジトリのディレクトリへ移動してから
sh ./install.sh # 必要なライブラリをインストール
```

### Windowsの場合
Windowsの場合は
zipファイルを解凍し，そのディレクトリのなかへ移動してから
ディレクトリ内の**install.bat**をダブルクリック

## ラズパイGUI(クライアント)利用方法
ラズパイのGUIは履修者データをダウンロードし，その履修者データを用いて出席管理を行い，そのデータをサーバにアップロードするために使用される．

前章の操作により必要なライブラリをインストールした後に
以下に記すサーバのIPアドレスの設定を行い，
プラットフォームに合わせて以下のコマンドまたは操作を行い，表示されるランチャーの3つのボタンをクリックすることでダウンロード，アップロード，出席管理の各種機能が使用できる．
それぞれの使い方については後述する．
### Linuxの場合
```shell
# レポジトリのディレクトリへ移動してから
sh ./run.sh # 実行
```

### Windowsの場合
zipファイルを解凍し，そのディレクトリのなかへ移動してから
**run.bat**をダブルクリック

### 設定
クライアントを使用する前に履修者データのダウンロードと出席データのアップロードを行うためのサーバのIPアドレスを設定する必要がある．
サーバマシンから
```sh
ifconfig # Linux
ipconfig # Windows
```
を実行するなどして
サーバのIPアドレスを確認し，
そのIPアドレスをRaspberrypi/GUI/tusin.pyのserverIP変数に記載する．
例として以下のように設定することができる．
```python
serverIP = '192.168.1.11'
```

## GUIの機能
### ダウンロード
履修者データをダウンロードする．

この機能はクライアントマシンがサーバと同じネットワークに接続されているときに使用できる．
出席管理を行いたい科目のIDを選択し，ダウンロードボタンをクリックする．

### アップロード
出席データをアップロードする．

この機能はクライアントマシンがサーバと同じネットワークに接続されているときに使用できる．
アップロードしたい科目IDと授業回数をコンボボックスから選択肢，アップロードのボタンを押すことでその授業回数の出席データがサーバにアップロードされる．
アップロードが成功するとアップロードに使用した出席データのファイルを削除する．

### 出席管理メイン画面
履修者データを用いて出席管理を行い，その結果を出席データとして保存する．

起動画面(スタート画面)で出席管理を行いたい科目のIDと授業回数を選択し，開始ボタンを押すことで出席管理画面に遷移する．
このとき，出席管理を行いたい科目の履修者データがない場合は警告が表示されるので，ダウンロード画面を起動し，その科目の履修者データをダウンロードする必要がある．
出席管理画面ではカードからIDを読み取った場合に規則時間と現在時刻を比較し，出席かどうかが表示される．(今回はターミナルでエンターキーを押すことでIDを読み取る．)
出席管理を終える場合は終了ボタンを押す．
ここで取られた出席データをサーバにアップロードする場合はアップロードGUIを起動し，アップロードを行う．


# サーバ
サーバはsousei.zipとして配布している．
~~実際はnginxのインストールとその設定が必要だが，簡単のためインストールは省略する．~~

Dockerを用いて仮想環境上ですべてのソフトウェアを用意する．
## 必要なソフトウェア
- ~~python~~
- ~~mariadb~~
- ~~nginx~~
- docker
    - nginxコンテナ(python3.7)
    - mariadbコンテナ
    - phpmyadminコンテナ

## dockerのインストール
### Linuxの場合
使用しているパッケージマネージャに合わせて以下のコマンドを実行することで大半のLinux環境では使用できると思われる．
```sh
sudo apt install docker docker-compose # ubuntu,debian系
sudo zypper install docker docker-compose # opensuse
sudo pacman -S docker docker-compose # archlinux系
```
Dockerのインストール後にDockerのサービスを有効化する．
```sh
systemctl start docker # docker有効化
```

### windowsの場合
[docker公式サイト](https://www.docker.com/products/docker-desktop)
からインストーラをダウンロードし，
[docker公式ドキュメント](https://docs.docker.jp/docker-for-windows/wsl.html)
を参考にインストールする

### Docker動作確認
インストールが完了したと思われる状態になったら，
```sh
docker -v
# -> Docker version 20.10.7, build f0df35096d
docker-compose -v
# -> docker-compose version 1.29.2, build unknown
```
を実行し，dockerとdocker-composeコマンドが利用可能なことを確認する．
また，Docker公式のHelloWorldイメージを利用し，DockerHubからイメージが取得可能なことを確認する．
```sh
docker run --rm hello-world
# -> Hello from Docker!
# -> This message shows that your installation appears to be working correctly.
```

Dockerが実行できていない場合は一度再起動して，再び上記コマンドを実行してみる．
それでも実行できない場合はBIOSからCPUの仮想化機能が有効になっているかを確認する．
Windowsの場合はHyper-Vの機能かWindows Subsystem for Linuxが有効になっているかも確認する．

## サーバの実行方法
server.zipを解凍後docker-compose.ymlのあるディレクトリに移動して，
```sh
docker-compose up -d --build
```
を実行することで，システムで使用するnginxとmariadbとphpmyadminのイメージがダウンロードされ，サーバが実行される．

ブラウザで[http://*ipadress*:13431/](http://ipadress:13431/)(サーバを起動したマシンと同じマシンからのアクセスの場合 localhost:13431)にアクセスし，ログインページが返されることを確認する．
デフォルトのログインパスワードはそれぞれの教員のIDと同じに設定されている(例として，IDが**P001**の教員の場合パスワードも**P001**)．


