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

## P.128: リスト4.6.12でKeyErrorになる

KeyErrorは、settings.iniに指定した文字列が存在しない場合に発生します。  
まずは、コードの誤りやsettings.iniのテキストの入力ミスなどがないか、チェックしてください。

本書のサンプルファイルと比較してどこに違いがあるかは、テキストの差分を比較できるツールを使用すると便利です。  

例えば、以下のサイトなどがあります。  

- [テキスト比較ツール difff《ﾃﾞｭﾌﾌ》](https://difff.jp/)  

また、configparserの仕様上、config.read()の引数で指定したパスが正しくない場合もKeyErrorが出力されるので注意が必要です。  
