# github-copilot-demo


## GitHub Copilot
- コメントからコード生成 (suggest.py)
  - `# Hello World を出力`
  - `Class Ani...` を入力しても続きが表示されない
  - context.py を開く
  - `Class Ani...` を入力すると context.py を元に続きが提案
- コンテキストファイルからコード提案 (context.py)


## GitHub Copilot Chat
- ソースコードの解説 (explain.py)
  - 右クリック > 「Copilot」 > 「Start in Editor」
  - 「この関数を説明して」と入力して実行
  - 該当コードを選択した状態で Copilot Chat 画面から質問
  - (「Explain This」は英語で出力されるため利用しない)
- バグ修正 (fix.py)
  - `python github-copilot-chat/bug.py` でバグの確認
  - 右クリック > 「Copilot」 > 「Fix This」
  - `python github-copilot-chat/bug.py` でバグの修正を確認
  - バグが修正しきれていない場合、再度「Fix This」を実行
- コメント生成 (generate-docs.py)
  - 右クリック > 「Copilot」 > 「Generate Docs」
- 日本語翻訳 (translate.py)
  - 右クリック > 「Copilot」 > 「Start in Editor」
  - 「日本語に置き換えて」と入力して実行
- コミットコメントの生成 (commit.py)
  - commit.py を変更
  - 変更をステージングして、☆を押下

