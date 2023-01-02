# FAQ

よくある質問を掲載しています。

## P.5: Jupyter Notebook以外のIDEの使用について

本書では、アプリケーション開発のIDE(統合開発環境)としてJupyter Notebookを使用して解説しています。  
既に他のIDEを使用している方は、Jupyter Notebookにこだわらず、ご自身の使いやすいもので学習を進めていただいて問題ございません。  

例えば、Jupyter Notebook以外の選択肢として以下のようなIDEが有名です。  
- [PyCharm](https://www.jetbrains.com/ja-jp/pycharm/)
- [PyScripter](https://www.embarcadero.com/jp/free-tools/pyscripter/free-download)
- [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)

色々なソフトウエアに触れて、最終的に使いやすいものを見つけてみてください。  

## P.18:　アプリケーションウインドウが表示されない  

正しくコードを入力しても、アプリケーションウインドウが表示されない場合は、Jupyter Notebookのカーネルが正常に起動していない可能性があります。カーネルについては本書のP25に記載があります。P25の方法に従い、カーネルを一度リセットしてみてください。  

PCやJupyter Notebookを再起動、またはAnacondaを再インストールしても症状が改善しない場合は、他に原因がある可能性があります。  

Jupyter Notebookを起動した際のシェル画面(Windowsはプロンプト、Macはターミナル)に、ErrorやWarningといったエラーメッセージが出力されているか確認してください。  

また、古いPCまたはソフトウエアをお使いの場合や、相性の問題で稀にエラーが発生するケースもあるようです。  

こういった問題が原因の場合は、シェル画面に表示されるエラーメッセージをGoogleなどで検索してみると解決策が見つかることがあります。  

エラーメッセージの内容をメールでお送りいただければ、解決策をご提案することも可能です。お使いのPCやOSの種類、仮想環境の使用の有無、Anacondaをインストールする前に別のPython環境を導入していたかなど、併せて詳細をご連絡ください。  


## P.128: リスト4.6.12でKeyErrorになる

KeyErrorは、settings.iniに指定した文字列が存在しない場合に発生します。  
まずは、コードの誤りやsettings.iniのテキストの入力ミスなどがないか、チェックしてください。

本書のサンプルファイルと比較してどこに違いがあるかは、テキストの差分を比較できるツールを使用すると便利です。  

例えば、以下のサイトなどがあります。  

- [テキスト比較ツール difff《ﾃﾞｭﾌﾌ》](https://difff.jp/)  

また、configparserの仕様上、config.read()の引数で指定したパスが正しくない場合もKeyErrorが出力されるので注意が必要です。  
