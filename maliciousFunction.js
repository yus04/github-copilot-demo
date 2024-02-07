// @name: Simple JavaScript CodeQL Example
// @description: A simple JavaScript file for CodeQL scanning

// 悪意のあるコードの例
function maliciousFunction() {
    alert("This is a malicious function!");
  }
  
  // ユーザーからの入力を含むコード
  var userInput = prompt("Please enter some data:");
  
  // ユーザーからの入力を使用する箇所
  document.write("<p>" + userInput + "</p>");
  
  // セキュリティ上の脆弱性の例
  eval("maliciousFunction()"); // evalを使用することはセキュリティ上のリスクとなります
  