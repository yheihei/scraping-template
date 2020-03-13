<?php

/**
 * phpでスクレイピングツールを動かし、結果のcsvをダウンロードするサンプル
 */

// pythonでスクレイピング実行
exec('python scraping.py 2>&1',$output,$result);

if($result === 1) {
    echo "failed!!";
    // 結果出力
    var_dump($output);

    echo "<br>";
    return;
}

// ファイルのパス
$filepath = 'result.csv';
 
// リネーム後のファイル名
$filename = 'result_'.date("Ymd").'.csv';
 
// ファイルタイプを指定
header('Content-Type: application/force-download');
 
// ファイルサイズを取得し、ダウンロードの進捗を表示
header('Content-Length: '.filesize($filepath));
 
// ファイルのダウンロード、リネームを指示
header('Content-Disposition: attachment; filename="'.$filename.'"');
 
// ファイルを読み込みダウンロードを実行
readfile($filepath);



